from wtforms import StringField, TextAreaField, IntegerField, SelectField, FloatField, RadioField, FormField, \
    SubmitField, HiddenField, BooleanField, SelectMultipleField, FieldList
from wtforms.fields.core import UnboundField

from wtforms import validators
from wtforms.fields.html5 import DateField
from db_dict.mammography import MammographyDict
from flask_wtf import FlaskForm
from datetime import datetime
from schema_forms import form_utilities
from db_dict.common_dict import CommonDict
from schema_forms.form_utilities import BaseForm, SectionForm


class MammoMassForm(SectionForm):
    def get_summary(self):
        return "fld-number: " + str(self.fld_number.data)
    fld_number = IntegerField("Mass number", default=1)
    fld_loc_right_breast = SelectField("Location of mass in Right Breast", choices = MammographyDict.mammo_mass_location_right_breast_choice)
    fld_loc_right_breast_other = StringField("Other")
    fld_loc_left_breast = SelectField("Location of mass in Left Breast", choices=MammographyDict.mammo_mass_location_left_breast_choice)
    fld_loc_left_breast_other = StringField("Other")
    fld_depth = SelectField("Depth of mass detected", choices=MammographyDict.mammo_mass_depth_choice)
    fld_depth_other = StringField("Other")
    fld_dist = SelectField("Distance of mass from nipple", choices=MammographyDict.mammo_mass_dist_choice)
    fld_dist_other = StringField("Other")
    fld_pect = StringField("Distance from Pectoralis Major (cm) if available (NA if not present)")
    fld_shape = SelectField("Shape of mass", choices=MammographyDict.mammo_mass_shape_choice)
    fld_shape_other = StringField("Other")
    fld_margin = SelectField("Margins of mass", choices=MammographyDict.mammo_mass_margin_choice)
    fld_margin_other = StringField("Other")
    fld_density = SelectField("Density of mass", choices=MammographyDict.mammo_mass_density_choice)
    fld_density_other = StringField("Other")
    submit_button = SubmitField('Submit Form')


class MammoCalcificationForm(SectionForm):
    def get_summary(self):
        return "fld-number: " + str(self.fld_number.data)
        
    fld_number = IntegerField("Group of calcification", default = 1)
    fld_loc_right_breast = SelectField("Location of calcification in Right Breast", choices=MammographyDict.mammo_calc_location_right_breast_choice)
    fld_loc_right_breast_other = StringField("Other")
    fld_loc_left_breast = SelectField("Location of calcification in Left Breast", choices=MammographyDict.mammo_calc_location_left_breast_choice)
    fld_loc_left_breast_other = StringField("Other")
    fld_depth = SelectField("Depth of Calcification", choices=MammographyDict.mammo_calc_depth_choice)
    fld_depth_other = StringField("Other")
    fld_dist = SelectField("Distance of calcification from nipple", choices=MammographyDict.mamo_calc_dist_choice)
    fld_dist_other = StringField("Other")
    fld_type = SelectField("Calcification Type", choices=MammographyDict.mammo_calcification_type_choice)
    fld_type_other = StringField("Other")
    fld_diagnosis = SelectField("Calcification Diagnosis", choices=MammographyDict.mammo_calcification_diagnosis_choice)
    fld_diagnosis_other = StringField("Other")
    submit_button = SubmitField('Submit Form')


class MammoArchDistortionsForm(BaseForm):
    pass

class MammoAssymetryForm(BaseForm):
    pass

class AssoFeatureForm(BaseForm):
    pass

class MammographyForm(SectionForm):
    def get_summary(self):
        return self.fld_mammo_location.data

    fld_mammo_location = SelectField('Mammography Diagnosis at', choices=MammographyDict.mammo_location_choice)
    fld_mammo_details = SelectField("Is this the first mammography?", choices=MammographyDict.mammo_details_choice)
    fld_mammo_date = DateField("Date of mammography")
    fld_mammo_accesion = StringField("Accession number of mammography")
    fld_mammo_number = StringField("Number of previous mammographies undergone")
    fld_mammo_report_previous = TextAreaField("Report of previous mammography if available")
    fld_mammo_breast_density = SelectField("Breast Density in Mammography",
                                           choices=MammographyDict.mammo_breast_density_choice)


    fld_mammography_architectural_distortions_form_present = SelectField("Are Architectural Distortions present",
                                                                    choices=MammographyDict.mammo_arch_present_choice)
    mammography_architectural_distortions_form = FormField(
            MammoArchDistortionsForm.append_select_fields([
            ("fld_loc_right_breast", (
                "Location of Architectural Distortion on Right Breast",
                MammographyDict.mammo_arch_location_right_breast_choice)),
            ("fld_loc_left_breast", (
                "Location of Architectural Distortion on Left Breast",
                MammographyDict.mammo_arch_location_left_breast_choice)),
            ("fld_depth",  (
                "Depth of Architectural Distortion", 
                MammographyDict.mammo_arch_depth_choice)),
            ("fld_dist", (
                "Distance of Architectural Distortion from nipple", 
                MammographyDict.mammo_arch_dist_choice)),
        ])
    )

    fld_mammography_asymmetry_form_present = SelectField("Are Asymmetries present", choices=MammographyDict.mammo_assym_present_choice)
    mammography_asymmetry_form = FormField(
        MammoAssymetryForm.append_select_fields([
            ("fld_location_right_breast", ("Location of asymmetries on Right Breast", MammographyDict.mammo_assym_location_right_breast_choice)),
            ("fld_location_left_breast", ("Location of asymmetries on Left Breast", MammographyDict.mammo_assym_location_left_breast_choice)),
            ("fld_depth", ("Depth of asymmetry", MammographyDict.mammo_assym_depth_choice)),
            ("fld_type_right_breast", ("Type of asymmetry on Right Breast", MammographyDict.mammo_assym_type_right_breast_choice)),
            ("fld_left_breast", ("Type of asymmetry on Left Breast", MammographyDict.mammo_assym_type_left_breast_choice)),
        ])
    )

    fld_mammo_intra_mammary_lymph_nodes_present = SelectField("Are intra-mammary lymph nodes present",
                                                              choices=MammographyDict.mammo_intra_mammary_lymph_nodes_choice)
    fld_mammo_intra_mammary_lymph_nodes_description = TextAreaField("Description of intra-mammary lymph nodes")
    fld_mammo_lesion = SelectField(label="Is skin lesion present", choices=MammographyDict.mammo_lesion_choice,
                                  default='tbd')
    fld_mammo_lesion_right_breast = SelectField("Location of skin lesion on right breast",
                                                choices=MammographyDict.mammo_lesion_right_breast_choice)
    fld_mammo_lesion_left_breast = SelectField("Location of skin lesion on left breast",
                                               choices=MammographyDict.mammo_lesion_left_breast_choice)
    fld_mammography_associated_features_form_present = SelectField("Are associated features present?",
                                                              choices = CommonDict.yes_no_choice)
    mammography_associated_features_form = FormField(
        AssoFeatureForm.append_select_fields([
            ("fld_skin_retraction", ("Skin Retraction", CommonDict.absent_present_choice)),
            ("fld_nipple_retraction", ("Nipple Retraction", CommonDict.absent_present_choice)),
            ("fld_skin_thickening", ("Skin Thickening", CommonDict.absent_present_choice)),
            ("fld_trabecular_thickening", ("Trabecular Thickening", CommonDict.absent_present_choice)),
            ("fld_axillary_adenopathy", ("Axillary Adenopathy", CommonDict.absent_present_choice)),
            ("fld_architectural_distortion", ("Architectural Distortion", CommonDict.absent_present_choice)),
            ("fld_calicifications", ("Calcification", CommonDict.absent_present_choice)),
        ])
    )

    fld_mammo_birad = SelectField("BI-RAD classification (if available)", choices=MammographyDict.mammo_birad_choice)
    submit_button = SubmitField('Submit Form')

