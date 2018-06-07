from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField
from schema_forms.form_utilities import SectionForm, FormField
from db_dict.patient_details_dict import PatientHistoryDict
from db_dict.common_dict import CommonDict
from schema_forms.patient_details.patient_optional_forms import AlcoholConsumptionForm, TobaccoConsumption

tbd = "To be Filled"
class PatientInformationHabitsForm(SectionForm):
    fld_age_diagnosis = IntegerField('Age at diagnosis (yrs)')
    fld_place_birth = StringField('Place of Birth')
    fld_height_cm = FloatField('Height (in cm)')
    fld_weight_kg = FloatField('Weight (in kg)')
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice)
    fld_diet_other = StringField("Other")
    fld_alcohol = SelectField("Alcohol consumption", choices=CommonDict.form_yes_no_choice)
    alcohol = FormField(AlcoholConsumptionForm)
    fld_tobacco = SelectField("Is there any exposure to Tobacco (Passive and/or Active)", choices=CommonDict.form_yes_no_choice)
    tobacco = FormField(TobaccoConsumption)
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

class FamilyReproductiveDetails(SectionForm):
    fld_marital_status = StringField('Marital Status', default=tbd)
    fld_sisters = StringField('Sisters', default=tbd)
    fld_brothers = StringField('Brothers', default=tbd)
    fld_daughters = StringField('Daughters', default=tbd)
    fld_sons = StringField('Sons', default=tbd)
    fld_menarche = StringField('Age at menarche (yrs)', default=tbd)
    fld_menopause = SelectField("Menopausal Status", choices=PatientHistoryDict.menstruation_choice)
    fld_menopause_other = StringField("Other")
    fld_menopause_age = StringField('Age at menopause (yrs)', default=tbd)
    fld_lmp = StringField("Date of last menstrual period", default=tbd)
    fld_period_type = SelectField("Type of Period", choices=PatientHistoryDict.menstruation_type_choice)
    fld_period_type_other = StringField("Other")
    fld_number_pregnancy = StringField("Number of pregnancies", default=tbd)
    fld_number_term = StringField("Pregnancy carried to term (include abortion after 6 months)", default=tbd)
    fld_number_abortion = StringField("Number of abortions", default=tbd)
    fld_age_first_preg = StringField("Age at first pregnancy", default=tbd)
    fld_age_first = StringField("Age of first child", default=tbd)
    fld_age_last = StringField("Age of last child", default=tbd)
    fld_age_last_preg = StringField("Age at last pregnancy", default=tbd)
    fld_twice_birth = SelectField("Two births in a year (not twins)", choices=CommonDict.yes_no_choice)
    fld_breast_feeding = SelectField("Breast feeding?", choices=CommonDict.form_yes_no_choice)
    # insert breast feeding with number of children to number of forms
    fld_type_fert = StringField("Type of fertility treatment used", default=tbd)
    fld_detail_fert = StringField("Details of fertility treatment use", default=tbd)
    fld_cycles_fert = StringField("Number of cycles of fertility treatment taken", default=tbd)
    fld_success_fert = SelectField("Did fertility treatment result in successful pregnancy? ",
                                   choices=CommonDict.yes_no_choice)
    fld_type_birth_control = StringField("Type of birth control used", default=tbd)
    fld_detail_birth_control = StringField("Details of birth control used", default=tbd)
    fld_duration_birth_control = StringField("Duration of birth control use", default=tbd)
    submit_button = SubmitField('Submit Form')