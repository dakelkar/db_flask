from wtforms import StringField, TextAreaField, SelectField
from wtforms.fields.html5 import DateField
from db_dict.common_dict import CommonDict
from db_dict.mammography import MammographyDict
from schema_forms.form_utilities import  BaseForm

class TomosynthesisForm(BaseForm):
    fld_tomo = SelectField("3D digital Tomosynthesis done",
                           choices=CommonDict.absent_present_choice)
    fld_tomo_date = DateField("Date of Tomosynthesis examination", default=None)
    fld_tomo_acc = StringField("Accession number of Tomosynthesis")
    fld_tomo_commments = TextAreaField("Comments/Notes for Tomosynthesis")

class AbvsForm(BaseForm):
    fld_abvs_date = DateField("Date of examination of ABVS", default=None)
    fld_abvs_acc = StringField("Accession number of ABVS")
    fld_abvs_right_breast_lesion = SelectField("Location of lesion in right breast",
                                               choices=CommonDict.breast_location_choice)
    fld_abvs_right_breast_lesion_other = StringField("Other")
    fld_abvs_left_breast_lesion = SelectField("Location of lesion in left breast",
                                              choices=CommonDict.breast_location_choice)
    fld_abvs_left_breast_lesion_other = StringField("Other")
    fld_abvs_size = StringField("Size of lesion")
    fld_abvs_dist = StringField("Distance from Skin (cm)")
    fld_abvs_pect = StringField("Distance from Pectoralis Major (cm)")
    fld_abvs_diagnosis = SelectField("ABVS Diagnosis", choices=MammographyDict.abvs_diagnosis_choice)

class AssoFeatureForm(BaseForm):
    fld_nipple_retraction = SelectField("Nipple Retraction", choices=CommonDict.absent_present_choice)
    fld_nipple_retraction_other = StringField("Other")
    fld_nipple_invasion = SelectField("Nipple Invasion", choices=CommonDict.absent_present_choice)
    fld_nipple_invasion_other = StringField("Other")
    fld_skin_retraction = SelectField("Skin Retraction", choices=CommonDict.absent_present_choice)
    fld_skin_retraction_other = StringField("Other")
    fld_skin_thickening = SelectField("Skin Thickening", choices=CommonDict.absent_present_choice)
    fld_skin_thickening_other = StringField("Other")
    fld_axillary_adenopathy = SelectField("Axillary Adenopathy", choices=CommonDict.absent_present_choice)
    fld_axillary_adenopathy_other = StringField("Other")
    fld_pectoralis_invasion = SelectField("Pectoralis muscle invasion", choices=CommonDict.absent_present_choice)
    fld_pectoralis_invasion_other = StringField("Other")
    fld_chest_invasion = SelectField("Chest wall invasion", choices=CommonDict.absent_present_choice)
    fld_chest_invasion_other = StringField("Other")
    fld_skin_invasion = SelectField("Skin Invasion", choices= MammographyDict.mri_skin_choice)


