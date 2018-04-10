from wtforms import Form, StringField, validators, IntegerField, SelectField, RadioField
from wtforms.fields.html5 import DateField
from schema_forms.models import BiopsyInfo
from db_dict.biopsy import BiopsyDict

class BiopsyForm (Form):
    folder_number = StringField('Folder Number', [validators.required()])
    consent_stat_biopsy = RadioField('Has consent been taken from patient?', choices=BiopsyDict.consent_stat_choice)
    consent_form_biopsy = RadioField('Is consent form with signature present in file ?',
                                     choices=BiopsyDict.consent_form_choice)
    block_serial_number_biopsy = StringField('Block Serial Number', [validators.Length(min=1, max=50)])
    block_location_biopsy = StringField("to try multiple fields here since it has a format")
    block_current_location_biopsy = StringField ("What is the current location of block?")
    biopsy_custody_pccm = RadioField('Is the biopsy report in PCCM custody?',
                                     choices=BiopsyDict.biopsy_custody_pccm_choice)
    biopsy_block_id = StringField("Biopsy Block ID")
    biopsy_block_number = IntegerField("Number of blocks")
    biopsy_date = DateField("Date of Biopsy")
    biopsy_lab_id = StringField("Biopsy Lab ID")
    biopsy_type = SelectField("Biopsy Type", choices=BiopsyDict.biopsy_type_choice)
    biopsy_tumour_diagnosis = SelectField("Tumour Diagnosis", choices = BiopsyDict.tumour_diagnosis_choice)
    biopsy_tumour_grade = SelectField("Tumour Grade", choices = BiopsyDict.tumour_grade_choice)
    biopsy_lymphovascular_emboli = RadioField('Are Lymphovascular emboli seen?',
                                              choices=BiopsyDict.lymphovascular_emboli_choice)
    dcis_biopsy = RadioField("Does the biopsy show DCIS", choices=BiopsyDict.dcis_biopsy_choice)
    tumour_er_biopsy = RadioField("ER Status", choices=BiopsyDict.tumour_er_choice)
    tumour_er_percent_biopsy = StringField("ER Percent")
    tumour_pr_biopsy = RadioField("PR Status", choices=BiopsyDict.tumour_pr_choice)
    tumour_pr_percent_biopsy = StringField("PR Percent")
    tumour_her2_biopsy = RadioField("HER2 Status", choices=BiopsyDict.tumour_her2_choice)
    tumour_her2_grade_biopsy = StringField("HER2 Grade")
    tumour_ki67_biopsy = StringField("Ki67 Percent")
    fnac = RadioField("Lymph Node biopsy FNAC", choices= BiopsyDict.fnac_choice)
    fnac_location = SelectField("FNAC Location", choices = BiopsyDict.fnac_location_choice)
    fnac_diagnosis = SelectField("FNAC Diagnosis", choices = BiopsyDict.fnac_diagnosis_choice)


    def to_model(self):
        """
        :returns Biopsy_Form: model for the form
        """
        biopsy = BiopsyInfo(folder_number= self.folder_number.data,
                            consent_stat_biopsy=self.consent_stat_biopsy.data,
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
        :param BiopsyForm biopsy: initialize form based on the model
        """
        self.folder_number.data = biopsy.folder_number
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
        self.dcis_biopsy.data = biopsy.dcis_biopsy
        self.tumour_er_biopsy.data =  biopsy.tumour_er_biopsy
        self.tumour_er_percent_biopsy.data =  biopsy.tumour_er_percent_biopsy
        self.tumour_pr_biopsy.data =  biopsy.tumour_pr_biopsy
        self.tumour_pr_percent_biopsy.data =  biopsy.tumour_pr_percent_biopsy
        self.tumour_her2_biopsy.data =  biopsy.tumour_her2_biopsy
        self.tumour_her2_grade_biopsy.data =  biopsy.tumour_her2_grade_biopsy
        self.tumour_ki67_biopsy.data =  biopsy.tumour_ki67_biopsy
        self.fnac_location.data =  biopsy.fnac_location
        self.fnac_diagnosis.data =  biopsy.fnac_diagnosis