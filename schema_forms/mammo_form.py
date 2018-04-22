from wtforms import StringField, TextAreaField, validators, IntegerField, SelectField, FloatField, RadioField, FormField, SubmitField, HiddenField
from wtforms.fields.html5 import DateField
from db_dict.mammography import MammographyDict
from flask_wtf import FlaskForm
from datetime import datetime, date
from schema_forms.other_form import OthersForm
#need help creating and deploying this.. - see dict it appears many times to code as new sub field every time?

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


class MammoMassForm(FlaskForm):
    class Meta:
        csrf = False

    mammo_mass_number = IntegerField("Mass detected", default=1)
    mammo_mass_location_right_breast = SelectField("Location of mass in Right Breast",
                                                   choices=MammographyDict.mammo_mass_location_right_breast_choice)
    mammo_mass_location_left_breast = SelectField("Location of mass in Left Breast",
                                                  choices=MammographyDict.mammo_mass_location_left_breast_choice)
    mammo_mass_depth = SelectField("Depth of mass detected", choices=MammographyDict.mammo_mass_depth_choice)
    mammo_mass_dist = SelectField("Distance of mass from nipple", choices=MammographyDict.mammo_mass_dist_choice)
    mammo_mass_pect = StringField("Distance from Pectoralis Major (cm) if available (NA if not present)")
    mammo_mass_shape = SelectField("Shape of mass", choices=MammographyDict.mammo_mass_shape_choice)
    mammo_mass_margin = SelectField("Margins of mass", choices=MammographyDict.mammo_mass_margin_choice)
    mammo_mass_density = SelectField("Density of mass", choices=MammographyDict.mammo_mass_density_choice)

    def to_bson(self):
        return {
            'mammo_mass_number': self.mammo_mass_number.data,
            'mammo_mass_location_right_breast': self.mammo_mass_location_right_breast.data,
            'mammo_mass_location_left_breast': self.mammo_mass_location_left_breast.data,
            'mammo_mass_depth': self.mammo_mass_depth.data,
            'mammo_mass_dist':self.mammo_mass_dist.data,
            'mammo_mass_pect':self.mammo_mass_pect.data,
            'mammo_mass_shape':self.mammo_mass_shape.data,
            'mammo_mass_margin':self.mammo_mass_margin.data,
            'mammo_mass_density':self.mammo_mass_density.data
        }

    def from_bson(self, p):
        self.mammo_mass_number.data = p['mammo_mass_number']
        self.mammo_mass_location_right_breast.data = p['mammo_mass_location_right_breast']
        self.mammo_mass_location_left_breast.data = p['mammo_mass_location_left_breast']
        self.mammo_mass_depth.data = p['mammo_mass_depth']
        self.mammo_mass_dist.data = p['mammo_mass_dist']
        self.mammo_mass_pect.data = p['mammo_mass_pect']
        self.mammo_mass_shape.data = p['mammo_mass_shape']
        self.mammo_mass_margin.data=p['mammo_mass_margin']
        self.mammo_mass_density.data = p['mammo_mass_density']


class MammoCalcificationForm(FlaskForm):

    class Meta:
        csrf = False

    mammo_calcification_number = IntegerField("Group of calcification", default= 1)
    mammo_calcification_location_right_breast = SelectField("Location of calcification in Right Breast",
                                                       choices=MammographyDict.mammo_calc_location_right_breast_choice)
    mammo_calcification_location_left_breast = SelectField("Location of calcification in Left Breast",
                                                      choices=MammographyDict.mammo_calc_location_left_breast_choice)
    mammo_calcification_depth = SelectField("Depth of Calcification", choices=MammographyDict.mammo_calc_depth_choice)
    mammo_calcification_dist = SelectField("Distance of calcification from nipple",
                                      choices=MammographyDict.mamo_calc_dist_choice)
    mammo_calcification_type = SelectField("Calcification Type",
                                               choices=MammographyDict.mammo_calcification_type_choice)
    mammo_calcification_diagnosis = SelectField("Calcification Diagnosis",
                                                    choices=MammographyDict.mammo_calcification_diagnosis_choice)

    def to_bson(self):
        return {
            'mammo_calcification_number': self.mammo_calcification_number.data,
            'mammo_calcification_location_right_breast': self.mammo_calcification_location_right_breast.data,
            'mammo_calcification_location_left_breast': self.mammo_calcification_location_left_breast.data,
            'mammo_calcification_depth': self.mammo_calcification_depth.data,
            'mammo_calcification_dist':self.mammo_calcification_dist.data,
            'mammo_calcification_type':self.mammo_calcification_type.data,
            'mammo_calcification_diagnosis':self.mammo_calcification_diagnosis.data
        }

    def from_bson(self, p):
        self.mammo_calcification_number.data =p['mammo_calcification_number']
        self.mammo_calcification_location_right_breast.data= p['mammo_calcification_location_right_breast']
        self.mammo_calcification_location_left_breast.data = p['mammo_calcification_location_left_breast']
        self.mammo_calcification_depth.data = p['mammo_calcification_depth']
        self.mammo_calcification_dist.data = p['mammo_calcification_dist']
        self.mammo_calcification_type.data = p['mammo_calcification_type']
        self.mammo_calcification_diagnosis.data = p['mammo_calcification_diagnosis']

class MammographyForm(FlaskForm):
    class Meta:
        csrf = False

    fld_folder_number = HiddenField()
    fld_mammo_location = SelectField('Mammography Diagnosis at', choices = MammographyDict.mammo_location_choice)
    fld_mammo_details = SelectField("Is this the first mammography?", choices = MammographyDict.mammo_details_choice)
    mammo_date = DateField("Date of mammography")
    fld_mammo_accesion = StringField("Accession number of mammography")
    fld_mammo_number = StringField("Number of previous mammographies undergone")
    fld_mammo_report_previous = TextAreaField("Report of previous mammography if available")
    fld_mammo_breast_density = SelectField("Breast Density in Mammography", choices = MammographyDict.mammo_breast_density_choice)
    fld_mammo_mass_present = SelectField("Is there any mass detected?", choices = MammographyDict.mammo_mass_present_choice)
    mammo_mass = FormField(MammoMassForm)
    fld_mammo_calcification_present = SelectField("Are there any calcifications detected?", choices=
                                                    MammographyDict.mammo_calcification_present_choice)
    mammo_calcification = FormField(MammoCalcificationForm)
    fld_mammo_arch_present = SelectField("Are Architectural Distortions present", choices =
                                        MammographyDict.mammo_arch_present_choice)
    mammo_arch = FormField(MammoArchDistortionsForm)
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
    fld_mammo_form_status = SelectField("Form Status",  choices= MammographyDict.mammo_status_choice)
    mammo_last_update = DateField('Date of last update', format= '%Y-%m-%d', default=date.today(),
                            validators=[validators.DataRequired()])
    submit_button = SubmitField('Submit Form')

    def to_bson(self):
        fld_prefix = 'fld_'
        field_list = [a for a in dir(self) if a.startswith(fld_prefix)]
        bson = {}
        for field in field_list:
            key = field[len(fld_prefix):]
            bson[key] = self[field].data
        
        #spl stuff for datetime
        bson['mammo_date'] =  datetime.combine(self.mammo_date.data, datetime.min.time())
        bson['mammo_last_update'] = datetime.combine(self.mammo_last_update.data, datetime.min.time())

        #spl stuff for subforms
        bson['mammo_arch'] = self.mammo_arch.to_bson()
        bson['mammo_mass'] = self.mammo_mass.to_bson()
        bson['mammo_calcification'] = self.mammo_calcification.to_bson()
        return bson

    def from_bson(self, p):
        for key in p.keys():
            field_name = 'fld_' + key
            if hasattr(self, field_name):
                print(field_name)
                self[field_name].data = p[key]
        
        #spl stuff for dates
        self.mammo_date.data = p['mammo_date'].date()
        self.mammo_last_update.data = p['mammo_last_update'].date()

        #spl stuff for subforms
        self.mammo_arch.from_bson(p['mammo_arch'])
        self.mammo_mass.from_bson(p['mammo_mass'])
        self.mammo_calcification.from_bson(p['mammo_calcification'])
