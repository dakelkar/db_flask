from flask_wtf import FlaskForm
from db_dict.common_dict import CommonDict
from wtforms import StringField, validators, IntegerField, SelectField, SubmitField, HiddenField
from wtforms.fields.html5 import DateField
from db_dict.surgery_block import SurgeryDict
from schema_forms.form_utilities import BaseForm, SectionForm


class SurgeryForm (SectionForm):
    def get_summary(self):
        return self.fld_biopsy_tumour_diagnosis.data

    fld_consent_stat_biopsy = SelectField('Has consent been taken from patient?', choices=SurgeryDict.consent_stat_choice)
    fld_consent_form_biopsy = SelectField('Is consent form with signature present in file ?',
                                         choices=SurgeryDict.consent_form_choice)
    fld_block_serial_number_biopsy = StringField('Block Serial Number', [validators.Length(min=1, max=50)])
    fld_block_location_biopsy = StringField("to try multiple fields here since it has a format")
    fld_block_current_location_biopsy = StringField("What is the current location of block?")
    fld_biopsy_custody_pccm = SelectField('Is the biopsy report in PCCM custody?',
                                          choices=SurgeryDict.biopsy_custody_pccm_choice)
    fld_biopsy_custody_pccm_other = StringField("Other")
    fld_biopsy_block_id = StringField("Biopsy Block ID")
    fld_biopsy_block_number = IntegerField("Number of blocks")
    fld_biopsy_date = DateField("Date of Biopsy")
    fld_biopsy_lab_id = StringField("Biopsy Lab ID")
    fld_biopsy_type = SelectField("Biopsy Type", choices=SurgeryDict.biopsy_type_choice)
    fld_biopsy_type_other = StringField("Other")
    fld_biopsy_tumour_diagnosis = SelectField("Tumour Diagnosis", choices=SurgeryDict.tumour_diagnosis_choice)
    fld_biopsy_tumour_diagnosis_other = StringField("Other")
    fld_biopsy_tumour_grade = SelectField("Tumour Grade", choices=SurgeryDict.tumour_grade_choice)
    fld_biopsy_tumour_grade_other = StringField("Other")
    fld_biopsy_lymphovascular_emboli = SelectField('Are Lymphovascular emboli seen?',
                                                   choices=SurgeryDict.lymphovascular_emboli_choice)
    fld_biopsy_lymphovascular_emboli_other = StringField("Other")
    fld_dcis_biopsy = SelectField("Does the biopsy show DCIS", choices=SurgeryDict.dcis_biopsy_choice)
    fld_dcis_biopsy_other = StringField("Other")

    fld_surgery_er_percent = StringField("ER Percent")
    fld_surgery_pr_percent = StringField("PR Percent")
    fld_surgery_her2_grade = StringField("HER2 Grade", default="0")
    fld_surgery_ki67 = StringField("Ki67 Percent", default="0")
    fld_surgery_er = SelectField("ER Status", choices=CommonDict.postive_negative_dict)
    fld_surgery_er_other = StringField("Other")
    fld_surgery_pr = SelectField("PR Status", choices=CommonDict.postive_negative_dict)
    fld_surgery_pr_other = StringField("Other")
    fld_surgery_her2 = SelectField("HER2 Status", choices=SurgeryDict.tumour_her2_choice)
    fld_surgery_her2_other = StringField("Other")

    fld_surgery_sentinel_node_status = SelectField("Status of node", choices=CommonDict.postive_negative_dict)
    fld_surgery_sentinel_node_status_other = StringField('Other')
    fld_surgery_sentinel_node_removed = IntegerField("Number of sentinel node removed", default=0)
    fld_surgery_sentinel_node_positive = IntegerField("Number of sentinel node positive", default=0)
    fld_surgery_axillary_node_status = SelectField("Status of node", choices=CommonDict.postive_negative_dict)
    fld_surgery_axillary_node_status_other = StringField('Other')
    fld_surgery_axillary_node_removed = IntegerField("Number of axillary node removed", default=0)
    fld_surgery_axillary_node_positive = IntegerField("Number of axillary node positive", default=0)
    fld_surgery_axillary_node_number = HiddenField()
    fld_surgery_apical_node_status = SelectField("Status of node", choices=CommonDict.postive_negative_dict)
    fld_surgery_apical_node_status_other = StringField('Other')
    fld_surgery_apical_node_removed = IntegerField("Number of apical node removed", default=0)
    fld_surgery_apical_node_positive = IntegerField("Number of apical node positive", default=0)
    fld_surgery_perinodal_spread = SelectField("Perinodal Spread", choices=CommonDict.absent_present_choice)
    fld_surgery_perinodal_spread_other = StringField('Other')
    fld_surgery_supraclavicular_node_involvement = SelectField("Supraclavicular Node Involvment",
                                                               choices=CommonDict.absent_present_choice)
    fld_surgery_supraclavicular_node_involvement_other = StringField('Other')
    fld_surgery_pt_status = SelectField("pT status", choices=SurgeryDict.pt_status_choice)
    fld_surgery_pt_status_other = StringField('Other')
    fld_surgery_pn_status = SelectField("pN status", choices=SurgeryDict.pn_status_choice)
    fld_surgery_pn_status_other = StringField('Other')
    fld_surgery_pm_status = SelectField("pM status", choices=SurgeryDict.pm_status_choice)
    fld_surgery_pm_status_other = StringField('Other')
    submit_button = SubmitField('Submit Form')