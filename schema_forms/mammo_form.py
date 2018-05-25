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


class BaseForm(FlaskForm):

    def to_bson(self):
        bson = form_utilities.to_bson(self)
        return bson

    def from_bson(self, p):
        form_utilities.from_bson(self, p)

    @classmethod
    def append_field(cls, name, field):
        setattr(cls, name, field)
        return cls

    @classmethod
    def append_select_fields(cls, fields):
        for field in fields:
            setattr(cls, field[0], SelectField(field[1][0], choices=field[1][1]))
            setattr(cls, field[0] + "_other", StringField("Other"))     

        return cls

class MammoArchDistortionsForm(BaseForm):
    pass

class MammoMassForm(BaseForm):
    fld_number = IntegerField("Mass detected",[validators.optional()])
    fld_pect = StringField("Distance from Pectoralis Major (cm) if available (NA if not present)")
    pass


class MammoCalcificationForm(BaseForm):
    fld_number = IntegerField("Group of calcification", [validators.optional()])
    pass


class MammoAssymetryForm(BaseForm):
    pass


class AssoFeatureForm(BaseForm):
    pass


class MammographyForm(FlaskForm):
    class Meta:
        csrf = False

    fld_folder_number = HiddenField()
    fld_mammo_location = SelectField('Mammography Diagnosis at', choices=MammographyDict.mammo_location_choice)
    fld_mammo_details = SelectField("Is this the first mammography?", choices=MammographyDict.mammo_details_choice)
    mammo_date = DateField("Date of mammography")
    fld_mammo_accesion = StringField("Accession number of mammography")
    fld_mammo_number = StringField("Number of previous mammographies undergone")
    fld_mammo_report_previous = TextAreaField("Report of previous mammography if available")
    fld_mammo_breast_density = SelectField("Breast Density in Mammography",
                                           choices=MammographyDict.mammo_breast_density_choice)

    fld_mammo_mass_present = SelectField("Is there any mass detected?",
                                         choices=MammographyDict.mammo_mass_present_choice)
    mammo_mass = FormField(
        MammoMassForm.append_select_fields([
            ("fld_loc_right_breast", ("Location of mass in Right Breast", MammographyDict.mammo_mass_location_right_breast_choice)),
            ("fld_loc_left_breast", ("Location of mass in Left Breast", MammographyDict.mammo_mass_location_left_breast_choice)),
            ("fld_depth", ("Depth of mass detected", MammographyDict.mammo_mass_depth_choice)),
            ("fld_dist", ("Distance of mass from nipple", MammographyDict.mammo_mass_dist_choice)),
            ("fld_shape", ("Shape of mass", MammographyDict.mammo_mass_shape_choice)),
            ("fld_margin", ("Margins of mass", MammographyDict.mammo_mass_margin_choice)),
            ("fld_density", ("Density of mass", MammographyDict.mammo_mass_density_choice)),
        ])
    )

    fld_mammo_calcification_present = SelectField("Are there any calcifications detected?",
                                                  choices=MammographyDict.mammo_calcification_present_choice)
    mammo_calcification = FormField(
        MammoCalcificationForm.append_select_fields([
            ("fld_loc_right_breast", ("Location of calcification in Right Breast", MammographyDict.mammo_calc_location_right_breast_choice)),
            ("fld_loc_left_breast", ("Location of calcification in Left Breast", MammographyDict.mammo_calc_location_left_breast_choice)),
            ("fld_depth", ("Depth of Calcification", MammographyDict.mammo_calc_depth_choice)),
            ("fld_dist", ("Distance of calcification from nipple", MammographyDict.mamo_calc_dist_choice)),
            ("fld_type", ("Calcification Type", MammographyDict.mammo_calcification_type_choice)),
            ("fld_diagnosis", ("Calcification Diagnosis", MammographyDict.mammo_calcification_diagnosis_choice)),
        ])
    )

    fld_mammography_architectural_distortions_present = SelectField("Are Architectural Distortions present",
                                                                    choices=MammographyDict.mammo_arch_present_choice)
    mammography_architectural_distortions = FormField(
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

    fld_mammography_asymmetry_present = SelectField("Are Asymmetries present", choices=MammographyDict.mammo_assym_present_choice)
    mammography_asymmetry = FormField(
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
    fld_mammography_associated_features_present = SelectField("Are associated features present?",
                                                              choices = CommonDict.yes_no_choice)
    mammography_associated_features = FormField(
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
    fld_form_status = SelectField("Form Status",  choices= MammographyDict.mammo_status_choice)
    last_update = HiddenField()
    submit_button = SubmitField('Submit Form')

    def to_bson(self):
        bson = form_utilities.to_bson(self)
        # spl stuff for datetime
        bson['last_update'] = datetime.today()
        bson['mammo_date'] =  datetime.combine(self.mammo_date.data, datetime.min.time())
        #spl stuff for subforms
        bson['mammography_architectural_distortions'] = self.mammography_architectural_distortions.to_bson()
        bson['mammo_mass'] = self.mammo_mass.to_bson()
        bson['mammo_calcification'] = self.mammo_calcification.to_bson()
        bson['mammography_asymmetry']= self.mammography_asymmetry.to_bson()
        bson['mammography_associated_features']= self.mammography_associated_features.to_bson()
        # spl stuff for subforms

        return bson

    def from_bson(self, p):
        form_utilities.from_bson(self, p)
        #spl stuff for dates
        self.last_update.data = p['last_update'].date()
        self.mammo_date.data = p['mammo_date'].date()
        #spl stuff for subforms
        self.mammography_architectural_distortions.from_bson(p['mammography_architectural_distortions'])
        self.mammo_mass.from_bson(p['mammo_mass'])
        self.mammo_calcification.from_bson(p['mammo_calcification'])
        self.mammography_asymmetry.from_bson(p['mammography_asymmetry'])
        self.mammography_associated_features.from_bson(p['mammography_associated_features'])

#in mammo_arch check if validator there if it accepts if momma_arch not called... need nested validators?
#check all patterns
#how is subnesting evaluated?

#$function: should find "other", if False, then new field samefield_other is hidden, but when true is seen so
# dont need new subform, registers as on change function

#figure out how to get user passed to this form...

