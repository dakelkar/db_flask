from wtforms import StringField, TextAreaField, SelectMultipleField, SelectField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField
from db_dict.mammography import MammographyDict
from db_dict.common_dict import CommonDict
from schema_forms.form_utilities import BaseForm, SectionForm

tbd = 'To be filled'
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


class SonoMammographyForm(SectionForm):
    fld_sonomammography_acc = StringField("Accession number of Sono-Mammography", default=tbd)
    fld_sonomammography_date = StringField("Date of examination of Sono-mammography", default=tbd)
    fld_sonomammography_tissue = SelectField("Tissue Composition", choices=MammographyDict.sonomammo_tissue_choice)
    fld_sonomammography_tissue_other = StringField("Other")
    fld_sonomammography_calc = SelectField("Is there any calcification reported?", choices=CommonDict.breast_choice)
    fld_sonomammography_calc_other = StringField("Other")
    fld_sonomammography_calc_type = SelectField("Calcification location", choices=MammographyDict.sonomammo_calc_choice)
    fld_sonomammography_calc_type_other = StringField("Other")
    fld_sonomammography_arch = SelectField("Architectural distortion", choices=CommonDict.breast_choice)
    fld_sonomammography_arch_other = StringField("Other")
    fld_sonomammography_duct = SelectField("Duct Changes", choices=CommonDict.breast_choice)
    fld_sonomammography_duct_other = StringField("Other")
    fld_sonomammography_skin = SelectField("Type of Skin Changes", choices=MammographyDict.sonomammo_skin_choice)
    fld_sonomammography_skin_other = StringField("Other")
    fld_sonomammography_edema = SelectField("Edema", choices=CommonDict.breast_choice)
    fld_sonomammography_edema_other = StringField("Other")
    fld_sonomammography_vasc = SelectField("Vascularity", choices=MammographyDict.sonomammo_vascularity_choice)
    fld_sonomammography_vasc_other = StringField("Other")
    fld_sonomammography_elast = SelectField("Elasticity assessment", choices=MammographyDict.sonomammo_elast_choice)
    fld_sonomammography_elast_other = StringField("Other")
    fld_sonomammography_lymph_intra = TextAreaField("Description of intramammary lymph nodes", default=tbd)
    fld_sonomammography_lymph_ax = SelectField("Axillary Lymph Nodes", choices=CommonDict.normal_abnormal_choice)
    fld_sonomammography_lymph_ax_other = StringField("Other")
    fld_sonomammography_lymph_ax_cort = StringField("Cortical thickness of Abnormal Axillary Lymph Nodes", default=tbd)
    fld_sonomammography_lymph_ax_hilum = SelectField("Abnormal Axillary lymph node hilum",
                                               choices=MammographyDict.sonomammo_hilum_choice)
    fld_sonomammography_lymph_ax_hilum_other = StringField("Other")
    fld_sonomammography_lymph_ax_vasc = SelectField("Abnormal Axillary lymph node vascularity",
                                              choices=MammographyDict.sonomammo_lymph_ax_vasc_choice)
    fld_sonomammography_lymph_ax_vasc_other = StringField("Other")
    fld_sonomammography_sol_duct_loc = SelectField("Location of Solitary Dilated duct", choices=CommonDict.breast_choice)
    fld_sonomammography_sol_duct_loc_other = StringField("Other")
    fld_sonomammography_sol_duct_diam = StringField("Diameter of solitary dilated duct (mm)", default=tbd)
    fld_sonomammography_sol_mass = SelectField("Is Intra-ductal solid mass present?",
                                         choices=CommonDict.absent_present_choice)
    fld_sonomammography_sol_mass_other = StringField("Other")
    fld_sonomammography_shear = StringField("Strain and shear wave velocity on elastography type/pattern", default=tbd)
    fld_sonomammography_vtq = StringField("Median Shear Velocity (VTQ) in m/s", default=tbd)
    fld_sonomammography_other_findings = SelectMultipleField("Are there any other findings?",
                                                       choices=MammographyDict.sonomammo_other_findings_choice)
    fld_sonomammography_other_findings_other = StringField("Other")
    fld_sono_birad = SelectField("Does the report include a BI-RAfD assessment/Diagnosis?",
                                 choices=CommonDict.birad_choice)
    fld_sono_birad_other = StringField("Other")
    submit_button = SubmitField('Submit Form')

class SonoMammoMassForm(SectionForm):
    def get_summary(self):
        return "fld-number: " + str(self.fld_number.data)
    fld_number = IntegerField("Mass number", default=1)
    fld_sono_mass_right_location = SelectField("Location of mass in right breast",
                                               choices=CommonDict.breast_location_choice)
    fld_sono_mass_right_location_other = StringField("Other")
    fld_sono_mass_left_location = SelectField("Location of mass in left breast",
                                              choices=CommonDict.breast_location_choice)
    fld_sono_mass_left_location_other = StringField("Other")
    fld_sono_location_clock = StringField("What is the clock position of mass?", default='enter position only')
    fld_sono_mass_shape = SelectField("Shape of mass", choices=MammographyDict.sono_mass_shape_choice)
    fld_sono_mass_shape_other = StringField("Other")
    fld_sono_mass_depth = StringField("Depth of mass (cm)", default=tbd)
    fld_sono_mass_dist = StringField("Distance from nipple (cm)", default=tbd)
    fld_sono_pect_dist = StringField("Distance from Pectoralis Major (cm)", default=tbd)
    fld_sono_mass_orientation = SelectField("Orientation of mass", choices=MammographyDict.sono_orientation_choice)
    fld_sono_mass_orientation_other = StringField("Other")
    fld_sono_mass_margin = SelectField("Margin of mass", choices=MammographyDict.sono_mass_margin_choice)
    fld_sono_mass_margin_other = StringField("Other")
    fld_sono_mass_echo = SelectField("Echo pattern of mass", choices=MammographyDict.sono_mass_echo_choice)
    fld_sono_mass_echo_other = StringField("Other")
    fld_sono_mass_posterior = SelectField("Posterior Acoustic features", choices=MammographyDict.sono_posterior_choice)
    fld_sono_mass_posterior_other = StringField("Other")
    submit_button = SubmitField('Submit Form')
