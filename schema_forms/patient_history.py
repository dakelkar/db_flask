from wtforms import StringField, validators, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField
from schema_forms.form_utilities import SectionForm
from db_dict.patient_history_dict import PatientHistoryDict
from db_dict.common_dict import CommonDict

class PatientHistoryForm(SectionForm):
    fld_age_diagnosis = IntegerField('Age at diagnosis (yrs)', [validators.required()])
    fld_place_birth = StringField('Place of Birth')
    fld_height_cm = FloatField('Height (in cm)', [validators.required()])
    fld_weight_kg = FloatField('Weight (in kg)', [validators.required()])
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice)
    fld_diet_other = StringField("Other")
    fld_alcohol = SelectField("Alcohol consumption", choices=CommonDict.yes_no_choice)
    fld_alcohol_other = StringField("Other")
    fld_alcohol_age = StringField("Consumption of alcohol from which age (yrs)")
    fld_alcohol_quant = StringField("Quantity of alcohol consumed per week")
    fld_alcohol_duration = StringField("Duration of alcohol consumption")
    fld_alcohol_comments = StringField("Additional comments for alcohol consumption")
    fld_tobacco = SelectField("Tobacco exposure (Passive and/or Active)", choices=PatientHistoryDict.tobacco_choice)
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
    fld_other_del_habits = StringField("Other Deleterious Habits (if present give details)")
    submit_button = SubmitField('Submit Form')

class PhysicalActivityForm(SectionForm):
    def get_summary(self):
        return "Physical activity" + str(self.fld_type_phys_act.data)
    fld_type_phys_act = StringField("Type of physical activity")
    fld_freq_phys_act = StringField("Frequency of physical activity")
    submit_button = SubmitField('Submit Form')

class NutritionalSupplementsForm(SectionForm):
    def get_summary(self):
        return "Nutritional Supplements" + str(self.fld_nut_supplements_type.data)
    fld_nut_supplements_type = StringField("Type of nutritional supplements taken")
    fld_nut_supplements_quant = StringField("Quantity of nutritional supplements taken per day")
    fld_nut_supplements_duration = StringField("Duration of nutritional supplements use")
    submit_button = SubmitField('Submit Form')