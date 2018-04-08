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

    biopsy_type ={"direct":"Direct", "usg_guided":"USG Guided", "vab":"VAB", "truecut":"True-cut",
     "stereo":"Steriotactic", "other":"Other"}
    biopsy_type_list = ["direct","usg_guided", "vab", "truecut","stereo", "other"]
    biopsy_type_choice = generate_choice(biopsy_type_list, biopsy_type)
