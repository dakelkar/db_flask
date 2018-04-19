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
    breast_location_dict = {'tbd':"To be filled",'NA': "Not present in this breast", 'uoq':"UOQ", 'uiq':"UIQ",'ucq':"UCQ",'loq': "LOQ",
                            'liq':"LIQ",'lcq':"LCQ", 'coq': "COQ",'ciq':"CIQ",'coo':"CCQ"}
    birad_dict = {'tbd':"To be filled",'NA': "Information not available in this report","0":"0: Incomplete – Need Additional Imaging Evaluation",
                  "i":"I: Negative",'ii':"II: Benign", 'iii':"III: Probably Benign",'iv':"IV: Suspicious",
                  'iva': "IVA: Low suspicion for malignancy",'ivb': "IVB: Moderate suspicion for malignancy",
                  'ivc': "IVC: High suspicion for malignancy",'v':"V:  Highly Suggestive of Malignancy"}
    distance_from_nipple_dict = {'tbd':"To be filled",'NA':"Not Present", '<.5': "<0.5 cm", '>0.5': ">0.5 cm", 'other': "Other"}
    yes_no_dict = {'tbd':"To be filled","N": "No", "Y": "Yes"}
    absent_present_dict = {'tbd':"To be filled",'absent':'Absent', 'present':'Present', 'other':"Other"}
    breast_location_choice = generate_choice(breast_location_dict)
    birad_choice = generate_choice(birad_dict)
    yes_no_choice = generate_choice(yes_no_dict)
    distance_from_nipple_choice = generate_choice(distance_from_nipple_dict)
    absent_present_choice = generate_choice(absent_present_dict)
    form_status_choice = generate_choice(form_status_dict)