from additional_tables.radio_tables import lesion_location
from modules.ask_y_n_statement import ask_option, ask_y_n, ask_y_n_na
import sql.add_update_sql as add_update_sql
import modules.pccm_names as pccm_names
from datetime import datetime


def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Surgery_Block_Report_Data(File_number) VALUES ('" + file_number + "')")


def surgery_block_information_1(file_number):
    module_name = "surgery_block_information_1"
    check = False
    while not check:
        con_stat = ask_y_n("Has consent been taken from patient?", "Consent Taken", "No Consent")
        if con_stat == "Consent Taken":
            con_form = ask_y_n("Is consent form with signature present in file ?",
                               "Consent form with signature present in folder",
                               "Completed consent form not present in folder")
        else:
            con_form = "NA"
        block_sr = input("Surgery Block Serial Number: ")
        print ("Surgery Block Location")
        location = False
        while location == False:
            print ("Surgery Block Location: ")
            block_cab = input ("Cabinet No: " )
            if block_cab !='to be filled':
                block_drawer = input ("Drawer Number: ")
                block_col = input ("Column Number: ")
                block_pos = ask_option("Is Block in", ["Front", "Back"])
                block_location = block_cab+"-"+block_drawer+"-"+block_col+"-"+block_pos
            else:
                block_location = block_cab
            print ("Block location is "+ block_location)
            location = ask_y_n("Is this correct?")
        block_current = input ("What is the current location of block? ")
        surg_block_id = input("Surgical Block ID: ")
        surg_no_block = input("Number of Blocks: ")
        surg_block_source = input("Pathology Lab (source of block): ")
        surg_tumour_block = input("Tumour Block Reference: ")
        surg_node_block = input("Nodes Block Reference: ")
        surg_normal_block = input("Adjacent Normal Block Reference: ")
        surg_red_block = input("Reduction Tissue Block Reference: ")
        surg_date = input("Date of Surgery: ")
        surg_name = input("Name of surgeon: ")
        surg_hosp_id = input("Hospital ID: ")
        lesion_side = ask_option("Lesion on", ["Right Breast", "Left Breast", "Both"])
        lesion_side_data = lesion_location(lesion_side)
        nact = ask_y_n_na("Did the patient undergo NACT?", "NACT done", "No NACT", "Data to be filled")
        surg_type = ask_option("Type Surgery (If both breasts have been operated enter data for LB and RB in 'Other'",
                               ["Reconstruction", "Breast Conservation Surgery (BCS)", "Therapeutic Mammoplasty",
                                "Reduction Mammoplasty", "Wide Local Excision", "Other"])
        if surg_type == "Reconstruction":
            surg_type = ask_option("Type Reconstruction", ["Mastectomy","Modified Radical Mastectomy",
                                                                             "Implant"])
        data_list = [con_stat, con_form, block_sr, block_current, surg_block_id, surg_no_block, surg_block_source,
                     surg_tumour_block, surg_node_block, surg_normal_block, surg_red_block, surg_date, surg_name,
                     surg_hosp_id, lesion_side_data, nact, surg_type]
        columns_list = pccm_names.names_surgery(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def surgery_block_information_2 (file_number):
    module_name = "surgery_block_information_2"
    check = False
    while not check:
        tumour_size = input("Tumour size: ")
        tumour_grade = ask_option("Tumour Grade", ["1", "2", "3", "Other"])
        surg_diag = ask_option("Surgery Diagnosis",
                               ["Ductal carcinoma in situ(DCIS)", "Invasive Ductal Carcinoma", "Other"])
        if (surg_diag == "Ductal carcinoma in situ(DCIS)"):
            dcis_percent = input("Percent DCIS: ")
            dcis_invasion = ask_option("DCIS Invasion", ['Microinvasion', 'Macroinvasion', 'Not mentioned in report'])
        else:
            dcis_percent, dcis_invasion = ("NA",) * 2
        per_inv = ask_option("Perineural Invasion", ["Perineural Invasion Present", "Perineural Invasion Absent", 'Other'])
        necrosis = ask_option("Necrosis", ["Necrosis Present", "Necrosis Absent", 'Other'])
        lymph_invasion = ask_option("Lymphovascular invasion", ["Lymphovascular invasion Present",
                                 "Lymphovascular invasion Absent", 'Other'])
        margin = ask_option("Margins", ["Margins Involved", "Margins Free", 'Other'])
        print("Surgery Block Report")
        report = ask_option("Pathological Complete Remission", ["Yes", "No", 'PCR not mentioned in report',"Other"])
        data_list = [tumour_size, tumour_grade, surg_diag, dcis_percent, dcis_invasion, per_inv, necrosis,
                     lymph_invasion, margin, report]
        columns_list = pccm_names.names_surgery(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def surgery_block_information_3 (file_number):
    module_name = "surgery_block_information_3"
    check = False
    while not check:
        surgery_er = ask_option("ER Status", ["Positive", "Negative", "Data not available", "Other"])
        if (surgery_er == "Positive"):
            surgery_er_percent = input("ER Percent: ")
        else:
            surgery_er_percent = "ER status " + surgery_er
        surgery_pr = ask_option("PR Status", ["Positive", "Negative", "Data not available", "Other"])
        if (surgery_pr == "Positive"):
            surgery_pr_percent = input("PR Percent: ")
        else:
            surgery_pr_percent = "PR status " + surgery_pr
        surgery_her2 = ask_option("HER2 Status", ["Positive", "Equivocal", "Negative", "Data not available", "Other"])
        surgery_her2_grade = input("HER2 Grade: ")
        surgery_fish = ask_option("FISH", ["Positive", "Negative"])
        surgery_ki67 = input("Ki67 Percent: ")
        sent_data = node_details("Sentinel")
        sentinel, sent_number_rem, sent_number_pos, sent_number = sent_data
        ax_data = node_details("Axillary")
        ax, ax_number_rem, ax_number_pos, ax_number = ax_data
        print("Axillary Node LNR: " + ax_number)
        ap_data = node_details("Apical")
        ap, ap_number_rem, ap_number_pos, ap_number = ap_data
        per_spread = ask_option("Perinodal Spread", ["Perinodal Spread Seen", "No Perinodal Spread",
                                                     "Not mentioned in Report", "Data not available"])
        supra_inv = ask_option("Supraclavicular Node Involvment", ["Supraclavicular Node Involved",
                                                                   "No Supraclavicular Node Involvment",
                                                                   'Not mentioned in report',
                                                                   'Data not available'])
        data_list = [surgery_er ,surgery_er_percent, surgery_pr, surgery_pr_percent, surgery_her2, surgery_her2_grade,
                     surgery_fish, surgery_ki67,sentinel, sent_number_rem, sent_number_pos, ax, ax_number_rem,
                     ax_number_pos, ax_number, ap, ap_number_rem, ap_number_pos, per_spread, supra_inv]
        columns_list = pccm_names.names_surgery(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def node_details (node_name):
    node_name + " Node"
    number_removed = input("Number of "+node_name+" Nodes removed: ")
    if number_removed==0:
        node, number_removed, number_positive, number = ("No node removed", )*4
    else:
        number_positive = input("Number of "+node_name+" Nodes positive: ")
        if int(number_positive)>0:
            node = "Positive"
        else:
            node = "Negative"
        number = "("+number_positive + "/" + number_removed+")"
    data = [node, number_removed, number_positive, number]
    return data

def path_stage(file_number, user_name):
    module_name = "path_stage"
    check = False
    while not check:
        category = "pT"
        options = ["is", "0", "1", "2", "3", "4", "Other"]
        pT = ask_option(category, options)
        category = "pN"
        options = ["0", "1", "2", "3", "4", "Other"]
        pN = ask_option(category, options)
        category = ("M")
        options = ["0", "1", "2", "3", "Other"]
        M = ask_option(category, options)
        path_stage = "pT" + pT + "N" + pN + "M" + M
        print ("Pathological Stage: "+ path_stage)
        check = ask_y_n("Is pathological stage correct")
        if not check:
            path_stage = input("Please enter correct pathological stage: ")
        if M in {"1", "2", "3"} :
            clinical_stage = "IV"
        elif M == "0":
            if pN == "3":
                clinical_stage = "IIIC"
            elif pN == "2":
                if pT == "4":
                    clinical_stage = "IIIB"
                else:
                    clinical_stage = "IIIA"
            elif pN == "1mi":
                clinical_stage = "IB"
            elif pN == "1":
                if (pT=="0" or pT == "1"):
                    clinical_stage = "IIA"
                elif pT=="2":
                    clinical_stage = "IIB"
                elif pT == "3":
                    clinical_stage = "IIIA"
                elif pT =="4":
                    clinical_stage = "IIIC"
                else:
                    clinical_stage = input("Clinical Staging: ")
            elif pN =="0":
                if pT =="is":
                    clinical_stage = "0"
                elif pT == "1":
                    clinical_stage = "IA"
                elif pT =="2":
                    clinical_stage = "IIA"
                elif pT == "3":
                    clinical_stage = "IIB"
                elif pT == "4":
                    clinical_stage = "IIIB"
                else:
                    clinical_stage = input("Clinical Staging: ")
        else:
            clinical_stage = input("Clinical Staging: ")
        print ("Clinical stage "+ clinical_stage)
        print ("Based on TNM status", path_stage, "and Anatomic stage/prognostic groups table at"
                                                  "https://emedicine.medscape.com/article/2007112-overview")
        check = ask_y_n("Is clinical stage correct")
        if not check:
            clinical_stage = input("Please enter correct clinical stage: ")
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = [pT, pN, M, path_stage, clinical_stage, user_name, last_update]
        columns_list = pccm_names.names_surgery(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def add_data(conn, cursor, file_number, user_name):
    table = "Surgery_Block_Report_Data"
    #file_row(cursor, file_number)
    enter = ask_y_n("Enter Surgery Block information?")
    if enter:
        data = surgery_block_information_1(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_surgery("surgery_block_information_1"), file_number, data)
    enter = ask_y_n("Enter Surgery Block information (Tumour Details) ?")
    if enter:
        data = surgery_block_information_2(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_surgery("surgery_block_information_2"), file_number, data)
    enter = ask_y_n("Enter Surgery Block information (Node Details)?")
    if enter:
        data = surgery_block_information_3(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_surgery("surgery_block_information_3"), file_number, data)
    enter = ask_y_n("Enter Pathological Stage?")
    if enter:
        data = path_stage(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_surgery("path_stage"), file_number, data)


def edit_data(conn, cursor, file_number, user_name):
    table = "Surgery_Block_Report_Data"
    print("Surgery Block information")
    col_list = pccm_names.names_surgery("surgery_block_information_1")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = surgery_block_information_1(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print ("Surgery Block information (Tumour Details)")
    col_list = pccm_names.names_surgery("surgery_block_information_2")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = surgery_block_information_2(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Surgery Block information (Node Details)")
    col_list = pccm_names.names_surgery("surgery_block_information_3")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = surgery_block_information_3(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Pathological Stage")
    col_list = pccm_names.names_surgery("path_stage")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = path_stage(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)