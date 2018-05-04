from wtforms import StringField, TextAreaField, IntegerField, SelectField, FloatField, RadioField, FormField, SubmitField, HiddenField
from wtforms import validators
from wtforms.fields.html5 import DateField
from db_dict.mammography import MammographyDict
from flask_wtf import FlaskForm
from datetime import datetime
from schema_forms import form_utilities
from db_dict.common_dict import CommonDict

class MammoArchDistortionsForm(FlaskForm):
    class Meta:
        csrf = False

    fld_loc_right_breast = SelectField("Location of Architectural Distortion on Right Breast",
                                                                  choices = MammographyDict.
                                                                  mammo_arch_location_right_breast_choice)
    fld_loc_left_breast = SelectField("Location of Architectural Distortion on Left Breast",
                                                                 choices = MammographyDict.
                                                                 mammo_arch_location_left_breast_choice)
    fld_depth =  SelectField("Depth of Architectural Distortion", choices =
                                        MammographyDict.mammo_arch_depth_choice)
    fld_dist = SelectField("Distance of Architectural Distortion from nipple", choices =
                                    MammographyDict.mammo_arch_dist_choice)


    def to_bson(self):
        bson = form_utilities.to_bson(self)
        return bson


    def from_bson(self, p):
        form_utilities.from_bson(self, p)

# to figure out validators...


class MammoMassForm(FlaskForm):
    class Meta:
        csrf = False

    fld_number = IntegerField("Mass detected",[validators.optional()])
    fld_loc_right_breast = SelectField("Location of mass in Right Breast",
                                                   choices=MammographyDict.mammo_mass_location_right_breast_choice)
    fld_loc_left_breast = SelectField("Location of mass in Left Breast",
                                                  choices=MammographyDict.mammo_mass_location_left_breast_choice)
    fld_depth = SelectField("Depth of mass detected", choices=MammographyDict.mammo_mass_depth_choice)
    fld_dist = SelectField("Distance of mass from nipple", choices=MammographyDict.mammo_mass_dist_choice)
    fld_pect = StringField("Distance from Pectoralis Major (cm) if available (NA if not present)")
    fld_shape = SelectField("Shape of mass", choices=MammographyDict.mammo_mass_shape_choice)
    fld_margin = SelectField("Margins of mass", choices=MammographyDict.mammo_mass_margin_choice)
    fld_density = SelectField("Density of mass", choices=MammographyDict.mammo_mass_density_choice)


    def to_bson(self):
        bson = form_utilities.to_bson(self)
        return bson


    def from_bson(self, p):
        form_utilities.from_bson(self, p)

class MammoCalcificationForm(FlaskForm):

    class Meta:
        csrf = False

    fld_number = IntegerField("Group of calcification", [validators.optional()])
    fld_loc_right_breast = SelectField("Location of calcification in Right Breast",
                                                       choices=MammographyDict.mammo_calc_location_right_breast_choice)
    fld_loc_left_breast = SelectField("Location of calcification in Left Breast",
                                                      choices=MammographyDict.mammo_calc_location_left_breast_choice)
    fld_depth = SelectField("Depth of Calcification", choices=MammographyDict.mammo_calc_depth_choice)
    fld_dist = SelectField("Distance of calcification from nipple",
                                      choices=MammographyDict.mamo_calc_dist_choice)
    fld_type = SelectField("Calcification Type",
                                               choices=MammographyDict.mammo_calcification_type_choice)
    fld_diagnosis = SelectField("Calcification Diagnosis",
                                                    choices=MammographyDict.mammo_calcification_diagnosis_choice)


    def to_bson(self):
        bson = form_utilities.to_bson(self)
        return bson


    def from_bson(self, p):
        form_utilities.from_bson(self, p)

class MammographyForm(FlaskForm):
    class Meta:
        csrf = False

    fld_mammo_location = SelectField('Mammography Diagnosis at', choices = MammographyDict.mammo_location_choice)
    fld_mammo_location_other = StringField("Other")
    fld_mammo_details = SelectField("Is this the first mammography?", choices = MammographyDict.mammo_details_choice)
    mammo_date = DateField("Date of mammography", default=datetime.today())
    fld_mammo_accesion = StringField("Accession number of mammography")
    fld_mammo_number = StringField("Number of previous mammographies undergone")
    fld_mammo_report_previous = TextAreaField("Report of previous mammography if available")
    fld_mammo_breast_density = SelectField("Breast Density in Mammography", choices = MammographyDict.mammo_breast_density_choice)

    fld_mammo_mass_present = SelectField("Is there any mass detected?", choices = MammographyDict.mammo_mass_present_choice)
    mammo_mass = FormField(MammoMassForm)

    fld_mammo_calcification_present = SelectField("Are there any calcifications detected?", choices=
                                                    MammographyDict.mammo_calcification_present_choice)
    mammo_calcification = FormField(MammoCalcificationForm)
    
    fld_mammography_architectural_distortions_present = SelectField("Are Architectural Distortions present", choices =
                                        MammographyDict.mammo_arch_present_choice)
    mammography_architectural_distortions = FormField(MammoArchDistortionsForm)
    
    # if set validator here?
    fld_mammo_assym_present = SelectField("Are Asymmetries present", choices =  MammographyDict.mammo_assym_present_choice)
    fld_mammo_assym_location_right_breast = SelectField("Location of asymmetries on Right Breast", choices =
                                                    MammographyDict.mammo_assym_location_right_breast_choice)
    fld_mammo_assym_location_left_breast = SelectField("Location of asymmetries on Left Breast", choices =
                                                   MammographyDict.mammo_assym_location_left_breast_choice)
    fld_mammo_assym_depth = SelectField("Depth of asymmetry", choices =  MammographyDict.mammo_assym_depth_choice)
    fld_mammo_assym_type_right_breast = SelectField("Type of asymmetry on Right Breast", choices =
                                                MammographyDict.mammo_assym_type_right_breast_choice)
    fld_mammo_assym_type_left_breast = SelectField("Type of asymmetry on Left Breast", choices =
                                                MammographyDict.mammo_assym_type_left_breast_choice)
    fld_mammo_intra_mammary_lymph_nodes_present = SelectField("Are intra-mammary lymph nodes present", choices =
                                                          MammographyDict.mammo_intra_mammary_lymph_nodes_choice)
    fld_mammo_intra_mammary_lymph_nodes_description = TextAreaField("Description of intra-mammary lymph nodes")
    fld_mammo_lesion = RadioField(label="Is skin lesion present", choices = MammographyDict.mammo_lesion_choice, default='tbd')
    fld_mammo_lesion_right_breast = SelectField("Location of skin lesion on right breast", choices =
                                            MammographyDict.mammo_lesion_right_breast_choice)
    fld_mammo_lesion_left_breast = SelectField("Location of skin lesion on left breast", choices =
                                           MammographyDict.mammo_lesion_left_breast_choice)
    fld_mammo_asso_feature_skin_retraction = SelectField("Associated Feature: Skin Retraction", choices =
                                                     MammographyDict.mammo_asso_feature_skin_retraction_choice)
    fld_mammo_asso_feature_nipple_retraction = SelectField("Associated Feature: Nipple Retraction", choices =
                                                       MammographyDict.mammo_asso_feature_nipple_retraction_choice)
    fld_mammo_asso_feature_skin_thickening = SelectField("Associated Feature: Skin Thickening", choices =
                                                     MammographyDict.mammo_asso_feature_skin_thickening_choice)
    fld_mammo_asso_feature_trabecular_thickening = SelectField("Associated Feature: Trabecular Thickening", choices =
                                                       MammographyDict.mammo_asso_feature_trabecular_thickening_choice)
    fld_mammo_asso_feature_axillary_adenopathy = SelectField("Associated Feature: Axillary Adenopathy", choices =
                                                         MammographyDict.mammo_asso_feature_axillary_adenopathy_choice)
    fld_mammo_asso_feature_architectural_distortion = SelectField("Associated Feature: Architectural Distortion", choices =
                                                  MammographyDict.mammo_asso_feature_architectural_distortion_choice)
    fld_mammo_asso_feature_calicifications = SelectField("Associated Feature: Calcification", choices =
                                                     MammographyDict.mammo_asso_feature_calicifications_choice)
    fld_mammo_birad = SelectField("BI-RAD classification (if available)",  choices =  MammographyDict.mammo_birad_choice)

    def to_bson(self):
        bson = form_utilities.to_bson(self)
        #spl stuff for datetime
        bson['mammo_date'] =  datetime.combine(self.mammo_date.data, datetime.min.time())

        #spl stuff for subforms
        bson['mammography_architectural_distortions'] = self.mammography_architectural_distortions.to_bson()
        bson['mammo_mass'] = self.mammo_mass.to_bson()
        bson['mammo_calcification'] = self.mammo_calcification.to_bson()
        return bson

    def from_bson(self, p):
        form_utilities.from_bson(self, p)
        #spl stuff for dates
        self.mammo_date.data = p['mammo_date'].date()
        #spl stuff for subforms
        self.mammography_architectural_distortions.from_bson(p['mammography_architectural_distortions'])
        self.mammo_mass.from_bson(p['mammo_mass'])
        self.mammo_calcification.from_bson(p['mammo_calcification'])

class TomographyForm (FlaskForm):
    class Meta:
        csrf = False

    fld_tomography_status = StringField("Form to be done")

    def to_bson(self):
        bson = form_utilities.to_bson(self)
        return bson

    def from_bson(self, p):
        form_utilities.from_bson(self, p)

class ABVSForm (FlaskForm):
    class Meta:
        csrf = False

    fld_abvs_status = StringField("Form to be done")

    def to_bson(self):
        bson = form_utilities.to_bson(self)
        return bson

    def from_bson(self, p):
        form_utilities.from_bson(self, p)

class MRIForm (FlaskForm):
    class Meta:
        csrf = False
    fld_mri_status = StringField("Form to be done")

    def to_bson(self):
        bson = form_utilities.to_bson(self)
        return bson

    def from_bson(self, p):
        form_utilities.from_bson(self, p)

class RadiologyForm(FlaskForm):
    class Meta:
        csrf = False

    fld_folder_number = HiddenField()
    fld_mammography_report_present = SelectField('Is a Mammography or 3D Tomography report present in the patient file?',
                                           choices= CommonDict.yes_no_choice)
    mammography_report = FormField(MammographyForm)

    fld_tomography_report_present = SelectField('Is 3D Tomography report present in the patient file?',
                                           choices= CommonDict.yes_no_choice)
    tomography_report = FormField(TomographyForm)

    fld_abvs_report_present = SelectField('Is a ABVS report present in the patient file?',
                                           choices= CommonDict.yes_no_choice)
    abvs_report = FormField(ABVSForm)

    fld_mri_report_present = SelectField('Is a Breast MRI report present in the patient file?',
                                           choices= CommonDict.yes_no_choice)
    mri_report = FormField(MRIForm)

    fld_form_status = SelectField("Form Status",  choices= MammographyDict.mammo_status_choice)
    last_update = HiddenField()
    submit_button = SubmitField('Submit Form')

    def to_bson(self):
        bson = form_utilities.to_bson(self)
        # spl stuff for datetime
        bson['last_update'] = datetime.today()
        # spl stuff for subforms
        bson['mammography_report'] = self.mammography_report.to_bson()
        bson['tomography_report'] = self.tomography_report.to_bson()
        bson['abvs_report'] = self.abvs_report.to_bson()
        bson['mri_report'] = self.mri_report.to_bson()
        return bson

    def from_bson(self, p):
        form_utilities.from_bson(self, p)
        #spl stuff for dates
        self.last_update.data = p['last_update'].date()
        #spl stuff for subforms
        self.mammography_report.from_bson(p['mammography_report'])
        self.tomography_report.from_bson(p['tomography_report'])
        self.abvs_report.from_bson(p['abvs_report'])
        self.mri_report.from_bson(p['mri_report'])
#in mammo_arch check if validator there if it accepts if momma_arch not called... need nested validators?
#check all patterns
#how is subnesting evaluated?

#$function: should find "other", if False, then new field samefield_other is hidden, but when true is seen so
# dont need new subform, registers as on change function

#figure out how to get user passed to this form...

