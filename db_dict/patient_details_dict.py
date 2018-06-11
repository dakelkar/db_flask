class PatientHistoryDict():
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
            choices_all = choices_all + [(choices)]
        return tuple(choices_all)

    gender_dict = {'f':"Female", 'm':"Male", 'other':"Other"}
    gender_choice = generate_choice(gender_dict)
    family_income_dict= {'tbd':'To be filled',"1":"0-2.5 Lacks","2":"2.5-5 Lacks", '3':"5-10 Lacks",
                         '4':">10 Lacks", "no":'Not Known','na':'Data not in report'}
    family_income_choice = generate_choice(family_income_dict)
    diet_dict = {'tbd':'To be Filled','veg':"Vegetarian", 'non-veg':"Non-Vegetarian", 'egg':"Ovo-Vegetarian", 'other':"Other"}
    diet_choice = generate_choice(diet_dict)
    tobacco_dict =  {'passive':'Passive','active':'Active', 'pa':'Passive and Active'}
    tobacco_choice = generate_choice(tobacco_dict)
    tobacco_type_passive_dict = {'no':'No exposure','home':"Home", 'work':"Work", 'commute':"Commute",
                                 'social':"Social Interactions", 'other':'Other'}
    tobacco_type_passive_choice = generate_choice(tobacco_type_passive_dict)
    tobacco_type_dict = {'no':'No exposure','cig':"Cigarette", 'beedi':"Beedi", 'gutka':"Gutkha", 'pan_masala':"Pan Masala",
                         'jarda':"Jarda/Maava", 'hookah':"Hookah", 'patch':"Nicotine Patch", 'mishri':"Mishri",
                         'other':"Other"}
    tobacco_type_choice = generate_choice(tobacco_type_dict)
    yes_no_dict = {'tbd': "To be filled", "N": "No", "Y": "Yes", 'other': "Other"}

    #family_repro details
    menstruation_dict = {'tbd': "To be filled",'pre':"Pre-menopausal", 'peri': "Peri-menopausal", 'post':"Post-Menopausal", 'other':"Other"}
    menstruation_type_dict = {'tbd': "To be filled",'regular':"Regular", 'irregular':"Irregular", 'other':"Other"}
    menstruation_choice = generate_choice(menstruation_dict)
    menstruation_type_choice=generate_choice(menstruation_type_dict)
    del_habits_dict = {'tbd':"To be filled",'na':'Not available in report',"N": "No", "other": "Yes"}
    del_habits_choice= generate_choice(del_habits_dict)
    symptoms_dict = {'pain':"Pain or tenderness", 'lumps':"Lumps", 'discharge':"Nipple Discharge", 'retract':"Nipple Retraction", 'dimpling':"Dimpling",
                     'discolour':"Discolouration", 'ulceration':"Ulceration", 'eczema':"Eczema", 'other': 'Other'}
    symptoms_choice = generate_choice(symptoms_dict)
    family_degree_dict = {'0':"Immediate Family", 'm':"Maternal Family", 'p':"Paternal Family"}
    family_degree_choice = generate_choice(family_degree_dict)
