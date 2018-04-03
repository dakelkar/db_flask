from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, SelectField, FloatField
from wtforms.fields.html5 import DateField
from passlib.hash import sha256_crypt
from log import Log
from functools import wraps
from patientsdb import  PatientsDb
from create_url import decodex, encodex
from base64 import urlsafe_b64decode

import models

# Initialize logging
log = Log()
# Initialize DB
db = PatientsDb(log)
db.connect()

app = Flask(__name__)


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
        name=form.name.data
        email=form.email.data
        username=form.username.data
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


@app.route('/dashboard')
@is_logged_in
def dashboard():
    patient_list = db.get_patients()
    if patient_list:
        return render_template('dashboard.html', patients=patient_list)
    else:
        msg = 'No patients found'
        return render_template('dashboard.html', msg=msg)


class PatientForm(Form):
    folder_number = StringField('Folder Number', [validators.required()])
    mr_number = StringField('MR number', [validators.Length(min=1, max=50)])
    name = StringField('Name', [validators.Length(min=1, max=50)])
    aadhaar_card = StringField('Aadhaar Card Number (if available)')
    date_first = DateField("Date of first visit")
    permanent_address = TextAreaField('Permanent Address', [validators.Length(min=1, max=200)])
    current_address = TextAreaField('Current Address', [validators.Length(min=1, max=200)])
    phone = IntegerField ('Phone')
    email_id = StringField('Email ID', [validators.optional()])
    gender = SelectField('Gender', choices=[('F', 'Female'), ('M', 'Male')])
    age_yrs = IntegerField('Age in years', [validators.required()])
    date_of_birth = DateField('Date of Birth',[validators.required()])
    place_birth = StringField('Place of Birth')
    height_cm = FloatField('Height (in cm)', [validators.required()])
    weight_kg = FloatField('Weight (in kg)', [validators.required()])

    def to_model(self):
        patient = models.PatientInfo(folder_number= self.folder_number.data,
            mr_number=self.mr_number.data,
            name=self.name.data,
            aadhaar_card=self.aadhaar_card.data,
            date_first=self.date_first.data,
            permanent_address=self.permanent_address.data,
            current_address=self.current_address.data,
            phone=self.phone.data,
            email_id=self.email_id.data,
            gender=self.gender.data,
            age_yrs=self.age_yrs.data,
            date_of_birth=self.date_of_birth.data,
            place_birth=self.place_birth.data,
            height_cm=self.height_cm.data,
            weight_kg=self.weight_kg.data)
        return patient

    def from_model(self, patient):
        """
        :param models.PatientForm patient: initialize form based on the model
        """
        self.folder_number.data = patient.folder_number      
        self.mr_number.data = patient.mr_number
        self.name.data = patient.name        
        self.aadhaar_card.data = patient.aadhaar_card
        self.date_first.data = patient.date_first        
        self.permanent_address.data = patient.permanent_address
        self.current_address.data = patient.current_address        
        self.phone.data = patient.phone
        self.email_id.data = patient.email_id        
        self.gender.data = patient.gender
        self.age_yrs.data = patient.age_yrs        
        self.date_of_birth.data = patient.date_of_birth
        self.place_birth.data = patient.place_birth        
        self.height_cm.data = patient.height_cm
        self.weight_kg.data = patient.weight_kg


@app.route('/add_patient', methods=['GET', 'POST'])
@is_logged_in
def add_patient():
    form = PatientForm(request.form)
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

    return render_template('add_patient.html', form=form)



#EDIT EVENT FOR SP NAME
@app.route('/edit_patient/<folder_url>', methods=['GET', 'POST'])
@is_logged_in
def edit_patient(folder_url):
    form = PatientForm(request.form)

    if request.method == 'GET':
        folder_number = decodex(folder_url)
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

    return render_template('edit_patient.html', form=form)


@app.route('/delete_patient/<folder_url>', methods=['POST'])
@is_logged_in
def delete_patient(folder_url):
    folder_number = request.args.get('folder_url')

    success_flag, error = db.delete_patient(folder_number)

    if not success_flag:
        flash('Error deleting patient: ' + str(error), 'danger')
    else:
        flash('Patient Deleted', 'success')

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0', port=5666, debug=True)
