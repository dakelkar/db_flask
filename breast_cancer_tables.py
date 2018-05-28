import modules.pccm_names as pccm_names
from modules.ask_y_n_statement import get_rb_lb, ask_y_n, ask_option, join_lists
from sql.add_update_sql import update_multiple, insert

def physical_activity_table(conn, cursor, file_number):
    table_act = "Physical_Activity"
    columns = ", ".join(pccm_names.names_info("phys_act_table"))
    add_act = True
    type_phys_list, freq_phys_list = [], []
    while add_act:
        type_phys_act = input("Type of physical activity: ")
        type_phys_list.append(type_phys_act)
        freq_phys_act = input("Frequency of physical activity: ")
        freq_phys_list.append(freq_phys_act)
        data = file_number, type_phys_act, freq_phys_act
        insert(conn, cursor, table_act, columns, data)
        add_act = ask_y_n("Add further activities?")
    type_phys = '; '.join(type_phys_list)
    freq_phys = '; '.join(freq_phys_list)
    return (type_phys, freq_phys)

def cancer_table(conn, cursor, file_number):
    table_cancer = "Previous_Cancer_History"
    type_of_cancer_list = []
    year_diagnosis_list = []
    treat_all = []
    type_all = []
    duration_all = []
    data_return = []
    add_cancer = True
    while add_cancer:
        type_of_cancer = input("Type of Cancer: ")
        type_of_cancer_list.append(type_of_cancer)
        year_diagnosis = input("Year of diagnosis: ")
        year_diagnosis_list.append(year_diagnosis)
        col = ("File_number, Type_Cancer, Year_diagnosis")
        data = file_number, type_of_cancer, year_diagnosis
        insert(conn, cursor, table_cancer, col, data)
        print ("Please enter the type of treatment used: ")
        treatment = ["Surgery", "Radiation", "Chemotherapy", "Hormone", "Alternative", "HomeRemedy"]
        treat_list = []
        type_list = []
        duration_list = []
        treated, type, duration = ("NA", )*3
        for index in treatment:
            treat = ask_y_n(index)
            if treat:
                treat_list.append(index)
                type_treat = input("Type of " + index)
                type_list.append(type_treat)
                duration_treat = input("Duration of " + index)
                duration_list.append(duration_treat)
                data = index, type_treat, duration_treat
                columns = [index, ("Type_" + index), ("Duration_" + index)]
                treated = "; ".join(treat_list)
                type = "; ".join(type_list)
                duration = "; ".join(duration_list)
                update_multiple(conn, cursor, table_cancer, columns, file_number, data)
            elif not treat:
                index_no = "No " + index
                type_treat, duration_treat = ("NA",) * 2
                data = index_no, type_treat, duration_treat
                columns = [index, ("Type_" + index), ("Duration_" + index)]
                update_multiple(conn, cursor, table_cancer, columns, file_number, data)
        treat_all.append(treated)
        type_all.append(type)
        duration_all.append(duration)
        add_cancer = ask_y_n("Additional cancer history")
    all_data = [type_of_cancer_list, year_diagnosis_list, treat_all, type_all, duration_all]
    for index in all_data:
        data_joint = "|".join(index)
        data_return.append(data_joint)
    return tuple(data_return)


def nut_supp_table(conn, cursor, file_number):
    type_nut_list, quant_nut_list, duration_nut_list = [], [], []
    add_supp = True
    table_nut = "Nutritional_Supplements"
    columns = ", ".join(pccm_names.names_info("nut_sup"))
    while add_supp:
        nut_supplements_type = input("Type of nutritional supplements taken: ")
        type_nut_list.append(nut_supplements_type)
        nut_supplements_quant = input("Quantity of nutritional supplements taken per day: ")
        quant_nut_list.append(nut_supplements_quant)
        nut_supplements_duration = input("Duration of nutritional supplements use: ")
        duration_nut_list.append(nut_supplements_duration)
        new_data = file_number, nut_supplements_type, nut_supplements_quant, nut_supplements_duration
        insert(conn, cursor, table_nut, columns, new_data)
        add_supp = ask_y_n('Add more nutritional supplements?')
    type_nut = '; '.join(type_nut_list)
    quant_nut = '; '.join(quant_nut_list)
    duration_nut = "; ".join(duration_nut_list)
    return (type_nut, quant_nut, duration_nut)

def med_history_table(conn, cursor, file_number):
    add_history = True
    diagnosis_date_list, treatment_list, condition_list = [], [], []
    while add_history:
        condition = input("Condition : ")
        condition_list.append(condition)
        diagnosis_date = input("Date of diagnosis: ")
        diagnosis_date_list.append(diagnosis_date)
        treatment = input("Treatment: ")
        treatment_list.append(treatment)
        history = file_number, condition, diagnosis_date, treatment
        table_med = "General_Medical_History"
        columns = "File_number, Condition, Diagnosis_date, Treatment"
        insert(conn, cursor, table_med, columns, history)
        add_history = ask_y_n ('Add more history')
    condition_hist = '; '.join(condition_list)
    treatment_hist = '; '.join(treatment_list)
    diagnosis_date_hist = "; ".join(diagnosis_date_list)
    return (condition_hist, diagnosis_date_hist, treatment_hist)

def family_cancer_table(conn, cursor, file_number):
    add_family = True
    type_cancer_list, relation_degree_list, type_relation_list, age_detect_list = [], [], [], []
    all_data = []
    while add_family:
        type_of_cancer = input("Type of Cancer: ")
        type_cancer_list.append(type_of_cancer)
        relation_to_patient = ask_option("Relation to patient", ["Immediate Family", "Maternal Family", "Paternal Family"])
        relation_degree_list.append(relation_to_patient)
        type_relation = input("Specific Relationship:")
        type_relation_list.append(type_relation)
        age_at_detection_yrs = input('Age at detection (yrs) :')
        age_detect_list.append(age_at_detection_yrs)
        family_history = file_number, type_of_cancer, relation_to_patient, type_relation, age_at_detection_yrs
        family_history_list = "; ".join([type_of_cancer, relation_to_patient, type_relation, age_at_detection_yrs])
        all_data.append(family_history_list)
        columns = 'File_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs'
        table = "Family_Cancer_History"
        insert(conn, cursor, table, columns, family_history)
        add_family = ask_y_n("Add more family cancer history? ")
    all_data_flat = "|".join(all_data)
    return(all_data_flat)


def other_symp(conn, cursor, file_number, table):
    add_symp = True
    all_data = []
    while add_symp:
        other_symp = input("Type of symptom: ")
        symp_breast_right = input("Right Breast y/n: ")
        if str.lower(symp_breast_right) == "y":
            symp_breast_right = other_symp
            symp_duration_right = input("Duration of symptoms in right breast: ")
        else:
            symp_breast_right = None
            symp_duration_right = None
        symp_breast_left = input("Left Breast y/n: ")
        if str.lower(symp_breast_left) == "y":
            symp_breast_left = other_symp
            symp_duration_left = input("Duration of symptoms in left breast: ")
        else:
            symp_breast_left = None
            symp_duration_left = None
        RB = [symp_breast_right, symp_duration_right]
        LB = [symp_breast_left, symp_duration_left]
        data = [RB, LB]
        all_data.append(data)
        add_symp =  ask_y_n("Include more symptoms?")
    rb = get_rb_lb(all_data, 0)
    rb_symp = list(filter(None, get_rb_lb(rb, 0)))
    rb_dur = list(filter(None, get_rb_lb(rb, 1)))
    lb = get_rb_lb(all_data, 1)
    lb_symp = list(filter(None, get_rb_lb(lb, 0)))
    lb_dur = list(filter(None, get_rb_lb(lb, 1)))
    data = [rb_symp, rb_dur, lb_symp, lb_dur]
    for index in range(0, len(data)):
        if not data[index]:
            data[index] = ["No other symptoms"]
        else:
            data[index] = ["; ".join(data[index])]
    data_flat = [item for sublist in data for item in sublist]
    new_data = tuple(data_flat)
    columns = "RB_Other_Symptoms", "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "RB_Other_Symptoms_duration"
    update_multiple(conn, cursor, table, columns, file_number, new_data)
    return (new_data)

def feed_duration (conn, cursor, file_number, children_number):
    table = "Breast_Feeding"
    child_list, feeding_duration_list, feeding_details_list = [], [], []
    child_number = int(children_number)
    for index in range(0, child_number):
        kid = str(index+1)
        kid_add = "Child "+ kid
        child_list.append(kid_add)
        feeding_duration = input("Breast feeding duration for "+ kid_add +" (months) ?")
        feeding_duration_list.append(feeding_duration)
        category = "Breast feeding for child " + kid
        options = ["Right Breast", "Left Breast", "Both Breasts", "Other"]
        feeding_details = ask_option(category, options)
        feeding_details_list.append(feeding_details)
        columns = 'File_number, Child_number, Feeding_duration, Breast_usage_feeding'
        data = file_number, kid, feeding_duration, feeding_details
        insert (conn, cursor, table, columns, data)
    data_list = [child_list, feeding_duration_list, feeding_details_list]
    data_return = join_lists(data_list, "; ")
    return(data_return)