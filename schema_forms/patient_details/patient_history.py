from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField, RadioField
from schema_forms.form_utilities import SectionForm, FormField, BaseForm, FieldList
from db_dict.patient_details_dict import PatientHistoryDict
from db_dict.common_dict import CommonDict
from schema_forms.patient_details.patient_optional_forms import AlcoholConsumptionForm, TobaccoConsumption, \
    BreastSymptomsForm, MetastasisSymptomsForm


tbd = "To be Filled"
class PatientInformationHabitsForm(SectionForm):
    fld_gender = SelectField("Gender", PatientHistoryDict.gender_choice)
    fld_gender_other = StringField("Other")
    fld_age_diagnosis = IntegerField('Age at diagnosis (yrs)', default=tbd)
    fld_place_birth = StringField('Place of Birth', default=tbd)
    fld_height_cm = FloatField('Height (in cm)', default=tbd)
    fld_weight_kg = FloatField('Weight (in kg)', default=tbd)
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice, default=tbd)
    fld_diet_other = StringField("Other")
    fld_occuptation = StringField("Occupation", default=tbd)
    fld_income = SelectField('Annual household income', choices=PatientHistoryDict.family_income_choice)
    fld_alcohol_form_present = SelectField("Alcohol consumption", choices=CommonDict.form_yes_no_choice)
    alcohol_form = FormField(AlcoholConsumptionForm)
    fld_tobacco_form_present = SelectField("Is there any exposure to Tobacco (Passive and/or Active)",
                                           choices=CommonDict.form_yes_no_choice)
    tobacco_form = FormField(TobaccoConsumption)
    fld_other_del_habits = SelectField("Other Deleterious Habits (if present give details)",
                                       choices=PatientHistoryDict.del_habits_choice)
    fld_other_del_habits_other = StringField("Details")
    fld_symptoms_form_present = SelectField("Has the patient come with particular breast symptoms?",
                                            choices=CommonDict.form_yes_no_choice)
    symptoms_form = FormField(BreastSymptomsForm)
    fld_metastasis_form_present = SelectField("Are metastatic symptoms present?", choices=CommonDict.form_yes_no_choice)
    metastasis_form = FormField(MetastasisSymptomsForm)
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
    fld_breast_feeding = SelectField("Breast feeding?", choices=CommonDict.yes_no_choice)
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

class PatientMedicalHistory(SectionForm):
    def get_summary(self):
        return "Medical Condition" + str(self.fld_medical_condition.data)
    fld_medical_condition = StringField("Medical Condition")
    fld_diagnosis_date = StringField("Approximate time since diagnosis - days/months or years (please specify)")
    fld_treatment = StringField("Treatment taken for condition")
    submit_button = SubmitField('Submit Form')

class CancerTreatmentForm(BaseForm):
    fld_cancer_treatment_surgery_form_present = SelectField("Surgery treatment taken",
                                                              choices=CommonDict.form_yes_no_choice, default= tbd)

    fld_type_treat_surgery = StringField("Details of treatment taken", default=tbd)
    fld_cancer_treatment_radiation_form_present = SelectField("Radiation treatment taken",
                                                              choices=CommonDict.form_yes_no_choice, default=tbd)

    fld_type_treat_radiation = StringField("Details of treatment taken", default=tbd)
    fld_duration_treat_radiation = StringField("Duration of treatment", default=tbd)
    fld_cancer_treatment_chemotherapy_form_present = SelectField("Chemotherapy treatment taken",
                                                                 choices=CommonDict.form_yes_no_choice, default=tbd)
    fld_type_treat_chemo = StringField("Details of treatment taken", default=tbd)
    fld_duration_treat_chemo = StringField("Duration of treatment", default=tbd)
    fld_cancer_treatment_hormone_form_present = SelectField("Hormone treatment taken",
                                                            choices=CommonDict.form_yes_no_choice, default=tbd)
    fld_type_treat_hormone = StringField("Details of treatment taken", default=tbd)
    fld_duration_treat_hormone = StringField("Duration of treatment", default=tbd)
    fld_cancer_treatment_alt_form_present = SelectField("Alternate Therapy treatment taken",
                                                    choices=CommonDict.form_yes_no_choice, default=tbd)
    fld_type_treat_alt = StringField("Details of treatment taken", default=tbd)
    fld_duration_treat_alt = StringField("Duration of treatment", default=tbd)
    fld_cancer_treatment_home_form_present = SelectField("Home Remedy treatment taken",
                                                    choices=CommonDict.form_yes_no_choice, default=tbd)
    fld_type_treat_home = StringField("Details of treatment taken", default=tbd)
    fld_duration_treat_home = StringField("Duration of treatment", default=tbd)
    fld_other_cancer_treatment = SelectField("Other treatment taken for cancer",
                                                          choices=CommonDict.form_yes_no_choice, default=tbd)
    fld_other_type_treat = StringField("Details of treatment taken", default=tbd)
    fld_other_duration_treat = StringField("Duration of treatment", default=tbd)

class PatientCancerHistory(SectionForm):
    def get_summary(self):
        return "Medical Condition" + str(self.fld_type_of_cancer.data)
    fld_type_cancer = StringField("Type of Cancer: ")
    fld_year_diagnosis = StringField("Year of diagnosis: ")
    fld_cancer_treatment_form_present = SelectField("Treatment taken for cancer", choices=CommonDict.form_yes_no_choice)
    cancer_treatment_form = FormField(CancerTreatmentForm)
    submit_button = SubmitField('Submit Form')

class TreatmentForm(BaseForm):
    repeater = FieldList(FormField(CancerTreatmentForm), min_entries=1)

class FamilyCancerHistory(SectionForm):
    fld_type_of_cancer = StringField("Type of Cancer")
    fld_relation_to_patient = SelectField("Relation to patient (for example, mothers brother (mama) is Maternal Family)"
                                      , choices= PatientHistoryDict.family_degree_choice)
    fld_type_relation = StringField("Specific Relationship (for example, mothers brother (mama) is Brother)")
    fld_age_at_detection_yrs = StringField('Age at detection (yrs)')
    submit_button = SubmitField('Submit Form')
