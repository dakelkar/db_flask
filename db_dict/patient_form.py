class PatientDict():
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

    gender ={"F":"Female",
             "M":"Male"}
    gender_choice = generate_choice(gender)

