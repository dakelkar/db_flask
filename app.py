from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, SelectField, FloatField
from wtforms.fields.html5 import DateField
from passlib.hash import sha256_crypt
from log import Log
from functools import wraps
from patientsdb import  PatientsDb

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


@app.route('/dashboard')
@is_logged_in
def dashboard():
    patient_list = db.get_patients()
    print(patient_list)
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


@app.route('/add_patient', methods=['GET', 'POST'])
@is_logged_in
def add_patient():
    form = PatientForm(request.form)
    if request.method == 'POST' and form.validate():
        folder_number = form.folder_number.data
        mr_number = form.mr_number.data
        name = form.name.data
        aadhaar_card = form.aadhaar_card.data
        date_first = form.date_first.data
        permanent_address = form.permanent_address.data
        current_address = form.current_address.data
        phone = form.phone.data
        email_id = form.email_id.data
        gender = form.gender.data
        age_yrs = form.age_yrs.data
        date_of_birth = form.date_of_birth.data
        place_birth = form.place_birth.data
        height_cm = form.height_cm.data
        weight_kg = form.weight_kg.data

        success_flag, error = db.add_patient(folder_number, mr_number, name, aadhaar_card, date_first, permanent_address,
                               current_address, phone, email_id,gender, age_yrs, date_of_birth, place_birth, height_cm, weight_kg)
        if not success_flag:
            flash('Error adding patient: ' + str(error), 'danger')
        else:
            flash('Patient Added', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_patient.html', form=form)


#EDIT EVENT FOR SP NAME
@app.route('/edit_patient/<string:folder_number>', methods=['GET', 'POST'])
@is_logged_in
def edit_patient(folder_number):
    patient = db.get_patient(folder_number)
    if patient:
        form = PatientForm(request.form)
        form.folder_number.data = patient['File_number']
        form.mr_number.data = patient['MR_number']
        form.name.data = patient['Name']
        form.aadhaar_card.data = patient['Aadhaar_Card']
        form.date_first.data = patient['FirstVisit_Date'].date()
        form.permanent_address.data = patient['Permanent_Address']
        form.current_address.data = patient['current_address']
        form.phone.data = patient['phone']
        form.email_id.data = patient['email_id']
        form.gender.data = patient['gender']
        form.age_yrs.data = patient['age_yrs']
        form.date_of_birth.data = patient['date_of_birth']
        form.place_birth.data = patient['place_birth']
        form.height_cm.data = patient['height_cm']
        form.weight_kg.data = patient['weight_kg']

        if request.method == 'POST' and form.validate():
            mr_number = form.mr_number.data
            name = form.name.data
            aadhaar_card = form.aadhaar_card.data
            date_first = form.date_first.data
            permanent_address = form.permanent_address.data
            current_address = form.current_address.data
            phone = form.phone.data
            email_id = form.email_id.data
            gender = form.gender.data
            age_yrs = form.age_yrs.data
            date_of_birth = form.date_of_birth.data
            place_birth = form.place_birth.data
            height_cm = form.height_cm.data
            weight_kg = form.weight_kg.data

            success_flag, error = db.update_patient(folder_number, mr_number, name, aadhaar_card, date_first,
                                                    permanent_address, current_address, phone, email_id,gender, age_yrs,
                                                    date_of_birth, place_birth, height_cm, weight_kg)

            if not success_flag:
                flash('Error updating patient: ' + str(error), 'danger')
            else:
                flash('Patient Updated', 'success')

            return redirect(url_for('dashboard'))

    return render_template('edit_patient.html', form=form)


@app.route('/delete_patient/<string:folder_number>', methods=['POST'])
@is_logged_in
def delete_patient(folder_number):
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
