from db_dict.common_dict import CommonDict

class ChemoDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    place_nact_dict = {'tbd':"To be filled",'pccm':"At PCCM",'outside': "Outside",
                       'tbd_':"Not Certain, requires follow-up"}
    details_nact_dict = {'tbd':"To be filled","Y":"Details Available","tbd_":"Follow-up required"}
    drugs_dict = {'tbd':"To be filled",'5fu':"5-FluoroUracil",
                  'anthra':"Anthracycline",
                  'anstro':"Anastrozole",
                  'carbop':"Carboplatin",
                  'cisp':"Cisplatin",
                  'cyclo':"Cyclophosphamide",
                  'doci':"Docitaxel",
                  'doxo':"Doxorubicin",
                  'epi':'Epirubicin',
                  'exe':"Exemestane",
                  'fulv':"Fulvestrant",
                  'gem':"Gemcitabine",
                  'gos':"Goserelin",
                  'herc':"Herceptin(Trastuzumab)",
                  'letro':"Letrozole",
                  'leupro':"Leuprolide",
                  'pacli':"Paclitaxel",
                  'tamoxi':"Tamoxifen",
                  'other':"Other"}
    toxic_side_effects_dict = {'tbd':"To be filled",'fever': "Fever",
                                'aneamia': "Anaemia",
                                'neutro': "Neutropenia",
                                'breath': "Breathlessness",
                                'vom': "Vomiting",
                                'nausea': "Nausea",
                                'loose': "Loose Motions",
                                'cough': "Cough",
                                'ui': "Urinary Infections",
                                'cardio': "Cardiotoxicity",
                                'neuro': "Neuropathy",
                                'other': "Other"}
    toxic_side_effects_grade_dict = {'tbd':"To be filled",'mild':"Mild", 'moderate':"Moderate", 'severe':"Severe",
                                     'other':"Other"}
    tumour_response_nact_dict = {'tbd':"To be filled",'partial':"Partial", 'complete':"Complete", 'no':"No Effect",
                              'other':"Other"}
    nact_change_dict = {'tbd':"To be filled", 'no':"No change",'change_tox':"NACT regime changed due to toxicity",
                        'stop_tox': "NACT stopped  due to toxicity", 'change_other': "NACT changed due to other reasons",
                        'stop_other': "NACT stopped due to other reasons"}
    trast_regime_nact_dict = {'tbd':"To be filled",'seq':"Sequential", 'con':"Concurrent", 'other':"Other"}
    reason_incomplete_chemo_dict = {'tbd':"To be filled",'tox':"Toxicity",
                              'reluctance': "Reluctance of patient",
                              'prog': "Progression on chemotherapy",
                              'doctor': "Advised by treating doctor",
                              'death_tox': "Death due to toxicity",
                              'death_disease': "Death due to progressive disease",
                              'centre': "Preferred treatment at another centre",
                              'death': "Death due to unrelated cause",
                              'price': "Patient was unable to afford treatment", 'other': 'Other'}
    menopause_dict = {'tbd':"To be filled",'pre': "Pre-menopausal",'peri': "Peri-menopausal",'post': "Post-Menopausal",
                      'other': "Other"}
    ovary_status_dict = {'tbd':"To be filled",'menses': "Menses ongoing",'ameno_on': "Amenorrhoea on Chemo",
                         'ameno_post': "Amenorrhoea post Chemotherapy", 'other':'Other'}
    place_nact_choice = CommonDict.generate_choice(place_nact_dict)
    details_nact_choice = CommonDict.generate_choice(details_nact_dict)
    drugs_choice = CommonDict.generate_choice(drugs_dict)
    toxic_side_effects_choice = CommonDict.generate_choice(toxic_side_effects_dict)
    toxic_side_effects_grade_choice = CommonDict.generate_choice(toxic_side_effects_grade_dict)
    tumour_response_choice = CommonDict.generate_choice(tumour_response_nact_dict)
    nact_change_choice = CommonDict.generate_choice(nact_change_dict)
    trast_regime_nact_choice = CommonDict.generate_choice(trast_regime_nact_dict)
    reason_incomplete_nact_choice = CommonDict.generate_choice(reason_incomplete_chemo_dict)
    menopause_choice = CommonDict.generate_choice(menopause_dict)
    ovary_status_choice = CommonDict.generate_choice(ovary_status_dict)