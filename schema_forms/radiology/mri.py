from wtforms import StringField, TextAreaField, IntegerField, SelectField, FormField, \
    SubmitField
from wtforms.fields.html5 import DateField
from db_dict.mammography import MammographyDict
from db_dict.common_dict import CommonDict
from schema_forms.form_utilities import BaseForm, SectionForm
from schema_forms.radiology.other_radiology import AssoFeatureForm

tbd = 'To be filled'

class MRIForm(SectionForm):
    fld_mri_breast_date = StringField("Date of examination of MRI", default=tbd)
    fld_mri_breast_acc = StringField("Accession number of MRI (Include location)", default=tbd)
    fld_mri_fgt = SelectField("Ammount of Fibroglandular Tissue", choices=MammographyDict.mri_fgt_choice)
    fld_mri_fgt_other = StringField("Other")
    fld_mri_bpe_level = SelectField("Background parenchymal enhancement Level",
                                    choices=MammographyDict.mri_bpe_level_choice)
    fld_mri_bpe_symm = SelectField("Background parenchymal enhancement Symmetry",
                                   choices=MammographyDict.mri_bpe_symm_choice)
    fld_mri_bpe_symm_other = StringField("Other")
    fld_mri_focus = StringField("Details of Focus", default=tbd)
    fld_m_r_i_associated_features_form_present = SelectField("Are Associated Features present",
                                                                         choices=CommonDict.form_yes_no_choice)
    m_r_i_associated_features_form = FormField(AssoFeatureForm)
    fld_mri_fat_lesions = SelectField("Fat Containing Lesions", choices=MammographyDict.mri_fat_lesion_choice)
    fld_mri_fat_lesions_other = StringField("Other")
    fld_mri_kinetics_initial = SelectField(
        "Kinetic curve assessment Signal intensity (SI)/time curve description (Initial Phase)",
        choices=MammographyDict.mri_kinetics_initial_choice)
    fld_mri_kinetics_initial_other = StringField("Other")
    fld_mri_kinetics_delayed = SelectField(
        "Kinetic curve assessment Signal intensity (SI)/time curve description (Delayed Phase)",
        choices=MammographyDict.mri_kinetics_delayed_choice)
    fld_mri_kinetics_delayed_other = StringField("Other")
    fld_mri_breast_non_enhance = SelectField("Non-enhancing findings", choices=MammographyDict.mri_non_enhance_choice)
    fld_mri_breast_non_enhance_other = StringField("Other")
    fld_mri_breast_implant = StringField("Implant related findings", default=tbd)
    fld_mri_breast_lesion_right = SelectField("Location of lesion on Right Breast",
                                              choices=CommonDict.breast_location_choice)
    fld_mri_breast_lesion_right_other = StringField("Other")
    fld_mri_breast_lesion_left = SelectField("Location of lesion on Left Breast", choices=CommonDict.breast_location_choice)
    fld_mri_breast_lesion_left_other = StringField("Other")
    fld_mri_breast_lesion_depth = StringField("Lesion depth", default=tbd)
    fld_mri_lesion_size = StringField("Size of lesion", default=tbd)
    fld_mri_lesion_dist = StringField("Distance from Skin (cm)", default=tbd)
    fld_mri_lesion_pect = StringField("Distance from Pectoralis Major (cm)", default=tbd)
    fld_mri_breast_birad = SelectField("BI-RAD assessment/Diagnosis", choices=CommonDict.birad_choice)
    fld_mri_breast_birad_other = StringField("Other")
    submit_button = SubmitField('Submit Form')

class MRIMassForm(SectionForm):
    fld_number = IntegerField("Mass number", default=1)
    fld_loc_right_breast = SelectField("Location of mass in Right Breast",
                                       choices=MammographyDict.mammo_mass_location_right_breast_choice)
    fld_loc_right_breast_other = StringField("Other")
    fld_loc_left_breast = SelectField("Location of mass in Left Breast",
                                      choices=MammographyDict.mammo_mass_location_left_breast_choice)
    fld_loc_left_breast_other = StringField("Other")
    fld_shape = SelectField("Shape of mass", choices=MammographyDict.mammo_mass_shape_choice)
    fld_shape_other = StringField("Other")
    fld_margin = SelectField("Margins of mass", choices=MammographyDict.mri_mass_margin_choice)
    fld_margin_other = StringField("Other")
    fld_mass_internal = SelectField("Internal enhancement characteristics",
                                    choices=MammographyDict.mri_mass_internal_choice)
    fld_mass_internal_other = StringField("Other")
    submit_button = SubmitField('Submit Form')


