class CommonDict():
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

    form_status_dict = {'Empty':"Empty", 'All fields are not filled':"All fields are not filled",
                        'Requires additional data from specialist':"Requires additional data from specialist",
                        "Data to be obtained from Patient":'Data to be obtained from Patient','Complete':"Complete"}
    breast_location_dict = {'tbd':"To be filled",'NA': "Not present in this breast", 'uoq':"UOQ", 'uiq':"UIQ",
                            'ucq':"UCQ",'loq': "LOQ", 'liq':"LIQ",'lcq':"LCQ", 'coq': "COQ",'ciq':"CIQ",'ccq':"CCQ",
                            'other': "Other"}
    birad_dict = {'tbd':"To be filled",'NA': "Information not available in this report","0":"0: Incomplete – Need Additional Imaging Evaluation",
                  "i":"I: Negative",'ii':"II: Benign", 'iii':"III: Probably Benign",'iv':"IV: Suspicious",
                  'iva': "IVA: Low suspicion for malignancy",'ivb': "IVB: Moderate suspicion for malignancy",
                  'ivc': "IVC: High suspicion for malignancy",'v':"V:  Highly Suggestive of Malignancy", 'other': "Other"}
    distance_from_nipple_dict = {'tbd':"To be filled",'NA':"Not Present", '<.5': "<0.5 cm", '>0.5': ">0.5 cm", 'other': "Other"}
    yes_no_dict = {'tbd':"To be filled","N": "No", "Y": "Yes", 'other': "Other"}
    yes_no_other_dict = {'tbd': "To be filled", "other": "Yes", "N": "No", 'na':'Data not available'}
    form_yes_no_dict ={'tbd':"To be filled",'na':'Not available in report',"N": "No", "Y": "Yes"}

    absent_present_dict = {'tbd':"To be filled",'absent':'Absent', 'present':'Present', 'na': "Not mentioned in report",
                           'other':"Other"}
    folder_status_dict = {'Empty':"Empty", 'All fields are not filled':"All fields are not filled",
                        'Requires additional data from specialist':"Requires additional data from specialist",
                        "Requires Follow up":'Requires Follow up','Complete':"Complete"}
    breast_dict ={'tbd':"To be filled",'no':"Not present",'right': "Right Breast", 'left':"Left Breast",
                  'both':"Both Breast", 'other':"Other"}
    normal_abnormal_dict = {'tbd':"To be filled",'no':'Not Present in Report','normal':"Normal", 'abnormal':"Abnormal"}
    postive_negative_dict = {'tbd':"To be filled","pos":"Positive", "neg": "Negative", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    breast_location_choice = generate_choice(breast_location_dict)
    birad_choice = generate_choice(birad_dict)
    yes_no_choice = generate_choice(yes_no_dict)
    distance_from_nipple_choice = generate_choice(distance_from_nipple_dict)
    absent_present_choice = generate_choice(absent_present_dict)
    form_status_choice = generate_choice(form_status_dict)
    folder_status_choice = generate_choice(folder_status_dict)
    form_yes_no_choice = generate_choice(form_yes_no_dict)
    breast_choice = generate_choice(breast_dict)
    normal_abnormal_choice = generate_choice(normal_abnormal_dict)
    postive_negative_choice = generate_choice(postive_negative_dict)
    yes_no_other_choice = generate_choice(yes_no_other_dict)