from wtforms import StringField, validators, IntegerField, FloatField, SubmitField
from schema_forms.form_utilities import SectionForm


class PatientHistoryForm(SectionForm):
    fld_age_diagnosis = IntegerField('Age at diagnosis (yrs)', [validators.required()])
    fld_place_birth = StringField('Place of Birth')
    fld_height_cm = FloatField('Height (in cm)', [validators.required()])
    fld_weight_kg = FloatField('Weight (in kg)', [validators.required()])
    submit_button = SubmitField('Submit Form')
    