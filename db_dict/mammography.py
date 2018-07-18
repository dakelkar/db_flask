from db_dict.common_dict import CommonDict

class MammographyDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    mammo_location_dict = {'tbd':"To be filled",'pccm':"PCCM", 'out':"Outside",'other': "Other"}
    mammo_details_dict = {'tbd':"To be filled","N": "No","Y":"Yes",}
    mammo_breast_density_dict = {'tbd':"To be filled",'NA': "Information not available in this report",
                                 'a':"a. The breasts are almost entirely fatty", 'b': "b. There are scattered areas of "
                                 "fibroglandular density", 'c': "c. The breasts are heterogeneously dense, which may "
                                 "obscure small masses", 'd': "d. The breasts are extremely dense which lowers the "
                                 "sensitivity of mammography", 'other': "Other"}
    mammo_mass_depth_dict = {'tbd':"To be filled",'NA':"Not Present",'anterior':"Anterior",'middle':"Middle",
                             'posterior':"Posterior",
                             'other':"Other"}
    mammo_mass_shape_dict= {'tbd':"To be filled",'NA':"Not Present",'oval':"Oval", 'round':"Round", 'irreg':"Irregular",
                            'other':"Other"}
    mammo_mass_margin_dict = {'tbd':"To be filled",'NA':"Not Present",'circ':"Circumscribed", 'obsc':"Obscured",
                              'micro':"Microlobulated",
                              'ind':"Indistinct", 'spic':"Spiculated", 'other':"Other"}
    mammo_mass_density_dict = {'tbd':"To be filled",'NA':"Not Present",'high':"High density",'equal':"Equal density",
                               'low': "Low density",
                               'fat':"Fat-containing", 'other': "Other"}
    mammo_calcification_type_dict = {'tbd':"To be filled",'NA':"Not Present",'skin':"Skin",'vascular': "Vascular",
                                     'popcorn': "Coarse or 'Popcorn-like'", 'large': "Large Rod-like",
                                     'round':"Round and punctate", 'egg':"Eggshell or Rim",
                                     'dystrophic': "Dystrophic",'suture': "Suture",'amorphous': "Amorphous",'coarse':
                                     "Coarse Heterogeneous",'fine': "Fine Pleomorphic", 'fine_linear':
                                     "Fine Linear or Fine Linear Branching",'other': "Other"}
    mammo_calcification_diagnosis_dict = {'tbd':"To be filled",'NA':"Not Present",'benign':"Typically Benign",
                                          'suspicious':"Suspicious Morphology"}
    mammo_calcification_distribution_dict = {'tbd':"To be filled",'NA':"Not Present",'diffuse':"Diffuse",
                                             'regional':"Regional",
                                             'grouped':"Grouped",'linear':"Linear", 'segmental':"Segmental"}
    mammo_assym_type_dict = {'tbd':"To be filled",'NA':"Not Present",'assym':"Asymmetry", 'global':"Global asymmetry",
                             'focal':"Focal asymmetry", 'developing':"Developing asymmetry", 'other':"Other"}
    mammo_intra_mammary_lymph_nodes_dict = {'tbd':"To be filled","N":"Intra-mammary lymph nodes absent",
                                            "Y":"Intra-mammary lymph nodes present"}
    mammo_lesion_dict = {'tbd':"To be filled","N":"Skin Lesion not present", "Y":"Skin Lesion present"}
    abvs_diagnosis_dict = {'tbd':"To be filled",'follow_up':'Not Present in Report','normal':"Normal", 'benign':"Benign",
                          'suspicious':"Suspicious", 'cancer':"Diagnostic for Cancer"}
    sonomammo_tissue_dict = {'tbd':"To be filled", 'a': "a. Homogeneous background echotexture – fat",
                        'b':"b. Homogeneous background echotexture – fibroglandular",
                        'c': "c. Heterogeneous background echotexture", 'na':"Not available in Report",
                        'other': 'Other'}
    sonomammo_calc_dict = {'tbd':"To be filled",'no':"Not Present",'mass':"Calcifications in a mass", 'outside':"Calcifications outside of a mass",
                           'intra':"Intraductal calcifications", 'other':'Other'}
    sonomammo_skin_dict = {'tbd':"To be filled", 'na':"Not in Report", 'no':"No Skin Changes", 'thick':"Skin thickening", 'retract':"Skin retraction"}
    sonomammo_vascularity_dict = {'tbd':"To be filled",'na':"Not in Report", 'no':"Absent", 'internal':"Internal vascularity",
                                  'rim':"Vessels in rim", 'other':"Other"}
    sonomammo_elast_dict = {'tbd':"To be filled",'na':"Not in report", 'soft':"Soft", 'intermediate': "Intermediate", 'hard':"Hard",
                            'other':"Other"}
    sonomammo_hilum_dict  = {'tbd':"To be filled",'normal':'Normal Lymph Node','na':'Not in report','lost':"Lost", 'thin':"Thin",
                             'preserved':"Preserved", 'other':"Other"}

    sonomammo_lymph_ax_vasc_dict = {'tbd':"To be filled",'normal':'Normal Lymph Node','na':'Not in report', 'ventral':"Ventral",
                                    'peri':"Peripheral", 'other':"Other"}
    sonomammo_other_findings_dict = {'tbd':"To be filled",'no':"No other findings",'na':"Not mentioned in report",
                                     'cyst':"Simple cyst", 'microcyst':"Clustered microcysts",'complex':"Complicated cyst",
                                     'mass':"Mass in or on skin",'foriegn':"Foreign body including implants",
                                     'vasc':"Vascular abnormalities",'avm':"AVMs (arteriovenous malformations/pseudoaneurysms)",
                                     'mondor':"Mondor disease",'fluid':"Postsurgical ﬂuid collection",'fat':"Fat necrosis",
                                     'other':"Other"}
    sono_mass_shape_dict = {'tbd':"To be filled",'oval':"Oval", 'round':"Round", 'irregular':"Irregular", 'other':"Other"}
    sono_orientation_dict= {'tbd':"To be filled",'na':'Not in report','parallel':"Parallel", 'not':"Not parallel"}
    sono_mass_margin_dict = {'tbd':"To be filled", 'cirumc':"Circumscribed", 'not':"Not circumscribed",'indistinct':"Indistinct",
                             'angular':"Angular", 'micro':"Microlobulated", 'spiculated':"Spiculated"}
    sono_mass_echo_dict = {'tbd':"To be filled", 'anechoic':"Anechoic",'hyper':"Hyperechoic",'complex':"Complex cystic and solid",
                           'hypo':"Hypoechoic",'iso':"Isoechoic", 'hetero':"Heterogeneous", 'other':"Other"}
    sono_posterior_dict = {'tbd':"To be filled", 'no': "No posterior features", 'enhance':"Enhancement", 'shadow':"Shadowing",
                           'combinde':"Combined pattern", 'other':"Other"}
    mammo_location_choice = CommonDict.generate_choice(mammo_location_dict)
    mammo_details_choice = CommonDict.yes_no_choice
    mammo_breast_density_choice = CommonDict.generate_choice(mammo_breast_density_dict)
    mammo_mass_present_choice = CommonDict.yes_no_choice
    mammo_mass_location_right_breast_choice = CommonDict.breast_location_choice
    mammo_mass_location_left_breast_choice =  CommonDict.breast_location_choice
    mammo_mass_depth_choice = CommonDict.generate_choice(mammo_mass_depth_dict)
    mammo_mass_dist_choice = CommonDict.distance_from_nipple_choice
    mammo_mass_shape_choice = CommonDict.generate_choice(mammo_mass_shape_dict)
    mammo_mass_margin_choice = CommonDict.generate_choice(mammo_mass_margin_dict)
    mammo_mass_density_choice = CommonDict.generate_choice(mammo_mass_density_dict)
    mammo_calcification_present_choice = CommonDict.yes_no_choice
    mammo_calc_location_right_breast_choice =  CommonDict.breast_location_choice
    mammo_calc_location_left_breast_choice =  CommonDict.breast_location_choice
    mammo_calc_depth_choice = CommonDict.generate_choice(mammo_mass_depth_dict)
    mamo_calc_dist_choice = CommonDict.distance_from_nipple_choice
    mammo_calcification_type_choice = CommonDict.generate_choice(mammo_calcification_type_dict)
    mammo_calcification_diagnosis_choice = CommonDict.generate_choice( mammo_calcification_diagnosis_dict)
    mammo_arch_present_choice = CommonDict.yes_no_choice
    mammo_arch_location_right_breast_choice = CommonDict.breast_location_choice
    mammo_arch_location_left_breast_choice =  CommonDict.breast_location_choice
    mammo_arch_depth_choice = CommonDict.generate_choice(mammo_mass_depth_dict)
    mammo_arch_dist_choice = CommonDict.distance_from_nipple_choice
    mammo_assym_present_choice = CommonDict.yes_no_choice
    mammo_assym_location_right_breast_choice = CommonDict.breast_location_choice
    mammo_assym_location_left_breast_choice = CommonDict.breast_location_choice
    mammo_assym_depth_choice = CommonDict.generate_choice(mammo_mass_depth_dict)
    mammo_assym_type_right_breast_choice = CommonDict.generate_choice(mammo_assym_type_dict)
    mammo_assym_type_left_breast_choice = CommonDict.generate_choice(mammo_assym_type_dict)
    mammo_intra_mammary_lymph_nodes_choice = CommonDict.generate_choice(mammo_intra_mammary_lymph_nodes_dict)
    mammo_lesion_choice = CommonDict.generate_choice(mammo_lesion_dict)
    mammo_lesion_right_breast_choice =  CommonDict.breast_location_choice
    mammo_lesion_left_breast_choice =  CommonDict.breast_location_choice
    mammo_birad_choice =  CommonDict.birad_choice
    mammo_status_choice = CommonDict.form_status_choice
    abvs_diagnosis_choice = CommonDict.generate_choice(abvs_diagnosis_dict)
    sonomammo_tissue_choice = CommonDict.generate_choice(sonomammo_tissue_dict)
    sonomammo_calc_choice = CommonDict.generate_choice(sonomammo_calc_dict)
    sonomammo_skin_choice = CommonDict.generate_choice(sonomammo_skin_dict)
    sonomammo_vascularity_choice=CommonDict.generate_choice(sonomammo_vascularity_dict)
    sonomammo_elast_choice = CommonDict.generate_choice(sonomammo_elast_dict)
    sonomammo_hilum_choice = CommonDict.generate_choice(sonomammo_hilum_dict)
    sonomammo_lymph_ax_vasc_choice = CommonDict.generate_choice(sonomammo_lymph_ax_vasc_dict)
    sonomammo_other_findings_choice = CommonDict.generate_choice(sonomammo_other_findings_dict)
    sono_mass_shape_choice = CommonDict.generate_choice(sono_mass_shape_dict)
    sono_orientation_choice= CommonDict.generate_choice(sono_orientation_dict)
    sono_mass_margin_choice=CommonDict.generate_choice(sono_mass_margin_dict)
    sono_mass_echo_choice = CommonDict.generate_choice(sono_mass_echo_dict)
    sono_posterior_choice = CommonDict.generate_choice(sono_posterior_dict)