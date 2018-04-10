class MammoDict():
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
    breast_location_dict = {'uoq':"UOQ", 'uiq':"UIQ",'ucq':"UCQ",'loq': "LOQ",'liq':"LIQ",'lcq':"LCQ",
                            'coq': "COQ",'ciq':"CIQ",'coo':"CCQ"}
    birad_dict = {"0":"0: Incomplete – Need Additional Imaging Evaluation","i":"I: Negative",'ii':"II: Benign",
                 'iii':"III: Probably Benign",'iv':"IV: Suspicious",'iva': "IVA: Low suspicion for malignancy",'ivb':
                 "IVB: Moderate suspicion for malignancy",'ivc': "IVC: High suspicion for malignancy",
                 'v':"V:  Highly Suggestive of Malignancy"}
    mammo_location_dict = {'pccm':"PCCM", 'out':"Outside",'other': "Other"}
    mammo_details_dict = {"Y", "Yes", "N", "No"}
    mammo_breast_density_dict = {'a':"a. The breasts are almost entirely fatty", 'b': "b. There are scattered areas of "
                           "fibroglandular density", 'c': "c. The breasts are heterogeneously dense, which may obscure"
                           " small masses", 'd': "d. The breasts are extremely dense which lowers the sensitivity " \
                           "of mammography"}
    mammo_mass_location_dict = {"Y", "Yes", "N", "No"}
    mammo_mass_depth_dict = {'anterior':"Anterior",'middle':"Middle",'posterior':"Posterior",'other':"Other"}
    mammo_mass_dist_dict = {'<.5': "<0.5 cm", '>0.5': ">0.5 cm", 'other':"Other"}
    mammo_mass_shape_dict= {'oval':"Oval", 'round':"Round", 'irreg':"Irregular", 'other':"Other"}
    mammo_mass_margin_dict = {'circ':"Circumscribed", 'obsc':"Obscured", 'micro':"Microlobulated", 'ind':"Indistinct",
                              'spic':"Spiculated", 'other':"Other"}
    mammo_mass_density_dict = {'high':"High density",'equal':"Equal density",'low': "Low density",'fat':"Fat-containing",
                               'other': "Other"}
        #to add mass data here
    mammo_calcification_dict = {"Y", "Yes", "N", "No"}
    mammo_calcification_type_dict = {'skin':"Skin",'vascular': "Vascular",'popcorn': "Coarse or 'Popcorn-like'",
                                     'large': "Large Rod-like", 'round':"Round and punctate", 'egg':"Eggshell or Rim",
                                     'dystrophic': "Dystrophic",'suture': "Suture",'amorphous': "Amorphous",'coarse':
                                     "Coarse Heterogeneous",'fine': "Fine Pleomorphic", 'fine_linear':
                                     "Fine Linear or Fine Linear Branching",'other': "Other"}
    mammo_calcification_diagnosis_dict = {'benign':"Typically Benign", 'suspicious':"Suspicious Morphology"}
    mammo_calcification_distribution_dict = {'diffuse':"Diffuse",'regional':"Regional", 'grouped':"Grouped",'linear':"Linear",
                                             'segmental':"Segmental"}
    # to add calc data here
    # to add arch dist data here
    mammo_intra_mammary_lymph_nodes_dict = {"Y", "Intra-mammary lymph nodes present", "N", "Intra-mammary lymph nodes absent"}
    mammo_lesion_dict = {"Y", "Skin Lesion present", "N", "Skin Lesion not present"}
    #mammo_lesion_right_breast = {}
    #mammo_lesion_left_breast = {}
    #mammo_birad =

    #choice
    mammo_location_choice = generate_choice(mammo_location_dict)
    mammo_details_choice = generate_choice(mammo_details_dict)
    mammo_breast_density_choice = generate_choice(mammo_breast_density_dict)
    mammo_mass_location_choice = generate_choice(mammo_mass_location_dict)
    mammo_mass_location_right_breast_choice = generate_choice(breast_location_dict)
    mammo_mass_location_left_breast_choice = generate_choice(breast_location_dict)
    mammo_mass_depth_choice = generate_choice(mammo_mass_depth_dict)
    mammo_mass_dist_choice = generate_choice(mammo_mass_dist_dict)
    mammo_mass_shape_choice = generate_choice(mammo_mass_shape_dict)
    mammo_mass_margin_choice = generate_choice(mammo_mass_margin_dict)
    mammo_mass_density_choice = generate_choice(mammo_mass_density_dict)
    mammo_calcification_choicet = generate_choice(mammo_calcification_dict)
    mammo_calc_location_right_breast_choice = generate_choice(breast_location_dict)
    mammo_calc_location_left_breast_choice = generate_choice(breast_location_dict)
    mammo_calc_depth_choice = generate_choice(mammo_mass_depth_dict)
    mamo_calc_dist_choice = generate_choice(mammo_mass_dist_dict)
    mammo_calcification_type_choice = generate_choice(mammo_calcification_type_dict)
    mammo_calcification_diagnosis_choice = generate_choice( mammo_calcification_diagnosis_dict)
    # to add arch dist data here
    mammo_intra_mammary_lymph_nodes_choice = generate_choice(mammo_intra_mammary_lymph_nodes_dict)
    mammo_lesion_choice = generate_choice(mammo_lesion_dict)
    mammo_lesion_right_breast_choice = generate_choice(breast_location_dict)
    mammo_lesion_left_breast_choice = generate_choice(breast_location_dict)
    mammo_birad_choice =  generate_choice(birad_dict)