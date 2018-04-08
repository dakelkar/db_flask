from wtforms import Form, StringField, TextAreaField, validators, IntegerField, SelectField, FloatField, RadioField
from wtforms.fields.html5 import DateField
from schema_forms.models import Patient_bio_info_Info
from db_dict.biopsy import Biopsy_dict

class biopsy_Form(Form):

    folder_number = StringField('Folder Number', [validators.required()])
    consent_stat = RadioField('Has consent been taken from patient?', choices=((1, "Consent Taken"), (0, "No Consent")))
    consent_form = RadioField('Is consent form with signature present in file ?',
                              choices=((1, "Consent form with signature present in folder"),
                                       (0, "Completed consent form not present in folder")))
    block_serial_number = StringField('Block Serial Number', [validators.Length(min=1, max=50)])
    block_location = "to try fields here since it has a format"
    block_current_location = StringField ("What is the current location of block?")
    biopsy_custody_pccm = RadioField('Is the biopsy report in PCCM custody?',
                                     choices=((1, "In PCCM Custody"), (0, "Not in PCCM custody")))
    biopsy_block_id = StringField("Biopsy Block ID")
    biopsy_block_number = IntegerField("Number of blocks")
    biopsy_date = DateField("Date of Biopsy")
    biopsy_lab_id = StringField("Biopsy Lab ID")
    biopsy_type = SelectField("Biopsy Type", choices =
    (("direct",Biopsy_dict.biopsy_type.get("direct")), ("usg_guided",Biopsy_dict.biopsy_type.get("usg_guided")),
     ("vab",Biopsy_dict.biopsy_type.get("vab")), ("truecut",Biopsy_dict.biopsy_type.get("truecut")),
     ("stereo",Biopsy_dict.biopsy_type.get("stereo")), ("other",Biopsy_dict.biopsy_type.get("other"))))
    biopsy_tumour_diagnosis = SelectField("Tumour Diagnosis", choices = (('benign','Benign'),
                    ('dcis_with_micro',"Ductal carcinoma in situ(DCIS) with microinvasion"),
                    ('dcis_without_micro',"Ductal carcinoma in situ(DCIS) without microinvasion"),("lcs",
                    "Lobular Carcinoma in Situ (LCS)"),("idc","Invasive Ductal Carcinoma (IDC)"), ('ilc',
                    "Invasive Lobular Carcinoma (ILC)"), ('gm',"Granulamatous Mastitis"),('papc', "Papillary Carcinoma"),
                    ('phyc',"Phylloid Carcinoma"), ('imc', "Invasive Mammary Carcinoma"),('ibc', "Invasive Breast "
                                                                                                 "Carcinoma")))
    biopsy_tumour_grade = SelectField("Tumour Grade", choices = (('1','Grade 1'),('2',"Grade 2"),('3',"Grade 3")))
    biopsy_lymphovascular_emboli = RadioField('Are Lymphovascular emboli seen?',
                                     choices=((1, "Lymphovascular Emboli Seen"), (0, "No Lymphovascular Emboli Seen")))
    aadhaar_card = StringField('Aadhaar Card Number (if available)')
    date_first = DateField("Date of first visit")
    permanent_address = TextAreaField('Permanent Address', [validators.Length(min=1, max=200)])
    current_address = TextAreaField('Current Address', [validators.Length(min=1, max=200)])
    phone = IntegerField('Phone')
    email_id = StringField('Email ID', [validators.optional()])
    gender = SelectField(u'Gender', choices=())
    age_yrs = IntegerField('Age in years', [validators.required()])
    date_of_birth = DateField('Date of Birth', [validators.required()])
    place_birth = StringField('Place of Birth')
    height_cm = FloatField('Height (in cm)', [validators.required()])
    weight_kg = FloatField('Weight (in kg)', [validators.required()])

    def to_model(self):
        """
        :returns Patient_bio_info_Form: model for the form
        """
        patient = Patient_bio_info_Info(folder_number= self.folder_number.data,
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
        :param PatientForm patient: initialize form based on the model
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