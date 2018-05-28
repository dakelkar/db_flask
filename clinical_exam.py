import modules.ask_y_n_statement as ask_y_n_statement
import modules.pccm_names as pccm_names
from additional_tables.radio_tables import clinical_tests
import sql.add_update_sql as add_update_sql
from datetime import datetime


def clinical_exam_initial (file_number, user_name):
    module_name = "clinical_exam_initial"
    check = False
    while not check:
        con_stat = ask_y_n_statement.ask_y_n("Has consent been taken from patient?", "Consent Taken", "No Consent")
        if con_stat == "Consent Taken":
            con_form = ask_y_n_statement.ask_y_n("Is consent form with signature present in file ?",
                                             "Consent form with signature present in folder",
                                                 "Completed consent form not present in folder")
        else:
            con_form = "NA"
        prov_diag = input ("Provisional Diagnosis: ")
        options = ["Definite", "Vague", "Diffuse", "Nil", "Other"]
        lump_palp = ask_y_n_statement.ask_option("Palpable lump in the breast?", options)
        lump_location = ask_y_n_statement.ask_option("Location of lump", ["Right Breast", "Left Breast",
                                                                          "Both", "Not present"])
        lump_location_data = []
        if lump_location == "Right Breast" or lump_location == "Both":
            category = "Lump location on Right Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            lump_location_rb = ask_y_n_statement.ask_option(category, options)
            lump_location_rb_data = "RB-"+lump_location_rb
            lump_location_data.append(lump_location_rb_data)
        if lump_location == "Left Breast" or lump_location == "Both":
            category = "Lump location on Left Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            lump_location_lb = ask_y_n_statement.ask_option(category, options)
            lump_location_lb_data = "LB-" + lump_location_lb
            lump_location_data.append(lump_location_lb_data)
        lump_location_data = "; ".join(lump_location_data)
        if lump_location == "Not present":
            lump_location_data = "Lump " + lump_location
            lump_size, lump_number,lump_consistency,lump_fixity  = ("NA",)*4
        else:
            lump_size = ask_y_n_statement.ask_option("Lump size", ["< 2cm", "2-5 cm", ">5 cm"])
            lump_number = ask_y_n_statement.ask_option("Number of lumps", ["Single", "Multiple", "Other"])
            lump_consistency = ask_y_n_statement.ask_option("Consistency of lumps", ["Soft", "Firm", "Hard", "Cystic",
                                                                                     "Mobile", "Other"])
            lump_fixity = ask_y_n_statement.ask_option("Lump fixity to ", ["Skin", "Chest wall", "Pectoral major muscle",
                                                                           "No Fixation", "Other"])
        mastitis_location = ask_y_n_statement.ask_option("Location of mastitis",
                                                     ["Right Breast", "Left Breast", "Both", "Not present"])
        mastitis_location_data = []
        if mastitis_location == "Right Breast" or mastitis_location == "Both":
            category = "Mastitis location on Right Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            mastitis_location_rb = ask_y_n_statement.ask_option(category, options)
            mastitis_location_rb_data = "RB-" + mastitis_location_rb
            mastitis_location_data.append(mastitis_location_rb_data)
        if mastitis_location == "Left Breast" or mastitis_location == "Both":
            category = "Mastitis location on Left Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            mastitis_location_lb = ask_y_n_statement.ask_option(category, options)
            mastitis_location_lb_data = "LB-" + mastitis_location_lb
            mastitis_location_data.append(mastitis_location_lb_data)
        mastitis_location_data = "; ".join(mastitis_location_data)
        if mastitis_location == "Not present":
            mastitis_location_data = "mastitis " + mastitis_location
            mastitis_type = "NA"
        else:
            mastitis_type = ask_y_n_statement.ask_option("Mastitis type", ["Diffuse", "Sectoral", "Other"])
        tender = ask_y_n_statement.ask_option("Tenderness in breast ?",["Right Breast", "Left Breast", "Both",
                                                                        "Not Present", "Other"])
        retract = ask_y_n_statement.ask_option("Nipple Retraction ?",["Right Breast", "Left Breast", "Both",
                                                                      "Not Present", "Other"])
        discharge = ask_y_n_statement.ask_option("Nipple Discharge ?",
                                     ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
        if discharge == "Not Present":
            discharge_type = "NA"
        else:
            discharge_type = ask_y_n_statement.ask_option("Discharge Type?",
                                     ["Serous", "Milky", "Brown", "Bloody", "Other"])
        skin_change_location = ask_y_n_statement.ask_option("Skin Changes?",
                                     ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
        if skin_change_location == "Not Present":
            skin_change_type = "NA"
        else:
            skin_change = []
            change_add = True
            while change_add:
                skin_change_type = ask_y_n_statement.ask_option("Type of skin change?",
                                         ["Dimpling", "Ulceration", "Discolouration", "Eczema", "Edema", "Redness",
                                          "Peau d'orange", "Other"])
                skin_change.append(skin_change_type)
                change_add = ask_y_n_statement.ask_y_n("Enter another type of skin change?")
            skin_change_type = "; ".join(skin_change)
        ax_nodes = ask_y_n_statement.ask_option("Palpable axillary nodes",
                                     ["Right Breast", "Left Breast", "Both", "Not palpable", "Other"])
        if ax_nodes == "Not palpable":
            ax_nodes_number, ax_nodes_size, ax_nodes_fixity = ("NA",)*3
        else:
            ax_nodes_number = input("Number of nodes: ")
            ax_nodes_size = input("Size of nodes: ")
            ax_nodes_fixity =  ask_y_n_statement.ask_y_n("Fixity of axillary nodes", "Yes", "No")
        supra_nodes = ask_y_n_statement.ask_option("Palpable supraclavicular nodes",
                                                ["Right Breast", "Left Breast", "Both", "Not palpable", "Other"])
        if supra_nodes == "Not palpable":
            supra_nodes_number, supra_nodes_size, supra_nodes_fixity = ("NA",)*3
        else:
            supra_nodes_number = input("Number of nodes: ")
            supra_nodes_size = input("Size of nodes: ")
            supra_nodes_fixity = ask_y_n_statement.ask_y_n("Fixity of supraclavicular nodes", "Yes", "No")
        contra_breast = ask_y_n_statement.ask_option("Contralateral Breast", ["Normal", "Diffuse Mastitis",
                                                                              "Localised Mastitis", "Other"])
        arm_edema = ask_y_n_statement.ask_option("Edema of arm", ["Right", "Left", "Both", "Not Present", "Other"])
        arm_circ_right = input("Circumference of right arm (cm): ")
        arm_volume_right = input("Upper limb volume - right arm (cc): ")
        arm_elbow_right = input("Distance from the elbow - right arm (cm): ")
        arm_circ_left = input("Circumference of left arm (cm): ")
        arm_volume_left = input("Upper limb volume - left arm (cc): ")
        arm_elbow_left = input("Distance from the elbow - left arm (cml): ")
        follow_up_advised = input("Follow up tests advised for patient: ")
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = [con_stat, con_form, prov_diag, lump_palp, lump_location_data, lump_size, lump_number, lump_consistency,
                     lump_fixity, mastitis_location_data, mastitis_type, tender, retract, discharge, discharge_type,
                     skin_change_location, skin_change_type, ax_nodes, ax_nodes_number, ax_nodes_size, ax_nodes_fixity,
                     supra_nodes, supra_nodes_number, supra_nodes_size, supra_nodes_fixity, contra_breast, arm_edema,
                     arm_circ_right, arm_volume_right, arm_elbow_right, arm_circ_left, arm_volume_left, arm_elbow_left,
                     follow_up_advised, user_name, last_update]
        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def nipple_cytology (file_number):
    module_name = "nipple_cytology"
    check = False
    while not check:
        cyto = ask_y_n_statement.ask_option("Nipple Cytology", ["Done", "Not Done"])
        if cyto == "Not Done":
            cyto_date, cyto_number, cyto_report = ("NA",)*3
        else:
            cyto_date = input("Date of nipple cytology: ")
            cyto_number = input("Nipple Cytology number: ")
            cyto_report = ask_y_n_statement.ask_option("Nipple Cytology report and interpretation", ["Normal",
                                                                                                     "Suspicious",
                                                                                                     "Diagnostic for "
                                                                                                     "Cancer", "Other"])
        data_list = [cyto, cyto_date, cyto_number, cyto_report]
        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def other_test(file_number):
    module_name = "other_test"
    other_tests = [["USG Abdomen", "Abnormal"], ["CECT Abdomen and Thorax", "Visceral Metastasis"],
                   ["PET Scan", "Visceral Metastasis", "Skeletal Metastasis"], ["Bone Scan", "Skeletal Metastasis"]]
    check = False
    while not check:
        data_all = []
        for index in other_tests:
            data = clinical_tests(index)
            data_all.append(data)
        data_all_flat =  [item for sublist in data_all for item in sublist]
        col_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, col_list, data_all_flat)
    return data_all_flat

def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Clinical_Exam(File_number) VALUES ('" + file_number + "')")


def add_data(conn, cursor, file_number, user_name):
    table = "Clinical_Exam"
    #file_row(cursor, file_number)
    enter =ask_y_n_statement.ask_y_n("Enter Clinical Examination information")
    if enter:
        data = clinical_exam_initial(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("clinical_exam_initial"),
                                       file_number, data)
    enter = ask_y_n_statement.ask_y_n("Enter Nipple Cytology report?")
    if enter:
        data = nipple_cytology(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("nipple_cytology"), file_number,
                                       data)
    enter = ask_y_n_statement.ask_y_n("Enter results of other clinical tests?")
    if enter:
        data = other_test(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("other_test"), file_number,
                                       data)

def edit_data(conn, cursor, file_number, user_name):
    table = "Clinical_Exam"
    print("Initial Clinical Examination")
    col_list = pccm_names.name_clinical("clinical_exam_initial")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = clinical_exam_initial(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Nipple Cytology")
    col_list = pccm_names.name_clinical("nipple_cytology")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = nipple_cytology(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Other Tests (USG Abdomen, PET Scan, Bone Scan, CECT Abdomen and Thorax)")
    col_list = pccm_names.name_clinical("other_test")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = other_test(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)

