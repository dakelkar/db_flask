from wtforms import Form, StringField, TextAreaField, validators, IntegerField, SelectField, FloatField, RadioField, FormField, SubmitField, HiddenField
from wtforms.fields.html5 import DateField
from db_dict.mammography import MammographyDict
from flask_wtf import FlaskForm
from datetime import datetime

class MammoArchDistortionsForm(FlaskForm):
    class Meta:
        csrf = False


    mammo_arch_location_right_breast = SelectField("Location of Architectural Distortion on Right Breast", choices =
    MammographyDict.mammo_arch_location_right_breast_choice)
    mammo_arch_location_left_breast = SelectField("Location of Architectural Distortion on Left Breast", choices =
                                                  MammographyDict.mammo_arch_location_left_breast_choice)
    mammo_arch_depth =  SelectField("Depth of Architectural Distortion", choices =
                                        MammographyDict.mammo_arch_depth_choice)
    mammo_arch_dist = SelectField("Distance of Architectural Distortion from nipple", choices =
                                    MammographyDict.mammo_arch_dist_choice)

    def to_bson(self):
        return {
            'mammo_arch_location_right_breast': self.mammo_arch_location_right_breast.data,
            'mammo_arch_location_left_breast': self.mammo_arch_location_left_breast.data,
            'mammo_arch_depth': self.mammo_arch_depth.data, 
            'mammo_arch_dist': self.mammo_arch_dist.data
        }

    def from_bson(self, p):
        self.mammo_arch_location_right_breast.data = p['mammo_arch_location_right_breast']
        self.mammo_arch_location_left_breast.data = p['mammo_arch_location_left_breast']
        self.mammo_arch_depth.data = p['mammo_arch_depth']
        self.mammo_arch_dist.data = p['mammo_arch_dist']


class MammographyForm(FlaskForm):
    class Meta:
        csrf = False


    folder_number = HiddenField()
    mammo_location = SelectField('Mammography Diagnosis at', choices = MammographyDict.mammo_location_choice)
    mammo_details = SelectField("Is this the first mammography?", choices = MammographyDict.mammo_details_choice)
    mammo_date = DateField("Date of mammography")
    mammo_accesion = StringField("Accession number of mammography", [validators.Length(min=2, max=50)])
    mammo_number = StringField("Number of mammographies undergone (input NA if none)", [validators.Length(min=2, max=50)])
    mammo_report_previous = TextAreaField("Report of previous mammography if available (NA if not present)", [validators.Length(min=1, max=50)])
    mammo_breast_density = SelectField("Breast Density in Mammography", choices = MammographyDict.mammo_breast_density_choice)
    mammo_mass_present = SelectField("Is there any mass detected?", choices = MammographyDict.mammo_mass_present_choice)
    mammo_mass_number = IntegerField("Number of masses detected (enter 0 if none)")
    mammo_mass_location_right_breast = SelectField("Location of mass in Right Breast",choices =
                                                   MammographyDict.mammo_mass_location_right_breast_choice)
    mammo_mass_location_left_breast = SelectField("Location of mass in Leftt Breast",choices =
                                                  MammographyDict.mammo_mass_location_left_breast_choice)
    mammo_mass_depth = SelectField("Depth of mass detected", choices = MammographyDict.mammo_mass_depth_choice)
    mammo_mass_dist = SelectField("Distance of mass from nipple", choices = MammographyDict.mammo_mass_dist_choice)
    mammo_mass_pect = StringField("Distance from Pectoralis Major (cm) if available (NA if not present)")
    mammo_mass_shape = SelectField("Shape of mass", choices = MammographyDict.mammo_mass_shape_choice)
    mammo_mass_margin = SelectField ("Margins of mass", choices = MammographyDict.mammo_mass_margin_choice)
    mammo_mass_density = SelectField("Density of mass", choices = MammographyDict.mammo_mass_density_choice)

    mammo_calcification_present = SelectField("Are there any calcifications detected?", choices=
                                                    MammographyDict.mammo_calcification_present_choice)
    mammo_calc_number = IntegerField("Number of groups of calcifications detected (enter 0 if none)")
    mammo_calc_location_right_breast = SelectField("Location of calcification in Right Breast", choices=
                                                    MammographyDict.mammo_calc_location_right_breast_choice)
    mammo_calc_location_left_breast = SelectField("Location of calcification in Left Breast",choices =
                                                  MammographyDict.mammo_calc_location_left_breast_choice)
    mammo_calc_depth = SelectField("Depth of Calcification",  choices =
                                    MammographyDict.mammo_calc_depth_choice)
    mammo_calc_dist = SelectField("Distance of calcification from nipple", choices =
                                    MammographyDict.mamo_calc_dist_choice)
    mammo_calcification_type = SelectField("Calcification Type",  choices =
                                            MammographyDict.mammo_calcification_type_choice)
    mammo_calcification_diagnosis = SelectField("Calcification Diagnosis",choices =
                                                MammographyDict.mammo_calcification_diagnosis_choice)
    mammo_arch_present = SelectField("Are Architectural Distortions present", choices =
                                        MammographyDict.mammo_arch_present_choice)
    mammo_arch = FormField(MammoArchDistortionsForm)
    mammo_assym_present = SelectField("Are Asymmetries present", choices =  MammographyDict.mammo_assym_present_choice)
    mammo_assym_location_right_breast = SelectField("Location of asymmetries on Right Breast", choices =
                                                    MammographyDict.mammo_assym_location_right_breast_choice)
    mammo_assym_location_left_breast = SelectField("Location of asymmetries on Left Breast", choices =
                                                   MammographyDict.mammo_assym_location_left_breast_choice)
    mammo_assym_depth = SelectField("Depth of asymmetry", choices =  MammographyDict.mammo_assym_depth_choice)
    mammo_assym_type_right_breast = SelectField("Type of asymmetry on Right Breast", choices =
                                                MammographyDict.mammo_assym_type_right_breast_choice)
    mammo_assym_type_left_breast = SelectField("Type of asymmetry on Left Breast", choices =
                                                MammographyDict.mammo_assym_type_left_breast_choice)
    mammo_intra_mammary_lymph_nodes_present = SelectField("Are intra-mammary lymph nodes present", choices =
                                                          MammographyDict.mammo_intra_mammary_lymph_nodes_choice)
    mammo_intra_mammary_lymph_nodes_description = TextAreaField("Description of intra-mammary lymph nodes", [validators.Length(min=1, max=200)])
    mammo_lesion = RadioField(label="Is skin lesion present", choices = MammographyDict.mammo_lesion_choice, default='tbd')
    mammo_lesion_right_breast = SelectField("Location of skin lesion on right breast", choices =
                                            MammographyDict.mammo_lesion_right_breast_choice)
    mammo_lesion_left_breast = SelectField("Location of skin lesion on left breast", choices =
                                           MammographyDict.mammo_lesion_left_breast_choice)
    mammo_asso_feature_skin_retraction = SelectField("Associated Feature: Skin Retraction", choices =
                                                     MammographyDict.mammo_asso_feature_skin_retraction_choice)
    mammo_asso_feature_nipple_retraction = SelectField("Associated Feature: Nipple Retraction", choices =
                                                       MammographyDict.mammo_asso_feature_nipple_retraction_choice)
    mammo_asso_feature_skin_thickening = SelectField("Associated Feature: Skin Thickening", choices =
                                                     MammographyDict.mammo_asso_feature_skin_thickening_choice)
    mammo_asso_feature_trabecular_thickening = SelectField("Associated Feature: Trabecular Thickening", choices =
                                                       MammographyDict.mammo_asso_feature_trabecular_thickening_choice)
    mammo_asso_feature_axillary_adenopathy = SelectField("Associated Feature: Axillary Adenopathy", choices =
                                                         MammographyDict.mammo_asso_feature_axillary_adenopathy_choice)
    mammo_asso_feature_architectural_distortion = SelectField("Associated Feature: Architectural Distortion", choices =
                                                  MammographyDict.mammo_asso_feature_architectural_distortion_choice)
    mammo_asso_feature_calicifications = SelectField("Associated Feature: Calcification", choices =
                                                     MammographyDict.mammo_asso_feature_calicifications_choice)
    mammo_birad = SelectField("BI-RAD classification (if available)",  choices =  MammographyDict.mammo_birad_choice)
    submit_button = SubmitField('Submit Form')

    def to_bson(self):
        return {"folder_number": self.folder_number.data, 'mammo_location': self.mammo_location.data,
        'mammo_details': self.mammo_details.data, 'mammo_date': datetime.combine(self.mammo_date.data,
                                                                                   datetime.min.time()),
        'mammo_accesion': self.mammo_accesion.data, 'mammo_number': self.mammo_number.data,
        'mammo_report_previous':self.mammo_report_previous.data, 'mammo_breast_density':
        self.mammo_breast_density.data, 'mammo_mass_present':self.mammo_mass_present.data,
        'mammo_mass_number':self.mammo_mass_number.data, 'mammo_mass_location_right_breast':
        self.mammo_mass_location_right_breast.data, 'mammo_mass_location_left_breast':
        self.mammo_mass_location_left_breast.data,'mammo_mass_depth': self.mammo_mass_depth.data,
        'mammo_mass_dist' : self.mammo_mass_dist.data, 'mammo_mass_pect': self.mammo_mass_pect.data,
        'mammo_mass_shape': self.mammo_mass_shape.data,'mammo_mass_margin': self.mammo_mass_margin.data,
        'mammo_mass_density': self.mammo_mass_density.data, 'mammo_calcification_present':
         self.mammo_calcification_present.data, 'mammo_calc_number': self.mammo_calc_number.data,
        'mammo_calc_location_right_breast': self.mammo_calc_location_right_breast.data,
        'mammo_calc_location_left_breast': self.mammo_calc_location_left_breast.data,
        'mammo_calc_depth': self.mammo_calc_depth.data, 'mammo_calc_dist': self.mammo_calc_dist.data,
        'mammo_calcification_type': self.mammo_calcification_type.data,
        'mammo_calcification_diagnosis': self.mammo_calcification_diagnosis.data,

        'mammo_arch_present': self.mammo_arch_present.data,
        'mammo_arch': self.mammo_arch.to_bson(),

        'mammo_assym_present': self.mammo_assym_present.data,
        'mammo_assym_location_right_breast': self.mammo_assym_location_right_breast.data,
        'mammo_assym_location_left_breast': self.mammo_assym_location_left_breast.data,
        'mammo_assym_depth': self.mammo_assym_depth.data,
        'mammo_assym_type_right_breast': self.mammo_assym_type_right_breast.data,
        'mammo_assym_type_left_breast': self.mammo_assym_type_left_breast.data,
        'mammo_intra_mammary_lymph_nodes_present': self.mammo_intra_mammary_lymph_nodes_present.data,
        'mammo_intra_mammary_lymph_nodes_description': self.mammo_intra_mammary_lymph_nodes_description.data,
        'mammo_lesion': self.mammo_lesion.data, 'mammo_lesion_right_breast': self.mammo_lesion_right_breast.data,
        'mammo_lesion_left_breast': self.mammo_lesion_left_breast.data,
        'mammo_asso_feature_skin_retraction': self.mammo_asso_feature_skin_retraction.data,
        'mammo_asso_feature_nipple_retraction': self.mammo_asso_feature_nipple_retraction.data,
        'mammo_asso_feature_skin_thickening': self.mammo_asso_feature_skin_thickening.data,
        'mammo_asso_feature_trabecular_thickening' : self.mammo_asso_feature_trabecular_thickening.data,
        'mammo_asso_feature_axillary_adenopathy': self.mammo_asso_feature_axillary_adenopathy.data,
        'mammo_asso_feature_architectural_distortion': self.mammo_asso_feature_architectural_distortion.data,
        'mammo_asso_feature_calicifications': self.mammo_asso_feature_calicifications.data,
        'mammo_birad': self.mammo_birad.data}

    def from_bson(self, p):
        self.folder_number.data = p['folder_number']
        self.mammo_location.data = p['mammo_location']
        self.mammo_details.data =  p['mammo_details']
        self.mammo_date.data = p['mammo_date'].date()
        self.mammo_accesion.data = p['mammo_accesion']
        self.mammo_number.data = p['mammo_number']
        self.mammo_report_previous.data = p['mammo_report_previous']
        self.mammo_breast_density.data = p['mammo_breast_density']
        self.mammo_mass_present.data = p['mammo_mass_present']
        self.mammo_mass_number.data = p['mammo_mass_number']
        self.mammo_mass_location_right_breast.data = p['mammo_mass_location_right_breast']
        self.mammo_mass_location_left_breast.data = p['mammo_mass_location_left_breast']
        self.mammo_mass_depth.data = p['mammo_mass_depth']
        self.mammo_mass_dist.data = p['mammo_mass_dist']
        self.mammo_mass_pect.data = p['mammo_mass_pect']
        self.mammo_mass_shape.data = p['mammo_mass_shape']
        self.mammo_mass_margin.data = p['mammo_mass_margin']
        self.mammo_mass_density.data = p['mammo_mass_density']
        self.mammo_calcification_present.data = p['mammo_calcification_present']
        self.mammo_calc_number.data = p['mammo_calc_number']
        self.mammo_calc_location_right_breast.data = p['mammo_calc_location_right_breast']
        self.mammo_calc_location_left_breast.data = p['mammo_calc_location_left_breast']
        self.mammo_calc_depth.data = p['mammo_calc_depth']
        self.mammo_calc_dist.data = p['mammo_calc_dist']
        self.mammo_calcification_type.data = p['mammo_calcification_type']
        self.mammo_calcification_diagnosis.data = p['mammo_calcification_diagnosis']
        
        self.mammo_arch_present.data = p['mammo_arch_present']
        self.mammo_arch.from_bson(p['mammo_arch'])

        self.mammo_assym_present.data = p['mammo_assym_present']
        self.mammo_assym_location_right_breast.data = p['mammo_assym_location_right_breast']
        self.mammo_assym_location_left_breast.data = p['mammo_assym_location_left_breast']
        self.mammo_assym_depth.data = p['mammo_assym_depth']
        self.mammo_assym_type_right_breast.data = p['mammo_assym_type_right_breast']
        self.mammo_assym_type_left_breast.data = p['mammo_assym_type_left_breast']
        self.mammo_intra_mammary_lymph_nodes_present.data = p['mammo_intra_mammary_lymph_nodes_present']
        self.mammo_intra_mammary_lymph_nodes_description.data = p['mammo_intra_mammary_lymph_nodes_description']
        self.mammo_lesion.data = p['mammo_lesion']
        self.mammo_lesion_right_breast.data = p['mammo_lesion_right_breast']
        self.mammo_lesion_left_breast.data = p['mammo_lesion_left_breast']
        self.mammo_asso_feature_skin_retraction.data = p['mammo_asso_feature_skin_retraction']
        self.mammo_asso_feature_nipple_retraction.data = p['mammo_asso_feature_nipple_retraction']
        self.mammo_asso_feature_skin_thickening.data = p['mammo_asso_feature_skin_thickening']
        self.mammo_asso_feature_trabecular_thickening.data = p['mammo_asso_feature_trabecular_thickening']
        self.mammo_asso_feature_axillary_adenopathy.data = p['mammo_asso_feature_axillary_adenopathy']
        self.mammo_asso_feature_architectural_distortion.data = p['mammo_asso_feature_architectural_distortion']
        self.mammo_asso_feature_calicifications.data = p['mammo_asso_feature_calicifications']
        self.mammo_birad.data = p['mammo_birad']


