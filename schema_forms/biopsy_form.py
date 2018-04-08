from wtforms import Form, StringField, validators, IntegerField, SelectField, RadioField
from wtforms.fields.html5 import DateField
from schema_forms.models import Biopsy_Info
from db_dict.biopsy import Biopsy_dict

class Biopsy_info_Form (Form):
    consent_stat_biopsy = RadioField('Has consent been taken from patient?', choices=Biopsy_dict.consent_stat_choice)
    consent_form_biopsy = RadioField('Is consent form with signature present in file ?', choices=
                                                                                    Biopsy_dict.consent_form_choice)
    block_serial_number_biopsy = StringField('Block Serial Number', [validators.Length(min=1, max=50)])
    block_location_biopsy = StringField("to try multiple fields here since it has a format")
    block_current_location_biopsy = StringField ("What is the current location of block?")
    biopsy_custody_pccm = RadioField('Is the biopsy report in PCCM custody?',
                                     choices=Biopsy_dict.biopsy_custody_pccm_choice)
    biopsy_block_id = StringField("Biopsy Block ID")
    biopsy_block_number = IntegerField("Number of blocks")
    biopsy_date = DateField("Date of Biopsy")
    biopsy_lab_id = StringField("Biopsy Lab ID")
    biopsy_type = SelectField("Biopsy Type", choices=Biopsy_dict.biopsy_type_choice)
    biopsy_tumour_diagnosis = SelectField("Tumour Diagnosis", choices = Biopsy_dict.tumour_diagnosis_choice)
    biopsy_tumour_grade = SelectField("Tumour Grade", choices = Biopsy_dict.tumour_grade_choice)
    biopsy_lymphovascular_emboli = RadioField('Are Lymphovascular emboli seen?',
                                              choices=Biopsy_dict.lymphovascular_emboli_choice)
    dcis_biopsy = RadioField("Does the biopsy show DCIS", choices=Biopsy_dict.dcis_biopsy_choice)
    tumour_er_biopsy = RadioField("ER Status", choices=Biopsy_dict.tumour_er_choice)
    tumour_er_percent_biopsy = IntegerField("ER Percent")
    tumour_pr_biopsy = RadioField("PR Status", choices=Biopsy_dict.tumour_pr_choice)
    tumour_pr_percent_biopsy = IntegerField("PR Percent")
    tumour_her2_biopsy = RadioField("HER2 Status", choices=Biopsy_dict.tumour_her2_choice)
    tumour_her2_grade_biopsy = StringField("HER2 Grade")
    tumour_ki67_biopsy = IntegerField("Ki67 Percent")
    fnac = RadioField("Lymph Node biopsy FNAC", choices= Biopsy_dict.fnac_choice)
    fnac_location = SelectField("FNAC Location", choices = Biopsy_dict.fnac_location_choice)
    fnac_diagnosis = SelectField("FNAC Diagnosis", choices = Biopsy_dict.fnac_diagnosis_choice)


    def to_model(self):
        """
        :returns Biopsy_Form: model for the form
        """
        biopsy = Biopsy_Info( consent_stat_biopsy=self.consent_stat_biopsy.data,
                              consent_form_biopsy=self.consent_form_biopsy.data,
                              block_serial_number_biopsy=self.block_serial_number_biopsy.data,
                              block_location_biopsy=self.block_location_biopsy.data,
                              block_current_location_biopsy=self.block_current_location_biopsy.data,
                              biopsy_custody_pccm=self.biopsy_custody_pccm.data,
                              biopsy_block_id=self.biopsy_block_id.data,
                              biopsy_block_number=self.biopsy_block_number.data,
                              biopsy_date=self.biopsy_date.data,
                              biopsy_lab_id=self.biopsy_lab_id.data,
                              biopsy_type=self.biopsy_type.data,
                              biopsy_tumour_diagnosis=self.biopsy_tumour_diagnosis.data,
                              biopsy_tumour_grade=self.biopsy_tumour_grade.data,
                              biopsy_lymphovascular_emboli=self.biopsy_lymphovascular_emboli.data,
                              dcis_biopsy = self.dcis_biopsy.data,
                              tumour_er_biopsy=self.tumour_er_biopsy.data,
                              tumour_er_percent_biopsy =self.tumour_er_percent_biopsy.data,
                              tumour_pr_biopsy = self.tumour_pr_biopsy.data,
                              tumour_pr_percent_biopsy = self.tumour_pr_percent_biopsy.data,
                              tumour_her2_biopsy = self.tumour_her2_biopsy.data,
                              tumour_her2_grade_biopsy = self.tumour_her2_grade_biopsy.data,
                              tumour_ki67_biopsy = self.tumour_ki67_biopsy.data,
                              fnac = self.fnac.data,
                              fnac_location = self.fnac_location.data,
                              fnac_diagnosis = self.fnac_diagnosis.data)
        return biopsy

    def from_model(self, biopsy):
        """
        :param PatientForm patient: initialize form based on the model
        """
        self.consent_stat_biopsy.data =  biopsy.consent_stat_biopsy
        self.consent_form_biopsy.data = biopsy.consent_form_biopsy
        self.block_serial_number_biopsy.data = biopsy.block_serial_number_biopsy
        self.block_location_biopsy.data = biopsy.block_location_biopsy
        self.block_current_location_biopsy.data= biopsy.block_current_location_biopsy
        self.biopsy_custody_pccm.data = biopsy.biopsy_custody_pccm
        self.biopsy_block_id.data = biopsy.biopsy_block_id
        self.biopsy_block_number.data = biopsy.biopsy_block_number
        self.biopsy_date.data = biopsy.biopsy_date
        self.biopsy_lab_id.data=  biopsy.biopsy_lab_id
        self.biopsy_type.data = biopsy.biopsy_type
        self.biopsy_tumour_diagnosis.data = biopsy.biopsy_tumour_diagnosis
        self.biopsy_tumour_grade.data = biopsy.biopsy_tumour_grade
        self.biopsy_lymphovascular_emboli.data = biopsy.biopsy_lymphovascular_emboli
        self.dcis_biopsy = biopsy.dcis_biopsy
        self.tumour_er_biopsy =  biopsy.tumour_er_biopsy
        self.tumour_er_percent_biopsy=  biopsy.tumour_er_percent_biopsy
        self.tumour_pr_biopsy =  biopsy.tumour_pr_biopsy
        self.tumour_pr_percent_biopsy=  biopsy.tumour_pr_percent_biopsy
        self.tumour_her2_biopsy =  biopsy.tumour_her2_biopsy
        self.tumour_her2_grade_biopsy =  biopsy.tumour_her2_grade_biopsy
        self.tumour_ki67_biopsy =  biopsy.tumour_ki67_biopsy
        self.fnac_location =  biopsy.fnac_location
        self.fnac_diagnosis =  biopsy.fnac_diagnosis