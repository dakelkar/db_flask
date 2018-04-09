from wtforms import Form, StringField, TextAreaField, validators, IntegerField, SelectField, FloatField, RadioField
from wtforms.fields.html5 import DateField
from schema_forms.models import Patient_bio_info_Info
from db_dict.patient_form import PatientDict

class PatientBioInfoForm(Form):
    folder_number = StringField('Folder Number', [validators.required()])
    mr_number = StringField('MR number', [validators.Length(min=1, max=50)])
    name = StringField('Name', [validators.Length(min=1, max=50)])
    aadhaar_card = StringField('Aadhaar Card Number (if available)')
    date_first = DateField("Date of first visit")
    permanent_address = TextAreaField('Permanent Address', [validators.Length(min=1, max=200)])
    current_address = TextAreaField('Current Address', [validators.Length(min=1, max=200)])
    phone = IntegerField('Phone')
    email_id = StringField('Email ID', [validators.optional()])
    gender = RadioField('Gender', choices= PatientDict.gender_choice)
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


