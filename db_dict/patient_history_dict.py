from db_dict.common_dict import CommonDict

class PatientHistoryDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    diet_dict = {'veg':"Vegetarian", 'non-veg':"Non-Vegetarian", 'egg':"Ovo-Vegetarian", 'other':"Other"}
    diet_choice = CommonDict.generate_choice(diet_dict)
    tobacco_dict =  {'no':'No exposure', 'passive':'Passive','active':'Active', 'pa':'Passive and Active'}
    tobacco_choice = CommonDict.generate_choice(tobacco_dict)
    tobacco_type_passive_dict = {'no':'No exposure','home':"Home", 'work':"Work", 'commute':"Commute",
                                 'social':"Social Interactions", 'other':'Other'}
    tobacco_type_passive_choice = CommonDict.generate_choice(tobacco_type_passive_dict)
    tobacco_type_dict = {'no':'No exposure','cig':"Cigarette", 'beedi':"Beedi", 'gutka':"Gutkha", 'pan_masala':"Pan Masala",
                         'jarda':"Jarda/Maava", 'hookah':"Hookah", 'patch':"Nicotine Patch", 'mishri':"Mishri",
                         'other':"Other"}
    tobacco_type_choice = CommonDict.generate_choice(tobacco_type_dict)
    yes_no_dict = {'tbd': "To be filled", "N": "No", "Y": "Yes", 'other': "Other"}
