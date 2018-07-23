from db_dict.common_dict import CommonDict

class BiopsyDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    consent_stat_dict = {'tbd':"To be filled","N":"No Consent", "Y":"Consent Taken"}
    consent_form_dict = {'tbd':"To be filled","Y":"Consent form with signature present in folder",
                         "N":"Completed consent form not present in folder"}
    biopsy_type_dict ={'tbd':"To be filled","direct":"Direct", "usg_guided":"USG Guided", "vab":"VAB",
                       "trucut":"Tru-cut", "stereo":"Steriotactic", "other":"Other"}
    tumour_diagnosis_dict ={'tbd':"To be filled",'benign':'Benign',
                            'dcis_micro':"Ductal carcinoma in situ(DCIS) with microinvasion",
                            'dcis_no_micro':"Ductal carcinoma in situ(DCIS) without microinvasion","lcs":
                            "Lobular Carcinoma in Situ (LCS)","idc":"Invasive Ductal Carcinoma (IDC)",'ilc':
                            "Invasive Lobular Carcinoma (ILC)",'gm':"Granulamatous Mastitis",'papc':"Papillary Carcinoma",
                            'phyc':"Phylloid Carcinoma",'imc':"Invasive Mammary Carcinoma",'ibc':
                            "Invasive Breast Carcinoma", 'other':'Other'}
    biopsy_custody_pccm_dict = {'tbd':"To be filled","Y":"In PCCM Custody", "N":"Not in PCCM custody"}
    tumour_grade_dict = {'tbd':"To be filled","1":'Grade 1', "2": "Grade 2","3": "Grade 3"}
    lymphovascular_emboli_dict = {'tbd':"To be filled","Y": "Lymphovascular Emboli Seen",
                                  "N":"No Lymphovascular Emboli Seen", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    dcis_biopsy_dict = {'tbd':"To be filled","Y":"DCIS seen", "N": "DCIS not seen", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    tumour_er_dict = {'tbd':"To be filled","pos":"Positive", "neg": "Negative", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    tumour_pr_dict = {'tbd':"To be filled","pos":"Positive", "neg": "Negative", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    tumour_her2_dict = {'tbd':"To be filled","pos": "Positive", "eqv": "Equivocal", "neg": "Negative",
                        'report': 'Not mentioned in Report', 'other': 'Other'}
    fnac_dict = {'tbd':"To be filled","Y":"Done", "N":"Not Done", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    fnac_location_dict = {'tbd':"To be filled", "rb":"Right", "lb":"Left", "both":"Both",
                          'report': 'Not mentioned in Report', 'other': 'Other'}
    fnac_diagnosis_dict = {'tbd':"To be filled", "normal":"Normal", "benign":"Benign", "malignant":"Malignant",
                           'report': 'Not mentioned in Report', 'other': 'Other'}

    consent_stat_choice = CommonDict.generate_choice(consent_stat_dict)
    consent_form_choice = CommonDict.generate_choice(consent_form_dict)
    biopsy_type_choice = CommonDict.generate_choice(biopsy_type_dict)
    tumour_diagnosis_choice = CommonDict.generate_choice(tumour_diagnosis_dict)
    biopsy_custody_pccm_choice = CommonDict.generate_choice(biopsy_custody_pccm_dict)
    tumour_grade_choice = CommonDict.generate_choice(tumour_grade_dict)
    lymphovascular_emboli_choice = CommonDict.generate_choice(lymphovascular_emboli_dict)
    dcis_biopsy_choice = CommonDict.generate_choice(dcis_biopsy_dict)
    tumour_er_choice = CommonDict.generate_choice(tumour_er_dict)
    tumour_pr_choice = CommonDict.generate_choice(tumour_pr_dict)
    tumour_her2_choice = CommonDict.generate_choice(tumour_her2_dict)
    fnac_choice = CommonDict.generate_choice(fnac_dict)
    fnac_location_choice = CommonDict.generate_choice(fnac_location_dict)
    fnac_diagnosis_choice = CommonDict.generate_choice(fnac_diagnosis_dict)