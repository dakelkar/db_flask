import datetime
from flask import Flask, render_template, flash, redirect, url_for, session, request
from passlib.hash import sha256_crypt
from log import Log
from dbs.foldersdb import FoldersDb
from dbs.userdb import UserDb
from schema_forms.patient_details.patient_history import PatientInformationHabitsForm, PhysicalActivityForm, \
    NutritionalSupplementsForm, FamilyReproductiveDetails, PatientMedicalHistory, PatientCancerHistory, \
    FamilyCancerHistory
from schema_forms.biopsy_form import BiopsyForm
from schema_forms.radiology.mammo_form import MammographyForm, MammoMassForm, MammoCalcificationForm
from schema_forms.radiology.usg import SonoMammographyForm, SonoMammoMassForm
from schema_forms.radiology.mri import MRIForm, MRIMassForm
from schema_forms.folder_form import FoldersForm
from wtforms import Form, StringField, PasswordField, validators
from schema_forms.models import FolderSection
from flask_bootstrap import Bootstrap
from isloggedin import is_logged_in
from crudprint import construct_crudprint
from crudprint_folder import construct_crudprint_folder
from dbs.sectiondb import SectionDb
import os

# Initialize logging
log = Log()
# Initialize DB
#url = os.getenv('BCDB_URL')
url = None
if url is None:
    url = 'mongodb://localhost:27017'
url = url.replace('"', '')
print('Using db at: '+url)

#port = os.getenv('PORT')
port = None
if port is None:
    port = 5666

db = FoldersDb(log, FoldersForm)
db.connect(url)

# Initialize User DB
users_db = UserDb(log)
users_db.connect(url)

#Initialize section DBs
app = Flask(__name__)
Bootstrap(app)

folder_db = FoldersDb(log, FoldersForm)
folder_db.connect(url)
folder_crudprint = construct_crudprint_folder(folder_db)
app.register_blueprint(folder_crudprint, url_prefix="/folder")

#Patient CRUD

patient_history_db = SectionDb(log, PatientInformationHabitsForm,'patient_history')
patient_history_db.connect(url)
patient_history_crudprint = construct_crudprint('patient_history', patient_history_db, folder_db)
app.register_blueprint(patient_history_crudprint, url_prefix="/patient_history")

patient_history_phys_act_db = SectionDb(log, PhysicalActivityForm, 'physical_activity')
patient_history_phys_act_db.connect(url)
patient_history_phys_act_crudprint = construct_crudprint('physical_activity', patient_history_phys_act_db, folder_db)
app.register_blueprint(patient_history_phys_act_crudprint, url_prefix="/physical_activity")

patient_history_nut_supp_db = SectionDb(log, NutritionalSupplementsForm, 'nutritional_supplements')
patient_history_nut_supp_db.connect(url)
patient_history_nut_supp_crudprint = construct_crudprint('nutritional_supplements', patient_history_nut_supp_db, folder_db)
app.register_blueprint(patient_history_nut_supp_crudprint, url_prefix="/nutritional_supplements")

family_details_db = SectionDb(log, FamilyReproductiveDetails, 'family_details')
family_details_db.connect(url)
family_details_crudprint = construct_crudprint('family_details', family_details_db, folder_db)
app.register_blueprint(family_details_crudprint, url_prefix="/family_details")

patient_medical_db = SectionDb(log, PatientMedicalHistory, 'patient_medical')
patient_medical_db.connect(url)
patient_medical_crudprint = construct_crudprint('patient_medical', patient_medical_db, folder_db)
app.register_blueprint(patient_medical_crudprint, url_prefix="/patient_medical")

patient_former_cancer_db = SectionDb(log, PatientCancerHistory, 'patient_former_cancer')
patient_former_cancer_db.connect(url)
patient_former_cancer_crudprint = construct_crudprint('patient_former_cancer', patient_former_cancer_db, folder_db)
app.register_blueprint(patient_former_cancer_crudprint, url_prefix="/patient_former_cancer")

family_cancer_db = SectionDb(log, FamilyCancerHistory, 'family_cancer')
family_cancer_db.connect(url)
family_cancer_crudprint = construct_crudprint('family_cancer', family_cancer_db, folder_db)
app.register_blueprint(family_cancer_crudprint, url_prefix="/family_cancer")

#Radiology CRUD

mammo_db = SectionDb(log, MammographyForm, 'mammography')
mammo_db.connect(url)
mammo_crudprint = construct_crudprint('mammography', mammo_db, folder_db)
app.register_blueprint(mammo_crudprint, url_prefix="/mammo")

mammo_mass_db = SectionDb(log, MammoMassForm, 'mammo_mass')
mammo_mass_db.connect(url)
mammo_mass_crudprint = construct_crudprint('mammography_mass', mammo_mass_db, folder_db)
app.register_blueprint(mammo_mass_crudprint, url_prefix="/mammo_mass")

mammo_calcification_db = SectionDb(log, MammoCalcificationForm, 'mammo_calcification')
mammo_calcification_db.connect(url)
mammo_calcification_crudprint = construct_crudprint('mammo_calcification', mammo_calcification_db, folder_db)
app.register_blueprint(mammo_calcification_crudprint, url_prefix="/mammo_calcification")

usg_db = SectionDb(log, SonoMammographyForm, 'sono_mammography')
usg_db.connect(url)
usg_crudprint = construct_crudprint('sonomammography', usg_db, folder_db)
app.register_blueprint(usg_crudprint, url_prefix="/usg")

usg_mass_db = SectionDb(log, SonoMammoMassForm, 'sonomammography_mass')
usg_mass_db.connect(url)
usg_mass_crudprint = construct_crudprint('sonomammography_mass', usg_mass_db, folder_db)
app.register_blueprint(usg_mass_crudprint, url_prefix="/usg_mass")

mri_db = SectionDb(log, MRIForm, 'mri')
mri_db.connect(url)
mri_crudprint = construct_crudprint('mri', mri_db, folder_db)
app.register_blueprint(mri_crudprint, url_prefix="/mri")

mri_mass_db = SectionDb(log, MRIMassForm, 'mri_mass')
mri_mass_db.connect(url)
mri_mass_crudprint = construct_crudprint('mri_mass', mri_mass_db, folder_db)
app.register_blueprint(mri_mass_crudprint, url_prefix="/mri_mass")

biopsy_db = SectionDb(log, BiopsyForm, 'biopsies')
biopsy_db.connect(url)
biopsy_crudprint = construct_crudprint('biopsy', biopsy_db, folder_db)
app.register_blueprint(biopsy_crudprint, url_prefix="/biopsy")

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
    folder_list = db.get_folders()
    if folder_list:
        return render_template('dashboard.html', folders = folder_list)
    else:
        msg = 'No data found'
        return render_template('dashboard.html', msg = msg)

#########################################################
    # Folder CRUD

 
######################
# Folder
@app.route('/search', methods=['POST'])
@is_logged_in
def search_folder():
    folder_number = request.form['query']
    folder = folder_db.get_folder_by_number(folder_number, is_delete=False)
    if folder is None:
        flash(folder_number + ' not found', 'danger')
        return redirect(url_for('dashboard'))
    return redirect(url_for('view_folder', folder_pk=folder.fld_folder_pk.data))


@app.route('/folder/<folder_pk>', methods=['GET'])
@is_logged_in
def view_folder(folder_pk):
    folder_number = folder_db.folder_check(folder_pk)

    if folder_number is None:
        flash(folder_pk + ' not found', 'danger')
        return redirect(url_for('dashboard'))

# select active tab
    active_tab_id = request.args.get('active_tab')
    if active_tab_id is None:
        if 'active_tab' in session:
            active_tab_id = session['active_tab']
    if active_tab_id is None:
        active_tab_id = "PatientHistory"
    session['active_tab'] = active_tab_id

    # set up sections
    folder_sections = []
    if active_tab_id == "PatientHistory":
        folder_sections = [
            create_folder_section(folder_pk, "patient_history", "Patient Information and Habits",
                                  patient_history_db.get_folder_items),
            create_folder_section(folder_pk, "physical_activity", "Physical Activity Habits",
                                  patient_history_phys_act_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "nutritional_supplements", "Nutritional Supplements Intake",
                                  patient_history_nut_supp_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "family_details", "Patient Family and Reproductive Details",
                                  family_details_db.get_folder_items),
            create_folder_section(folder_pk, "patient_medical", "Patient Medical History",
                                  patient_medical_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "patient_former_cancer", "Patient Cancer History",
                                  patient_former_cancer_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "family_cancer", "Patient Family Cancer History",
                                  family_cancer_db.get_folder_items, is_list=True),
            ]
    elif active_tab_id == "Radiology":
        folder_sections = [
            create_folder_section(folder_pk, "mammo","Mammography", mammo_db.get_folder_items),
            create_folder_section(folder_pk,  "mammo_mass","Mammography Mass/Lesion", mammo_mass_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "mammo_calcification", "Mammography Calcification",
                                  mammo_calcification_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "usg", "USG", usg_db.get_folder_items),
            create_folder_section(folder_pk,  "usg_mass","USG Mass/Lesion", usg_mass_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "mri", "MRI", mri_db.get_folder_items),
            create_folder_section(folder_pk,  "mri_mass","MRI Mass/Lesion", mri_mass_db.get_folder_items, is_list=True),
        ]
    elif active_tab_id == "Biopsy":
        folder_sections = [
            create_folder_section(folder_pk, "biopsy", "Biopsy Report", biopsy_db.get_folder_items),
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

    key = folder_pk
    return render_template('folder_tabs.html', folder_number = folder_number, key = folder_pk, folder_sections=folder_sections,
                            folder_tabs=folder_tabs, active_tab_id=active_tab_id)

def create_folder_section(folder_pk, id, section_name, db_get, is_list=False):
    forms = db_get(folder_pk)
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

    section = FolderSection(id, section_name, action, status, forms, folder_pk, last_modified_on = last_modified_on,
                            last_modified_by=update_by, pks=pks, is_list=is_list)
    return section



# MAIN
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0', port=port, debug=True)