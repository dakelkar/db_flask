from wtforms import Form, StringField, TextAreaField, validators, IntegerField, SelectField, FloatField, RadioField
from wtforms.fields.html5 import DateField
from schema_forms.models import MammographyInfo
from db_dict.mammography import MammographyDict

class MammographyForm(Form):
    folder_number = StringField('Folder Number', [validators.required()])
    mammo_location = RadioField('Mammography Diagnosis at', MammographyDict.mammo_location_choice)
    mammo_details = RadioField("Is this the first mammography?", MammographyDict.mammo_details_choice)
    mammo_date = DateField("Date of mammography")
    mammo_accesion = StringField("Accession number of mammography")
    mammo_number = StringField("Number of mammographies undergone (input NA if none)")
    mammo_report_previous = TextAreaField("Report of previous mammography if available (NA if not present)")
    mammo_breast_density = SelectField("Breast Density in Mammography", MammographyDict.mammo_breast_density_choice)
    mammo_mass_present = SelectField("Is there any mass detected?", MammographyDict.mammo_mass_present_choice)
    mammo_mass_number = IntegerField("Number of masses detected (enter 0 if none)")
    mammo_mass_location_right_breast = SelectField("Location of mass in Right Breast",
                                                   MammographyDict.mammo_mass_location_right_breast_choice)
    mammo_mass_location_left_breast = SelectField("Location of mass in Leftt Breast",
                                                  MammographyDict.mammo_mass_location_left_breast_choice)
    mammo_mass_depth = SelectField("Depth of mass detected", MammographyDict.mammo_mass_depth_choice)
    mammo_mass_dist = SelectField("Distance of mass from nipple", MammographyDict.mammo_mass_dist_choice)
    mammo_mass_pect = StringField("Distance from Pectoralis Major (cm) (if available")
    mammo_mass_shape = SelectField("Shape of mass", MammographyDict.mammo_mass_shape_choice)
    mammo_mass_margin = SelectField ("Margins of mass", MammographyDict.mammo_mass_margin_choice)
    mammo_mass_density = SelectField("Density of mass", MammographyDict.mammo_mass_density_choice)

    mammo_calcification_present = SelectField("Are there any calcifications detected?",
                                              MammographyDict.mammo_calcification_present_choice)
    mammo_calc_number = IntegerField("Number of groups of calcifications detected (enter 0 if none)")
    mammo_calc_location_right_breast = SelectField("Location of calcification in Right Breast",
                                                   MammographyDict.mammo_calc_location_right_breast_choice)
    mammo_calc_location_left_breast = SelectField("Location of calcification in Left Breast",
                                                  MammographyDict.mammo_calc_location_left_breast_choice)
    mammo_calc_depth = SelectField("Depth of Calcification",  MammographyDict.mammo_calc_depth_choice)
    mammo_calc_dist = SelectField("Distance of calcification from nipple", MammographyDict.mamo_calc_dist_choice)
    mammo_calcification_type = SelectField("Calcification Type",  MammographyDict.mammo_calcification_type_choice)
    mammo_calcification_diagnosis = SelectField("Calcification Diagnosis",
                                                MammographyDict.mammo_calcification_diagnosis_choice)
    mammo_arch_present = SelectField("Are Architectural Distortions present", MammographyDict.mammo_arch_present_choice)
    mammo_arch_location_right_breast = SelectField("Location of Architectural Distortion on Right Breast",
                                                   MammographyDict.mammo_arch_location_right_breast_choice)
    mammo_arch_location_left_breast = SelectField("Location of Architectural Distortion on Left Breast",
                                                  MammographyDict.mammo_arch_location_left_breast_choice)
    mammo_arch_depth =  SelectField("Depth of Architectural Distortion", MammographyDict.mammo_arch_depth_choice)
    mammo_arch_dist = SelectField("Distance of Architectural Distortion from nipple", MammographyDict.mammo_arch_dist_choice)
    mammo_assym_present = SelectField("Are Asymmetries present", MammographyDict.mammo_assym_present_choice)
    mammo_assym_location_right_breast = SelectField("Location of asymmetries on Right Breast",
                                                    MammographyDict.mammo_assym_location_right_breast_choice)
    mammo_assym_location_left_breast = SelectField("Location of asymmetries on Left Breast",
                                                   MammographyDict.mammo_assym_location_left_breast_choice)
    mammo_assym_depth = SelectField("Depth of asymmetry", MammographyDict.mammo_assym_depth_choice)
    mammo_assym_type_right_breast = SelectField("Type of asymmetry on Right Breast",
                                                MammographyDict.mammo_assym_type_right_breast_choice)
    mammo_assym_type_left_breast = SelectField("Type of asymmetry on Left Breast",
                                                MammographyDict.mammo_assym_type_left_breast_choice)
    mammo_intra_mammary_lymph_nodes_present = SelectField("Are intra-mammary lymph nodes present",
                                                          MammographyDict.mammo_intra_mammary_lymph_nodes_choice)
    mammo_intra_mammary_lymph_nodes_description = TextAreaField("Description of intra-mammary lymph nodes",
                                                                validators="optional")
    mammo_lesion = RadioField("Is skin lesion present", MammographyDict.mammo_lesion_choice)
    mammo_lesion_right_breast = SelectField("Location of skin lesion on right breast",
                                            MammographyDict.mammo_lesion_right_breast_choice)
    mammo_lesion_left_breast = SelectField("Location of skin lesion on left breast",
                                           MammographyDict.mammo_lesion_left_breast_choice)
    mammo_asso_feature_skin_retraction = SelectField("Associated Feature: Skin Retraction",
                                                     MammographyDict.mammo_asso_feature_skin_retraction_choice)
    mammo_asso_feature_nipple_retraction = SelectField("Associated Feature: Nipple Retraction",
                                                       MammographyDict.mammo_asso_feature_nipple_retraction_choice)
    mammo_asso_feature_skin_thickening = SelectField("Associated Feature: Skin Thickening",
                                                     MammographyDict.mammo_asso_feature_skin_thickening_choice)
    mammo_asso_feature_trabecular_thickening = SelectField("Associated Feature: Trabecular Thickening",
                                                           MammographyDict.mammo_asso_feature_trabecular_thickening_choice)
    mammo_asso_feature_axillary_adenopathy = SelectField("Associated Feature: Axillary Adenopathy",
                                                         MammographyDict.mammo_asso_feature_axillary_adenopathy_choice)
    mammo_asso_feature_architectural_distortion = SelectField("Associated Feature: Architectural Distortion",
                                                         MammographyDict.mammo_asso_feature_architectural_distortion_choice)
    mammo_asso_feature_calicifications = SelectField("Associated Feature: Calcification",
                                                     MammographyDict.mammo_asso_feature_calicifications_choice)
    mammo_birad = SelectField("BI-RAD classification (if available)",  MammographyDict.mammo_birad_choice)


    def to_model(self):
        """
        :returns Patient_bio_info_Form: model for the form
        """
        mammography = MammographyForm(folder_number= self.folder_number.data,
                                mammo_location=self.mammo_location.data,
                                mammo_details = self.mammo_details.data,
                                mammo_date = self. mammo_date.data,
                                mammo_accesion = self.mammo_accesion.data,
                                mammo_number = self. mammo_number.data,
                                mammo_report_previous = self.mammo_report_previous.data,
                                mammo_breast_density = self.mammo_breast_density.data,
                                mammo_mass_present = self.mammo_mass_present.data,
                                mammo_mass_number = self.mammo_mass_number.data,
                                mammo_mass_location_right_breast = self.mammo_mass_location_right_breast.data,
                                mammo_mass_location_left_breast = self.mammo_mass_location_left_breast.data,
                                mammo_mass_depth = self.mammo_mass_depth.data,
                                mammo_mass_dist = self.mammo_mass_dist.data,
                                mammo_mass_pect = self.mammo_mass_pect.data,
                                mammo_mass_shape = self.mammo_mass_shape.data,
                                mammo_mass_margin = self.mammo_mass_margin.data,
                                mammo_mass_density = self.mammo_mass_density.data,
                                mammo_calcification_present = self.mammo_calcification_present.data,
                                mammo_calc_number = self.mammo_calc_number.data,
                                mammo_calc_location_right_breast = self.mammo_calc_location_right_breast.data,
                                mammo_calc_location_left_breast = self.mammo_calc_location_left_breast.data,
                                mammo_calc_depth = self.mammo_calc_depth.data,
                                mammo_calc_dist = self.mammo_calc_dist.data,
                                mammo_calcification_type = self.mammo_calcification_type.data,
                                mammo_calcification_diagnosis = self.mammo_calcification_diagnosis.data,
                                mammo_arch_present = self.mammo_arch_present.data,
                                mammo_arch_location_right_breast = self.mammo_arch_location_right_breast.data,
                                mammo_arch_location_left_breast = self.mammo_arch_location_left_breast.data,
                                mammo_arch_depth = self.mammo_arch_depth.data,
                                mammo_arch_dist = self.mammo_arch_dist.data,
                                mammo_assym_present = self.mammo_assym_present.data,
                                mammo_assym_location_right_breast = self.mammo_assym_location_right_breast.data,
                                mammo_assym_location_left_breast = self.mammo_assym_location_left_breast.data,
                                mammo_assym_depth = self.mammo_assym_depth.data,
                                mammo_assym_type_right_breast = self.mammo_assym_type_right_breast.data,
                                mammo_assym_type_left_breast = self.mammo_assym_type_left_breast.data,
                                mammo_intra_mammary_lymph_nodes_present =
                                self.mammo_intra_mammary_lymph_nodes_present.data,
                                mammo_intra_mammary_lymph_nodes_description =
                                self.mammo_intra_mammary_lymph_nodes_description.data,
                                mammo_lesion = self.mammo_lesion.data,
                                mammo_lesion_right_breast = self.mammo_lesion_right_breast.data,
                                mammo_lesion_left_breast = self.mammo_lesion_left_breast.data,
                                mammo_asso_feature_skin_retraction = self.mammo_asso_feature_skin_retraction.data,
                                mammo_asso_feature_nipple_retraction = self.mammo_asso_feature_nipple_retraction.data,
                                mammo_asso_feature_skin_thickening = self.mammo_asso_feature_skin_thickening.data,
                                mammo_asso_feature_trabecular_thickening =
                                self.mammo_asso_feature_trabecular_thickening.data,
                                mammo_asso_feature_axillary_adenopathy =
                                self.mammo_asso_feature_axillary_adenopathy.data,
                                mammo_asso_feature_architectural_distortion =
                                self.mammo_asso_feature_architectural_distortion.data,
                                mammo_asso_feature_calicifications = self.mammo_asso_feature_calicifications.data,
                                mammo_birad = self.mammo_birad.data)
        return mammography

    def from_model(self, mammography):
        """
        :param PatientForm patient: initialize form based on the model
        """
        self.folder_number.data = mammography.folder_number
        self.mammo_location.data = mammography.mammo_location
        self.mammo_details.dat =  mammography.mammo_details
        self.mammo_date.data = mammography.mammo_date
        self.mammo_accesion.data = mammography.mammo_accesion
        self.mammo_number.data = mammography.mammo_number
        self.mammo_report_previous.data = mammography.mammo_report_previous
        self.mammo_breast_density.data = mammography.mammo_breast_density
        self.mammo_mass_present.data = mammography.mammo_mass_present
        self.mammo_mass_number.data = mammography.mammo_mass_number
        self.mammo_mass_location_right_breast.data = mammography.mammo_mass_location_right_breast
        self.mammo_mass_location_left_breast.data = mammography.mammo_mass_location_left_breast
        self.mammo_mass_depth.data = mammography.mammo_mass_depth
        self.mammo_mass_dist.data = mammography.mammo_mass_dist
        self.mammo_mass_pect.data = mammography.mammo_mass_pect
        self.mammo_mass_shape.data = mammography.mammo_mass_shape
        self.mammo_mass_margin.data = mammography.mammo_mass_margin
        self.mammo_mass_density.data = mammography.mammo_mass_density
        self.mammo_calcification_present.data = mammography.mammo_calcification_present
        self.mammo_calc_number.data = mammography.mammo_calc_number
        self.mammo_calc_location_right_breast.data = mammography.mammo_calc_location_right_breast
        self.mammo_calc_location_left_breast.data = mammography.mammo_calc_location_left_breast
        self.mammo_calc_depth.data = mammography.mammo_calc_depth
        self.mammo_calc_dist.data = mammography.mammo_calc_dist
        self.mammo_calcification_type.data = mammography.mammo_calcification_type
        self.mammo_calcification_diagnosis.data = mammography.mammo_calcification_diagnosis
        self.mammo_arch_present.data = mammography.mammo_arch_present
        self.mammo_arch_location_right_breast.data = mammography.mammo_arch_location_right_breast
        self.mammo_arch_location_left_breast.data = mammography.mammo_arch_location_left_breast
        self.mammo_arch_depth.data = mammography.mammo_arch_depth
        self.mammo_arch_dist.data = mammography.mammo_arch_dist
        self.mammo_assym_present.data = mammography.mammo_assym_present
        self.mammo_assym_location_right_breast.data = mammography.mammo_assym_location_right_breast
        self.mammo_assym_location_left_breast.data = mammography.mammo_assym_location_left_breast
        self.mammo_assym_depth.data = mammography.mammo_assym_depth
        self.mammo_assym_type_right_breast.data = mammography.mammo_assym_type_right_breast
        self.mammo_assym_type_left_breast.data = mammography.mammo_assym_type_left_breast
        self.mammo_intra_mammary_lymph_nodes_present.data = mammography.mammo_intra_mammary_lymph_nodes_present
        self.mammo_intra_mammary_lymph_nodes_description.data = mammography.mammo_intra_mammary_lymph_nodes_description
        self.mammo_lesion.data = mammography.mammo_lesion
        self.mammo_lesion_right_breast.data = mammography.mammo_lesion_right_breast
        self.mammo_lesion_left_breast.data = mammography.mammo_lesion_left_breast
        self.mammo_asso_feature_skin_retraction.data = mammography.mammo_asso_feature_skin_retraction
        self.mammo_asso_feature_nipple_retraction.data = mammography.mammo_asso_feature_nipple_retraction
        self.mammo_asso_feature_skin_thickening.data = mammography.mammo_asso_feature_skin_thickening
        self.mammo_asso_feature_trabecular_thickening.data = mammography.mammo_asso_feature_trabecular_thickening
        self.mammo_asso_feature_axillary_adenopathy.data = mammography.mammo_asso_feature_axillary_adenopathy
        self.mammo_asso_feature_architectural_distortion.data = mammography.mammo_asso_feature_architectural_distortion
        self.mammo_asso_feature_calicifications.data = mammography.mammo_asso_feature_calicifications
        self.mammo_birad.data = mammography.mammo_birad

