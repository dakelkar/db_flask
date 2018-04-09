class BiopsyDict():
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
    consent_stat_dict = {"Y":"Consent Taken","N":"No Consent"}
    consent_stat_choice = generate_choice(consent_stat_dict)
    consent_form_dict = {"Y":"Consent form with signature present in folder","N":"Completed consent form not present in folder"}
    consent_form_choice = generate_choice(consent_form_dict)
    biopsy_type_dict ={"direct":"Direct", "usg_guided":"USG Guided", "vab":"VAB", "truecut":"True-cut",
     "stereo":"Steriotactic", "other":"Other"}
    biopsy_type_choice = generate_choice(biopsy_type_dict)
    tumour_diagnosis_dict ={'benign':'Benign','dcis_micro':"Ductal carcinoma in situ(DCIS) with microinvasion",
                       'dcis_no_micro':"Ductal carcinoma in situ(DCIS) without microinvasion","lcs":
                       "Lobular Carcinoma in Situ (LCS)","idc":"Invasive Ductal Carcinoma (IDC)",'ilc':
                       "Invasive Lobular Carcinoma (ILC)",'gm':"Granulamatous Mastitis",'papc':"Papillary Carcinoma",
                       'phyc':"Phylloid Carcinoma",'imc':"Invasive Mammary Carcinoma",'ibc': "Invasive Breast Carcinoma"}
    tumour_diagnosis_choice = generate_choice(tumour_diagnosis_dict)
    biopsy_custody_pccm_dict = {"Y":"In PCCM Custody", "N":"Not in PCCM custody"}
    biopsy_custody_pccm_choice = generate_choice(biopsy_custody_pccm_dict)
    tumour_grade_dict = {"1":'Grade 1', "2": "Grade 2","3": "Grade 3"}
    tumour_grade_choice = generate_choice(tumour_grade_dict)
    lymphovascular_emboli_dict = {"Y": "Lymphovascular Emboli Seen","N":"No Lymphovascular Emboli Seen"}
    lymphovascular_emboli_choice = generate_choice(lymphovascular_emboli_dict)
    dcis_biopsy_dict = {"Y":"DCIS seen", "N": "DCIS not seen"}
    dcis_biopsy_choice = generate_choice(dcis_biopsy_dict)
    tumour_er_dict = {"pos":"Positive", "neg": "Negative"}
    tumour_er_choice = generate_choice(tumour_er_dict)
    tumour_pr_dict = {"pos":"Positive", "neg": "Negative"}
    tumour_pr_choice = generate_choice(tumour_pr_dict)
    tumour_her2_dict = {"pos": "Positive", "eqv": "Equivocal", "neg": "Negative"}
    tumour_her2_choice = generate_choice(tumour_her2_dict)
    fnac_dict = {"Y":"Done", "N":"Not Done"}
    fnac_choice = generate_choice(fnac_dict)
    fnac_location_dict = {"rb":"Right", "lb":"Left", "both":"Both"}
    fnac_location_choice = generate_choice(fnac_location_dict)
    fnac_diagnosis_dict = {"normal":"Normal", "benign":"Benign", "malignant":"Malignant","other": "Other"}
    fnac_diagnosis_choice = generate_choice(fnac_diagnosis_dict)