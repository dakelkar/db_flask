import datetime
from flask import Flask, render_template, flash, redirect, url_for, session, request
from passlib.hash import sha256_crypt
from log import Log
from create_hash import decodex
from dbs.patientsdb import PatientsDb
from dbs.userdb import UserDb
from schema_forms.patient_bio_info_form import PatientBioInfoForm
from schema_forms.biopsy_form import BiopsyForm
from schema_forms.mammo_form import MammographyForm, MammoMassRepeaterForm
from wtforms import Form, StringField, PasswordField, validators
from functools import wraps
from schema_forms.models import FolderSection
from dbs.biopsydb import BiopsyDb
from dbs.mammodb import MammoDb
from flask_bootstrap import Bootstrap

# Initialize logging
log = Log()
# Initialize DB
db = PatientsDb(log)
db.connect()

# Initialize User DB
users_db = UserDb(log)
users_db.connect()

# Initialize BiopsyDb
biopsy_db = BiopsyDb(log)
biopsy_db.connect()

#Initialize MammoDb
mammo_db = MammoDb(log)
mammo_db.connect()

app = Flask(__name__)
Bootstrap(app)

#########################################################
# Login, registration and index
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        if users_db.add_user(name, email, username, password):
            flash('You are now registered and can log in', 'success')
        else:
            flash('Error adding user to database', 'error')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        encrypted, name = users_db.get_password(username)
        if encrypted is not None:
            if sha256_crypt.verify(password_candidate, encrypted):
                session['logged_in'] = True
                session['username'] = username
                session['name'] = name
                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
        return name
    return render_template('login.html')


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please log in', 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


#########################################################
# Main dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    patient_list = db.get_patients()
    if patient_list:
        return render_template('dashboard.html', patients = patient_list)
    else:
        msg = 'No data found'
        return render_template('dashboard.html', msg = msg)

#########################################################
# Patient CRUD
@app.route('/add_patient', methods=['GET', 'POST'])
@is_logged_in
def add_patient():
    form = PatientBioInfoForm(request.form)
    if request.method == 'POST' and not form.validate():
        errs = ""
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                errs = errs + err + " "
        flash('Error adding patient: ' + errs, 'danger')

    if request.method == 'POST' and form.validate():
        patient = form.to_model()
        success_flag, error = db.add_patient(patient)
        if not success_flag:
            flash('Error adding patient: ' + str(error), 'danger')
        else:
            flash('Patient Added', 'success')

        return redirect(url_for('dashboard'))
    return render_template('patient_bio_info_add.html', form=form)

@app.route('/edit_patient/<folder_hash>', methods=['GET', 'POST'])
@is_logged_in
def edit_patient(folder_hash):
    form = PatientBioInfoForm(request.form)

    if request.method == 'GET':
        folder_number = decodex(folder_hash)
        patient = db.get_patient(folder_number)
        if patient is not None:
            form.from_model(patient)
        else:
            flash('Patient not found for folder: ' + folder_number, 'danger')

    if request.method == 'POST' and form.validate():
        patient = form.to_model()
        success_flag, error = db.update_patient(patient)

        if not success_flag:
            flash('Error updating patient: ' + str(error), 'danger')
        else:
            flash('Patient Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('patient_bio_info_edit.html', form=form)

@app.route('/delete_patient/<folder_hash>', methods=['POST'])
@is_logged_in
def delete_patient(folder_hash):
    folder_number = decodex(folder_hash)
    success_flag, error = db.delete_patient(folder_number)

    if not success_flag:
        flash('Error deleting patient: ' + str(error), 'danger')
    else:
        flash('Patient Deleted', 'success')

    return redirect(url_for('dashboard'))

######################
# Folder
@app.route('/folder/<folder_hash>', methods=['GET'])
@is_logged_in
def view_folder(folder_hash):
    folder_number = decodex(folder_hash)
    folder_sections = []

    section = create_folder_section(folder_number, "mammo", mammo_db.get_mammography)
    folder_sections.append(section)
    section = create_folder_section(folder_number, "mammo_mass", mammo_db.get_mammography)
    folder_sections.append(section)
    #section = create_folder_section(folder_number, "biopsy", biopsy_db.get_biopsy)
    #folder_sections.append(section)

    return render_template('folder.html', folder_hash=folder_hash, folder_number=folder_number,
                           folder_sections=folder_sections)

def create_folder_section(folder_number, section_name, db_get):
    section_object = db_get(folder_number)
    action = "add"
    status = "To be filled"
    last_modified_on = datetime.datetime.today().strftime('%Y-%m-%d')
    if section_object is not None:
        action = "edit"
        status = section_object.fld_form_status.data
        last_modified_on = section_object.last_update.data
    section = FolderSection(section_name, action, status, last_modified_on = last_modified_on, last_modified_by="Who Knows", )
    return section


######################
# Biopsy CRUD

@app.route('/add_biopsy/<folder_hash>', methods=['GET','POST'])
@is_logged_in
def add_biopsy(folder_hash):
    form = BiopsyForm(request.form)
    folder_number = decodex(folder_hash)
    form.folder_number.data = folder_number

    if request.method == 'POST' and not form.validate():
        errs = ""
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                errs = errs + err + " "
        flash('Error adding biopsy: ' + errs, 'danger')

    if request.method == 'POST' and form.validate():
        biopsy = form.to_model()
        success_flag, error = biopsy_db.add_biopsy(biopsy)
        if not success_flag:
            flash('Error adding patient: ' + str(error), 'danger')
        else:
            flash('Biopsy Information Added', 'success')

        return redirect(url_for('view_folder', folder_hash=folder_hash))
    return render_template('biopsy_add.html', form=form)

@app.route('/edit_biopsy/<folder_hash>', methods=['GET', 'POST'])
@is_logged_in
def edit_biopsy(folder_hash):
    form = BiopsyForm(request.form)
    folder_number = decodex(folder_hash)
    form.folder_number.data = folder_number

    if request.method == 'GET':
        biopsy = biopsy_db.get_biopsy(folder_number)
        if biopsy is not None:
            form.from_model(biopsy)
        else:
            flash('Biopsy not found for folder: ' + folder_number, 'danger')

    if request.method == 'POST' and form.validate():
        biopsy = form.to_model()
        success_flag, error = biopsy_db.update_biopsy(biopsy)

        if not success_flag:
            flash('Error updating biopsy: ' + str(error), 'danger')
        else:
            flash('Biopsy Updated', 'success')

        return redirect(url_for('view_folder', folder_hash=folder_hash))

    return render_template('biopsy_edit.html', form=form)


@app.route('/delete_biopsy/<folder_hash>', methods=['POST'])
@is_logged_in
def delete_biopsy(folder_hash):
    folder_number = decodex(folder_hash)
    success_flag, error = biopsy_db.delete_biopsy(folder_number)

    if not success_flag:
        flash('Error deleting biopsy: ' + str(error), 'danger')
    else:
        flash('Biopsy Deleted', 'success')

    return redirect(url_for('view_folder', folder_hash=folder_hash))


######################
# Mammo CRUD

@app.route('/add_mammo/<folder_hash>', methods=['GET', 'POST'])
@is_logged_in
def add_mammo(folder_hash):
    form = MammographyForm(request.form)
    folder_number = decodex(folder_hash)
    form.fld_folder_number.data = folder_number

    if request.method == 'POST' and not form.validate():
        flash('Please fix validation errors: ' + str(form.errors), 'danger')
    
    if request.method == 'POST' and form.validate():
        print("what the hell")
        success_flag, error = mammo_db.add_mammography(form)
        if not success_flag:
            flash('Error adding mammograph: ' + str(error), 'danger')
        else:
            flash('Patient Added', 'success')

        return redirect(url_for('view_folder', folder_hash=folder_hash))
    return render_template('mammo_form.html', form=form)

@app.route('/edit_mammo/<folder_hash>', methods=['GET', 'POST'])
@is_logged_in
def edit_mammo(folder_hash):
    form = MammographyForm(request.form)
    folder_number = decodex(folder_hash)
    form.fld_folder_number.data = folder_number

    if request.method == 'GET':
        form = mammo_db.get_mammography(folder_number)
        if form is None:
            flash('Mammograph not found for folder: ' + folder_number, 'danger')

    if request.method == 'POST' and form.validate():
        success_flag, error = mammo_db.update_mammography(form)

        if not success_flag:
            flash('Error updating mammograph: ' + str(error), 'danger')
        else:
            flash('Mammograph Updated', 'success')

        return redirect(url_for('view_folder', folder_hash=folder_hash))

    return render_template('mammo_form.html', form=form)

@app.route('/edit_mammo_mass/<folder_hash>', methods=['GET', 'POST'])
@is_logged_in
def edit_mammo_mass(folder_hash):
    form = MammoMassRepeaterForm(request.form)
    folder_number = decodex(folder_hash)
    form.fld_folder_number.data = folder_number

    # if request.method == 'GET':
    #     form = mammo_db.get_mammography(folder_number)
    #     if form is None:
    #         flash('Mammograph not found for folder: ' + folder_number, 'danger')

    if request.method == 'POST' and form.validate():
        success_flag, error = mammo_db.update_mammography(form)

        if not success_flag:
            flash('Error updating mammograph: ' + str(error), 'danger')
        else:
            flash('Mammograph Updated', 'success')

        return redirect(url_for('view_folder', folder_hash=folder_hash))

    return render_template('mammo_repeater.html', form=form)

@app.route('/delete_mammo/<folder_hash>', methods=['POST'])
@is_logged_in
def delete_mammo(folder_hash):
    folder_number = decodex(folder_hash)
    success_flag, error = mammo_db.delete_mammography(folder_number)

    if not success_flag:
        flash('Error deleting mammograph: ' + str(error), 'danger')
    else:
        flash('Mammograph Deleted', 'success')

    return redirect(url_for('view_folder', folder_hash=folder_hash))

#########################################################
# foo CRUD - should come here
# TODO: implement here...

#########################################################
# MAIN

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0', port=5666, debug=True)