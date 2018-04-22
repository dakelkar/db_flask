from db_dict.common_dict import CommonDict
class MammographyDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value


    def generate_choice(dict_):
        choices_all = []
        keys = []
        for key in dict_:
            keys.append(key)
        for index in keys:
            choices = (index, dict_.get(index))
            choices_all = choices_all+ [(choices)]
        return tuple(choices_all)

    mammo_location_dict = {'tbd':"To be filled",'pccm':"PCCM", 'out':"Outside",'other': "Other"}
    mammo_details_dict = {'tbd':"To be filled","N": "No","Y":"Yes",}
    mammo_breast_density_dict = {'tbd':"To be filled",'NA': "Information not available in this report",
                                 'a':"a. The breasts are almost entirely fatty", 'b': "b. There are scattered areas of "
                                 "fibroglandular density", 'c': "c. The breasts are heterogeneously dense, which may "
                                 "obscure small masses", 'd': "d. The breasts are extremely dense which lowers the "
                                 "sensitivity of mammography"}
    #this data has to actually repeat over n times n being mass number
    mammo_mass_depth_dict = {'tbd':"To be filled",'NA':"Not Present",'anterior':"Anterior",'middle':"Middle",'posterior':"Posterior",
                             'other':"Other"}
    mammo_mass_shape_dict= {'tbd':"To be filled",'NA':"Not Present",'oval':"Oval", 'round':"Round", 'irreg':"Irregular", 'other':"Other"}
    mammo_mass_margin_dict = {'tbd':"To be filled",'NA':"Not Present",'circ':"Circumscribed", 'obsc':"Obscured", 'micro':"Microlobulated",
                              'ind':"Indistinct", 'spic':"Spiculated", 'other':"Other"}
    mammo_mass_density_dict = {'tbd':"To be filled",'NA':"Not Present",'high':"High density",'equal':"Equal density",'low': "Low density",
                               'fat':"Fat-containing", 'other': "Other"}
    mammo_calcification_type_dict = {'tbd':"To be filled",'NA':"Not Present",'skin':"Skin",'vascular': "Vascular",
                                     'popcorn': "Coarse or 'Popcorn-like'", 'large': "Large Rod-like",
                                     'round':"Round and punctate", 'egg':"Eggshell or Rim",
                                     'dystrophic': "Dystrophic",'suture': "Suture",'amorphous': "Amorphous",'coarse':
                                     "Coarse Heterogeneous",'fine': "Fine Pleomorphic", 'fine_linear':
                                     "Fine Linear or Fine Linear Branching",'other': "Other"}
    mammo_calcification_diagnosis_dict = {'tbd':"To be filled",'NA':"Not Present",'benign':"Typically Benign",
                                          'suspicious':"Suspicious Morphology"}
    mammo_calcification_distribution_dict = {'tbd':"To be filled",'NA':"Not Present",'diffuse':"Diffuse",'regional':"Regional",
                                             'grouped':"Grouped",'linear':"Linear", 'segmental':"Segmental"}
    mammo_assym_type_dict = {'tbd':"To be filled",'NA':"Not Present",'assym':"Asymmetry", 'global':"Global asymmetry",
                             'focal':"Focal asymmetry", 'developing':"Developing asymmetry", 'other':"Other"}
    mammo_intra_mammary_lymph_nodes_dict = {'tbd':"To be filled","N":"Intra-mammary lymph nodes absent",
                                            "Y":"Intra-mammary lymph nodes present"}
    mammo_lesion_dict = {'tbd':"To be filled","N":"Skin Lesion not present", "Y":"Skin Lesion present"}


    mammo_location_choice = generate_choice(mammo_location_dict)
    mammo_details_choice = CommonDict.yes_no_choice
    mammo_breast_density_choice = generate_choice(mammo_breast_density_dict)
    mammo_mass_present_choice = CommonDict.yes_no_choice
    mammo_mass_location_right_breast_choice = CommonDict.breast_location_choice
    mammo_mass_location_left_breast_choice =  CommonDict.breast_location_choice
    mammo_mass_depth_choice = generate_choice(mammo_mass_depth_dict)
    mammo_mass_dist_choice = CommonDict.distance_from_nipple_choice
    mammo_mass_shape_choice = generate_choice(mammo_mass_shape_dict)
    mammo_mass_margin_choice = generate_choice(mammo_mass_margin_dict)
    mammo_mass_density_choice = generate_choice(mammo_mass_density_dict)
    mammo_calcification_present_choice = CommonDict.yes_no_choice
    mammo_calc_location_right_breast_choice =  CommonDict.breast_location_choice
    mammo_calc_location_left_breast_choice =  CommonDict.breast_location_choice
    mammo_calc_depth_choice = generate_choice(mammo_mass_depth_dict)
    mamo_calc_dist_choice = CommonDict.distance_from_nipple_choice
    mammo_calcification_type_choice = generate_choice(mammo_calcification_type_dict)
    mammo_calcification_diagnosis_choice = generate_choice( mammo_calcification_diagnosis_dict)
    mammo_arch_present_choice = CommonDict.yes_no_choice
    mammo_arch_location_right_breast_choice = CommonDict.breast_location_choice
    mammo_arch_location_left_breast_choice =  CommonDict.breast_location_choice
    mammo_arch_depth_choice = generate_choice(mammo_mass_depth_dict)
    mammo_arch_dist_choice = CommonDict.distance_from_nipple_choice
    mammo_assym_present_choice = CommonDict.yes_no_choice
    mammo_assym_location_right_breast_choice = CommonDict.breast_location_choice
    mammo_assym_location_left_breast_choice = CommonDict.breast_location_choice
    mammo_assym_depth_choice = generate_choice(mammo_mass_depth_dict)
    mammo_assym_type_right_breast_choice = generate_choice(mammo_assym_type_dict)
    mammo_assym_type_left_breast_choice = generate_choice(mammo_assym_type_dict)
    mammo_intra_mammary_lymph_nodes_choice = generate_choice(mammo_intra_mammary_lymph_nodes_dict)
    mammo_lesion_choice = generate_choice(mammo_lesion_dict)
    mammo_lesion_right_breast_choice =  CommonDict.breast_location_choice
    mammo_lesion_left_breast_choice =  CommonDict.breast_location_choice
    mammo_asso_feature_skin_retraction_choice  = CommonDict.absent_present_choice
    mammo_asso_feature_nipple_retraction_choice  = CommonDict.absent_present_choice
    mammo_asso_feature_skin_thickening_choice  = CommonDict.absent_present_choice
    mammo_asso_feature_trabecular_thickening_choice  = CommonDict.absent_present_choice
    mammo_asso_feature_axillary_adenopathy_choice  = CommonDict.absent_present_choice
    mammo_asso_feature_architectural_distortion_choice = CommonDict.absent_present_choice
    mammo_asso_feature_calicifications_choice = CommonDict.absent_present_choice
    mammo_birad_choice =  CommonDict.birad_choice
    mammo_status_choice = CommonDict.form_status_choice