class Biopsy_dict():
    def __init__(self, key, value):
        self.key = key
        self.value = value


    def generate_choice(dict_list, dict_):
        choices_all = []
        for index in dict_list:
            choices = (index, dict_.get(index))
            choices_all = choices_all+ [(choices)]
        return tuple(choices_all)
    binary_list = [1,0]
    consent_stat_dict = {1:"Consent Taken",0:"No Consent"}
    consent_stat_choice = generate_choice(binary_list, consent_stat_dict)
    consent_form_dict = {1:"Consent form with sign ature present in folder",0:"Completed consent form not present in folder"}
    consent_form_choice = generate_choice(binary_list, consent_form_dict)
    biopsy_type_dict ={"direct":"Direct", "usg_guided":"USG Guided", "vab":"VAB", "truecut":"True-cut",
     "stereo":"Steriotactic", "other":"Other"}
    biopsy_type_list = ["direct","usg_guided", "vab", "truecut","stereo", "other"]
    biopsy_type_choice = generate_choice(biopsy_type_list, biopsy_type_dict)
    tumour_diagnosis_dict ={'benign':'Benign','dcis_micro':"Ductal carcinoma in situ(DCIS) with microinvasion",
                       'dcis_no_micro':"Ductal carcinoma in situ(DCIS) without microinvasion","lcs":
                       "Lobular Carcinoma in Situ (LCS)","idc":"Invasive Ductal Carcinoma (IDC)",'ilc':
                       "Invasive Lobular Carcinoma (ILC)",'gm':"Granulamatous Mastitis",'papc':"Papillary Carcinoma",
                       'phyc':"Phylloid Carcinoma",'imc':"Invasive Mammary Carcinoma",'ibc': "Invasive Breast Carcinoma"}
    tumour_diagnosis_list =['benign','dcis_micro','dcis_no_micro',"lcs","idc",'ilc','gm','papc','phyc','imc','ibc']
    tumour_diagnosis_choice = generate_choice(tumour_diagnosis_list, tumour_diagnosis_dict)
    biopsy_custody_pccm_dict = {1:"In PCCM Custody", 0:"Not in PCCM custody"}
    biopsy_custody_pccm_choice = generate_choice(binary_list, biopsy_custody_pccm_dict)
    tumour_grade_dict = {1:'Grade 1', 2: "Grade 2",3: "Grade 3"}
    tumour_grade_list = [1,2,3]
    tumour_grade_choice = generate_choice(tumour_grade_list,tumour_grade_dict)
    lymphovascular_emboli_dict = {1: "Lymphovascular Emboli Seen",0:"No Lymphovascular Emboli Seen"}
    lymphovascular_emboli_choice = generate_choice(binary_list, lymphovascular_emboli_dict)
    dcis_biopsy_dict = {1:"DCIS seen", 0: "DCIS not seen"}
    dcis_biopsy_choice = generate_choice(binary_list, dcis_biopsy_dict)
    tumour_er_dict = {1:"Positive", 0: "Negative"}
    tumour_er_choice = generate_choice(binary_list, tumour_er_dict)
    tumour_pr_dict = {1: "Positive", 0: "Negative"}
    tumour_pr_choice = generate_choice(binary_list, tumour_pr_dict)
    tumour_her2_dict = {2: "Positive", 1: "Equivocal", 0: "Negative"}
    tumour_her2_list = [2,1,0]
    tumour_her2_choice = generate_choice(tumour_her2_list, tumour_her2_dict)
    fnac_dict = {1:"Done", 2:"Not Done"}
    fnac_choice = generate_choice(binary_list, fnac_dict)
    fnac_location_dict = {"rb":"Right", "lb":"Left", "both":"Both"}
    fnac_location_list = {"rb", "lb", "both"}
    fnac_location_choice = generate_choice(fnac_location_list,fnac_location_dict)
    fnac_diagnosis_dict = {"normal":"Normal", "benign":"Benign", "malignant":"Malignant","other": "Other"}
    fnac_diagnosis_list = ["normal","benign","malignant","other"]
    fnac_diagnosis_choice = generate_choice(fnac_diagnosis_list, fnac_diagnosis_dict)