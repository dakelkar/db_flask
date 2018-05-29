import datetime
from flask import Flask, render_template, flash, redirect, url_for, session, request, abort
from passlib.hash import sha256_crypt
from log import Log
from create_hash import decodex, encodex
from dbs.patientsdb import PatientsDb
from dbs.userdb import UserDb
from schema_forms.patient_bio_info_form import PatientBioInfoForm
from schema_forms.biopsy_form import BiopsyForm
from schema_forms.mammo_form import MammographyForm, MammoMassForm, MammoCalcificationForm
from schema_forms.patient_history import PatientHistoryForm
from wtforms import Form, StringField, PasswordField, validators
from functools import wraps
from schema_forms.models import FolderSection
from flask_bootstrap import Bootstrap
from isloggedin import is_logged_in
from crudprint import construct_crudprint
from dbs.sectiondb import SectionDb

# Initialize logging
log = Log()
# Initialize DB
db = PatientsDb(log)
db.connect()

# Initialize User DB
users_db = UserDb(log)
users_db.connect()

#Initialize section DBs
app = Flask(__name__)
Bootstrap(app)

mammo_db = SectionDb(log, MammographyForm, 'mammographies')
mammo_db.connect()
mammo_crudprint = construct_crudprint('mammo', mammo_db)
app.register_blueprint(mammo_crudprint, url_prefix="/mammo")

mammo_mass_db = SectionDb(log, MammoMassForm, 'mammo_mass')
mammo_mass_db.connect()
mammo_mass_crudprint = construct_crudprint('mammo_mass', mammo_mass_db)
app.register_blueprint(mammo_mass_crudprint, url_prefix="/mammo_mass")

mammo_calcification_db = SectionDb(log, MammoCalcificationForm, 'mammo_calcification')
mammo_calcification_db.connect()
mammo_calcification_crudprint = construct_crudprint('mammo_calcification', mammo_calcification_db)
app.register_blueprint(mammo_calcification_crudprint, url_prefix="/mammo_calcification")

biopsy_db = SectionDb(log, BiopsyForm, 'biopsies')
biopsy_db.connect()
biopsy_crudprint = construct_crudprint('biopsy', biopsy_db)
app.register_blueprint(biopsy_crudprint, url_prefix="/biopsy")

patient_history_db = SectionDb(log, PatientHistoryForm, 'patient_history')
patient_history_db.connect()
patient_history_crudprint = construct_crudprint('patient_history', patient_history_db)
app.register_blueprint(patient_history_crudprint, url_prefix="/patient_history")


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

@app.route('/search', methods=['POST'])
@is_logged_in
def search_folder():
    folder_number = request.form['query']
    patient = db.get_patient(folder_number)
    if patient is None:
        abort(404)
    folder_hash = encodex(folder_number) 
    return redirect(url_for('view_folder', folder_hash=folder_hash))
 
######################
# Folder
@app.route('/folder/<folder_hash>', methods=['GET'])
@is_logged_in
def view_folder(folder_hash):
    # currently only works for Radiology sections!
    active_tab_id = request.args.get('active_tab')
    if active_tab_id is None:
        if 'active_tab' in session:
            active_tab_id = session['active_tab']
    if active_tab_id is None:        
        active_tab_id = "PatientHistory"
    session['active_tab'] = active_tab_id

    folder_sections = []
    if active_tab_id == "Radiology":
        folder_sections = [
            create_folder_section(folder_hash, "mammo", "mammo", mammo_db.get_folder_items),
            create_folder_section(folder_hash, "mammo_mass", "mammo_mass", mammo_mass_db.get_folder_items, is_list=True),
            create_folder_section(folder_hash, "mammo_calcification", "mammo_calcification", mammo_calcification_db.get_folder_items, is_list=True),
        ]
    elif active_tab_id == "Biopsy":
        folder_sections = [
            create_folder_section(folder_hash, "biopsy", "biopsy", biopsy_db.get_folder_items),
        ]        
    elif active_tab_id == "PatientHistory":
        folder_sections = [
            create_folder_section(folder_hash, "patient_history", "patient_history", patient_history_db.get_folder_items),
        ]        
                

    folder_tabs = [        
        ("PatientHistory", "Patient History"),
        ("ClinicalExam", "Clinical Exam"),
        ("Radiology", "Radiology"),
        ("Biopsy", "Biopsy"),
        ("NACT", "NeoAdjuvant Chemotherapy"),
        ("SurgeryBlock", "Surgery Block"),
        ("Surgery", "Surgery"),
        ("AdjuvantChemo", "Adjuvant Chemotherapy"),
        ("Radiotherapy", "Radiotherapy"),
        ("LongTermTherapy", "LongTerm Therapy"),
        ("FollowUp", "Follow-up"),
    ]

    folder_number = decodex(folder_hash)
    return render_template('folder_tabs.html', folder_number=folder_number, folder_sections=folder_sections, 
                            folder_tabs=folder_tabs, active_tab_id=active_tab_id)

def create_folder_section(folder_hash, id, section_name, db_get, is_list=False):
    folder_number = decodex(folder_hash)
    forms = db_get(folder_number)
    action = "add"
    status = ["To be filled"]
    last_modified_on = [datetime.datetime.today().strftime('%Y-%m-%d')]
    update_by = [""]
    pks = None
    if forms is not None and len(forms) >0:
        action = "edit"
        status = [x.fld_form_status.data for x in forms]
        last_modified_on = [x.last_update.data for x in forms]
        pks = [(x.fld_pk.data, x.get_summary()) for x in forms]
        update_by = [x.update_by.data for x in forms]

    section = FolderSection(id, section_name, action, status, forms, folder_hash, last_modified_on = last_modified_on, 
                            last_modified_by=update_by, pks=pks, is_list=is_list)
    return section



# MAIN
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0', port=5666, debug=True)