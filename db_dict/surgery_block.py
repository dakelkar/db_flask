from db_dict.common_dict import CommonDict

class SurgeryDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    consent_stat_dict = {'tbd':"To be filled","N":"No Consent", "Y":"Consent Taken"}
    consent_form_dict = {'tbd':"To be filled","Y":"Consent form with signature present in folder",
                         "N":"Completed consent form not present in folder"}
    biopsy_type_dict ={'tbd':"To be filled","direct":"Direct", "usg_guided":"USG Guided", "vab":"VAB",
                       "truecut":"True-cut", "stereo":"Steriotactic", "other":"Other"}
    tumour_diagnosis_dict ={'tbd':"To be filled",'benign':'Benign',
                            'dcis_micro':"Ductal carcinoma in situ(DCIS) with microinvasion",
                            'dcis_no_micro':"Ductal carcinoma in situ(DCIS) without microinvasion","lcs":
                            "Lobular Carcinoma in Situ (LCS)","idc":"Invasive Ductal Carcinoma (IDC)",'ilc':
                            "Invasive Lobular Carcinoma (ILC)",'gm':"Granulamatous Mastitis",'papc':"Papillary Carcinoma",
                            'phyc':"Phylloid Carcinoma",'imc':"Invasive Mammary Carcinoma",'ibc':
                            "Invasive Breast Carcinoma", 'other':'Other'}
    biopsy_custody_pccm_dict = {'tbd':"To be filled","Y":"In PCCM Custody", "N":"Not in PCCM custody"}
    surgery_type_dict = {'bcs': "Breast Conservation Surgery (BCS)",'tm': "Therapeutic Mammoplasty",
                         'rm': "Reduction Mammoplasty",'reconstruction': "Reconstruction",
                         'reco-mastectomy': "Reconstruction: Mastectomy", 'reco:mrm': "Modified Radical Mastectomy",
                         'reco:implant': "Implant", 'wle':"Wide Local Excision", 'other': "Other", }
    tumour_grade_dict = {'tbd':"To be filled","1":'Grade 1', "2": "Grade 2","3": "Grade 3"}
    margin_dict  ={'involved': "Margins Involved", 'free': "Margins Free",'other': 'Other'}
    dcis_dict = {'tbd':"To be filled", "N": "DCIS not seen", 'micro':"Microinvasion",  'macro': "Macroinvasion",
                 'report': 'Not mentioned in Report','other': 'Other'}
    surgery_diagnosis_dict = {'tbd': "To be filled", 'dcis': "Ductal carcinoma in situ",
                             "lcs": "Lobular Carcinoma in Situ (LCS)", "idc": "Invasive Ductal Carcinoma (IDC)",
                             'ilc': "Invasive Lobular Carcinoma (ILC)", 'gm': "Granulamatous Mastitis",
                             'papc': "Papillary Carcinoma", 'phyc': "Phylloid Carcinoma",
                             'imc': "Invasive Mammary Carcinoma", 'ibc': "Invasive Breast Carcinoma", 'other': 'Other'}
    tumour_her2_dict = {'tbd':"To be filled","pos": "Positive", "eqv": "Equivocal", "neg": "Negative",
                        'report': 'Not mentioned in Report', 'other': 'Other'}
    pt_status_dict = {'tbd':"To be filled",'is': "is", '0': "0", '1': "1", '2': "2", '3': "3", '4': "4", 'other': "Other"}
    pn_status_dict = {'tbd': "To be filled",'0': "0", '1': "1", '2': "2", '3': "3", '4': "4", 'other': "Other"}
    pm_status_dict = {'tbd': "To be filled",'0': "0", '1': "1", '2': "2", '3': "3", 'other': "Other"}
    clinical_stage_dict = {'1a':'IA','1b':'IB','2a':'IIA','2b': 'IIB','3a': 'IIIA','3b': 'IIIB','3c': 'IIIC','4': 'IV' }
    consent_stat_choice = CommonDict.generate_choice(consent_stat_dict)
    consent_form_choice = CommonDict.generate_choice(consent_form_dict)
    biopsy_type_choice = CommonDict.generate_choice(biopsy_type_dict)
    tumour_diagnosis_choice = CommonDict.generate_choice(tumour_diagnosis_dict)
    biopsy_custody_pccm_choice = CommonDict.generate_choice(biopsy_custody_pccm_dict)
    tumour_grade_choice = CommonDict.generate_choice(tumour_grade_dict)
    tumour_her2_choice = CommonDict.generate_choice(tumour_her2_dict)
    pt_status_choice = CommonDict.generate_choice(pt_status_dict)
    pn_status_choice = CommonDict.generate_choice(pn_status_dict)
    pm_status_choice = CommonDict.generate_choice(pm_status_dict)
    surgery_diagnosis_choice = CommonDict.generate_choice(surgery_diagnosis_dict)
    dcis_choice = CommonDict.generate_choice(dcis_dict)
    margin_choice = CommonDict.generate_choice(margin_dict)
    surgery_type_choice = CommonDict.generate_choice(surgery_type_dict)
    clinical_stage_choice = CommonDict.generate_choice(clinical_stage_dict)