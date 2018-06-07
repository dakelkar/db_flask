from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField
from schema_forms.form_utilities import SectionForm, BaseForm, FormField
from db_dict.patient_details_dict import PatientHistoryDict
from db_dict.common_dict import CommonDict

class AlcoholConsumptionForm(BaseForm):
    fld_alcohol_age = StringField("Consumption of alcohol from which age (yrs)")
    fld_alcohol_quant = StringField("Quantity of alcohol consumed per week")
    fld_alcohol_duration = StringField("Duration of alcohol consumption")
    fld_alcohol_comments = StringField("Additional comments for alcohol consumption")

class TobaccoConsumption (BaseForm):
    fld_tobacco_exposure = SelectField("Type of tobacco consumption", choices=PatientHistoryDict.tobacco_choice)
    fld_tobacco_type_passive = SelectField("Mode of passive consumption",
                                           choices=PatientHistoryDict.tobacco_type_passive_choice)
    fld_tobacco_type_passive_other = StringField('Other')
    fld_tobacco_type_passive_home = StringField("What is the specific source of passive exposure at home",
                                                default='None')
    fld_tobacco_type = SelectMultipleField("Type of tobacco use", choices=PatientHistoryDict.tobacco_type_choice)
    fld_tobacco_type_other = StringField("Other")
    fld_tobacco_age = StringField("Consumption of tobacco from which age (yrs)")
    fld_tobacco_freq = StringField("Frequency of tobacco consumption")
    fld_tobacco_quant = StringField("Quantity of tobacco consumed per week")
    fld_tobacco_duration = StringField("Duration of tobacco consumption")
    fld_tobacco_comments = StringField("Additional comments for tobacco consumption")
