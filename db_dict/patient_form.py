class Patient_dict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def generate_choice(dict_list, dict_):
        choices_all = []
        for index in dict_list:
            choices = (index, dict_.get(index))
            choices_all = choices_all + [(choices)]
        return tuple(choices_all)

    gender ={"F":"Female",
             "M":"Male"}
    gender_list = ["F", "M"]
    gender_choice = generate_choice(gender_list, gender)

