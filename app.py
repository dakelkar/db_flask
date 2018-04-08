from flask import Flask, render_template, flash, redirect, url_for, session, request
from passlib.hash import sha256_crypt
from log import Log
from create_url import decodex
from dbs.patientsdb import PatientsDb
from schema_forms.patient_bio_info_form import Patient_bio_info_Form
from wtforms import Form, StringField, PasswordField, validators
from functools import wraps



# Initialize logging
log = Log()

# Initialize DB
db = PatientsDb(log)
db.connect()

app = Flask(__name__)


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

        if db.add_user(name, email, username, password):
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

        encrypted, name = db.get_password(username)
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
        return render_template('dashboard.html', patients=patient_list)
    else:
        msg = 'No patients found'
        return render_template('dashboard.html', msg=msg)


#########################################################
# Patient CRUD
@app.route('/add_patient', methods=['GET', 'POST'])
@is_logged_in
def add_patient():
    form = Patient_bio_info_Form(request.form)
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
   # return render_template(dk, form=form)

@app.route('/edit_patient/<folder_hash>', methods=['GET', 'POST'])
@is_logged_in
def edit_patient(folder_hash):
    form = Patient_bio_info_Form(request.form)

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

#########################################################
# foo CRUD - should come here
# TODO: implement here...

#########################################################
# MAIN

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0', port=5666, debug=True)
