from modules.ask_y_n_statement import ask_option, ask_y_n, join_lists, ask_y_n_na
from additional_tables.radio_tables import lesion_location
import sql.add_update_sql as add_update_sql
from modules.pccm_names import names_surgery_information as names
import additional_tables.surgery_tables as surgery_tables
from datetime import datetime
import pandas as pd


def surgery_information(file_number):
    check = False
    while not check:
        surgery_date = input("Date of surgery: ")
        surgery_hospital = input("Name of hospital: ")
        surgery_patient_hospital_id = input("Patient ID at the hospital: ")
        surgery_hospital_ward = input("Name of hospital ward: ")
        surgery_date_admission = input("Date of admission: ")
        surgery_name_anaesthetist = input("Name of Anaesthetist: ")
        surgery_name_surgeon = input("Name of the Surgeon/s: ")
        lesion = ask_option("Location of lesion", ["Right Breast", "Left Breast", "Both Breasts", "Other","Not known"])
        if lesion in {"Right Breast", "Left Breast", "Both Breasts"}:
           surgery_lesion_location = lesion_location(lesion)
        else:
           surgery_lesion_location = 'Requires specialist Input'
        surgery_type = ask_option("Types of Surgery", ["Conservative Breast Surgery", "Implant Based Reconstruction",
                                                      'Requires Specialist Input'])
        if surgery_type == "Conservative Breast Surgery":
            surgery_incision = ask_option("Type of Incisions", surgery_tables.incision("conservative_incision"))
            if surgery_incision == "Circum-areolar":
                incisions_type = ask_option("Circum-areolar incision is", ["at areolar margin", 'Away from margin',
                                                                           'Other'])
                surgery_incision = surgery_incision + " " + incisions_type
            surgery_type_subtype = ask_option("Type of Breast Conservation Surgery", ['Conventional Surgery',
                                                                                      'Oncoplastic Surgery', 'Other'])
            if surgery_type_subtype == "Conventional Surgery":
                surgery_type_level_subtype = ask_option("type of conventional surgery", ["Lumpectomy", "Quadrantectomy",
                                                                      "Wedge Resection"])
                oncoplastic_surgery_type, oncoplastic_surgery_flap, oncoplastic_surgery_plan, \
                oncoplastic_surgery_tumour_filled_by,oncoplastic_surgery_nac_graft, oncoplastic_surgery_primary_pedicle, \
                oncoplastic_surgery_secondary_pedicle, reconstruction_surgery_implant_type, \
                reconstruction_surgery_implant_size = ("Not applicable for Conventional Breast Conservation", )*9
            elif surgery_type_subtype == "Oncoplastic Surgery":
                surgery_type_level_subtype = ask_option("Level of oncoplastic surgery", ["Level 1",
                                                                                         "Level 2: Therapeutic Mammoplasty",
                                                        'Level 3: Volume Replacement'])
                if surgery_type_level_subtype == "Level 1":
                    oncoplastic_surgery_type = ask_option("Type of level 1 oncoplastic surgery",
                                                          ["Type 1: Simple oncoplastic – mammoplasty",
                                                           "Type 2: Volume Displacement"])
                    if oncoplastic_surgery_type == "Type 2: Volume Displacment":
                        oncoplastic_surgery_flap = ask_option("Type of flap used", ["Grisotti Flap", "Round Block",
                                                                        "Batwing Procedure"])
                        oncoplastic_surgery_plan, oncoplastic_surgery_tumour_filled_by, oncoplastic_surgery_nac_graft, \
                        oncoplastic_surgery_primary_pedicle, oncoplastic_surgery_secondary_pedicle, \
                        reconstruction_surgery_implant_type, reconstruction_surgery_implant_size, \
                        surgery_type_level_subtype = ("Not applicabel for Level 1: Type 2 Oncolplastic Surgery with " \
                                                      "volume displacement",)* 8
                    elif oncoplastic_surgery_type == 'Type 1: Simple oncoplastic – mammoplasty':
                        oncoplastic_surgery_flap = "No flap for Simple oncoplastic – mammoplasty"
                        oncoplastic_surgery_plan, oncoplastic_surgery_tumour_filled_by, oncoplastic_surgery_nac_graft, \
                        oncoplastic_surgery_primary_pedicle, oncoplastic_surgery_secondary_pedicle, \
                        reconstruction_surgery_implant_type, reconstruction_surgery_implant_size, \
                        surgery_type_level_subtype = ("Not applicabel for Level 1: Type 1 Simple oncoplastic – "
                                                      "mammoplasty",) * 8
                elif surgery_type_level_subtype =="Level 2: Therapeutic Mammoplasty":
                    oncoplastic_surgery_type = ask_option("Subtypes of Level 2 oncoplastic surgery, Therapeutic Mammoplastty",
                                      ["Simple Therapeutic", "Complex Therapeutic", "Extreme Therapeutic"])
                    oncoplastic_surgery_flap = "Therapeutic Mammoplasty"
                    if oncoplastic_surgery_type in {"Simple Therapeutic"}:
                        oncoplastic_surgery_plan = ask_option("Type of Plan used", ["Wise pattern", "Vertical Scar"])
                        oncoplastic_surgery_tumour_filled_by = oncoplastic_surgery_type
                        oncoplastic_surgery_nac_graft = "No NAC Graft, "+ oncoplastic_surgery_type
                        oncoplastic_surgery_primary_pedicle = ask_option("Type of pedicle used", surgery_tables.pedicle("primary"))
                        oncoplastic_surgery_secondary_pedicle = "No secondary pedicle, "+ oncoplastic_surgery_type
                    if oncoplastic_surgery_type in {"Complex Therapeutic", "Extreme Therapeutic"}:
                        oncoplastic_surgery_tumour_filled_by = ask_option("Tumour filled by", ["Extended Primary Pedicle", "Secondary Pedicle"])
                        oncoplastic_surgery_plan = ask_option("Type of Plan used", ["Wise pattern", "Vertical Scar"])
                        oncoplastic_surgery_nac_graft = ask_y_n("Is NAC graft done?")
                        if not oncoplastic_surgery_nac_graft:
                            oncoplastic_surgery_nac_graft = "Nipple areola complex is not grafted "
                            oncoplastic_surgery_primary_pedicle = ask_option("What is Nipple On (primary pedicle) pedicle used?",
                                                         surgery_tables.pedicle("primary"))

                            oncoplastic_surgery_secondary_pedicle = ask_option("What is the secondary pedicle used?",
                                                            surgery_tables.pedicle("secondary"))
                        else:
                            oncoplastic_surgery_nac_graft = "Nipple areola complex is grafted"
                            oncoplastic_surgery_primary_pedicle = oncoplastic_surgery_nac_graft
                            oncoplastic_surgery_secondary_pedicle = ask_option("What is the pedicle used?",
                                                            surgery_tables.pedicle("secondary"))
                elif surgery_type_level_subtype == "Level 3: Volume Replacement":
                    oncoplastic_surgery_flap = ask_option("Type of flap used", ["Local Flaps", "LD Flaps", "Mini LD"])
                    if oncoplastic_surgery_flap == "Local Flaps":
                        flap_type = ask_option("type of flap", ["Thoraco-epigastric Flap", "LICAP", "TDAP"])
                        oncoplastic_surgery_flap = "Local "+flap_type
                        oncoplastic_surgery_plan, oncoplastic_surgery_tumour_filled_by, oncoplastic_surgery_nac_graft, \
                        oncoplastic_surgery_primary_pedicle, oncoplastic_surgery_secondary_pedicle = \
                            ("Not applicable for volume replacment oncoplasty", )*5
            else:
                other = surgery_type_subtype
                oncoplastic_surgery_type, oncoplastic_surgery_flap, oncoplastic_surgery_plan, \
                oncoplastic_surgery_tumour_filled_by, oncoplastic_surgery_nac_graft, oncoplastic_surgery_primary_pedicle, \
                oncoplastic_surgery_secondary_pedicle, reconstruction_surgery_implant_type, \
                reconstruction_surgery_implant_size, surgery_type_level_subtype = (other,) * 10
        elif surgery_type == "Implant Based Reconstruction":
            surgery_type_subtype = ask_option("Type of surgery", ['Implant Based Reconstruction',
                                                          'Non Sling – Conventional IBRS',
                                                          'Sling ALDS',
                                                          'Advanced Sling (AALDS)',
                                                          'LD Flap + Implant',
                                                          'TDAP + Implant',
                                                          'LICAP + Implant'])
            reconstruction_surgery_implant_type = ask_option("Type of implant used", ["Fixed Volume", "Dual Lumen"])
            if reconstruction_surgery_implant_type == "Fixed Volume":
                fixed_type = ask_option("Type of fixed volume implant", ["Smooth", "Textured", "Microtextured"])
                reconstruction_surgery_implant_type = reconstruction_surgery_implant_type + " " + fixed_type
            reconstruction_surgery_implant_size = input("Size of implant used: ")
            surgery_incision = ask_option("Type of incision used", surgery_tables.incision("reconstruction"
                                                                                           "_incision"))
            surgery_type_level_subtype, oncoplastic_surgery_type, oncoplastic_surgery_flap, \
            oncoplastic_surgery_plan,oncoplastic_surgery_tumour_filled_by,oncoplastic_surgery_nac_graft,\
            oncoplastic_surgery_primary_pedicle,oncoplastic_surgery_secondary_pedicle = \
                ("Not applicable for reconstruction surgery", )*8
        else:
            surgery_incision,surgery_type_subtype,surgery_type_level_subtype,oncoplastic_surgery_type,\
            oncoplastic_surgery_flap,oncoplastic_surgery_plan,oncoplastic_surgery_tumour_filled_by,\
            oncoplastic_surgery_nac_graft,oncoplastic_surgery_primary_pedicle,oncoplastic_surgery_secondary_pedicle,\
            reconstruction_surgery_implant_type,reconstruction_surgery_implant_size = (surgery_type, ) *12
        contralateral_surgery = ask_option("Was Contralateral Surgery done?", ["Yes", "No", "Requires Specialist Input"])
        if contralateral_surgery == "Yes":
            contralateral_surgery_type = ask_option("Type of Contralateral Surgery Done", ["Symmetrisation",
                                    "Prophylactic Masstectomy with Reconstruction", "Other"])
            if contralateral_surgery_type == "Symmetrisation":
                contralateral_surgery_type_details = ask_option("Type of Symmetrisation", ["Same as other side",
                                                                "Different from other side"])
                if contralateral_surgery_type_details == "Different from other side":
                    contralateral_surgery_type_details = input ("Please give details of symmetrisation: ")
            else:
                contralateral_surgery_type_details = input ("Please give details of "+contralateral_surgery_type)
            contralateral_surgery = "Contralateral Surgery Performed"
        elif contralateral_surgery == "No":
            contralateral_surgery, contralateral_surgery_type, contralateral_surgery_type_details = \
                ("Contralateral Surgery Not Performed", )*3
        elif contralateral_surgery == "Requires Specialist Input":
             contralateral_surgery_type, contralateral_surgery_type_details = ('Requires Specialist Input', )*2
        surgery_notes = input("Additional Surgery Notes and comments (if available): ")
        data_list = [surgery_date,
                        surgery_hospital,
                        surgery_patient_hospital_id,
                        surgery_date_admission,
                        surgery_hospital_ward,
                        surgery_name_anaesthetist,
                        surgery_name_surgeon,
                        surgery_lesion_location,
                        surgery_type,
                        surgery_incision,
                        surgery_type_subtype,
                        surgery_type_level_subtype,
                        oncoplastic_surgery_type,
                        oncoplastic_surgery_flap,
                        oncoplastic_surgery_plan,
                        oncoplastic_surgery_tumour_filled_by,
                        oncoplastic_surgery_nac_graft,
                        oncoplastic_surgery_primary_pedicle,
                        oncoplastic_surgery_secondary_pedicle,
                        reconstruction_surgery_implant_type,
                        reconstruction_surgery_implant_size,
                        contralateral_surgery,
                        contralateral_surgery_type,
                        contralateral_surgery_type_details,
                        surgery_notes]
        col_list = names('surgery_information')
        check = add_update_sql.review_input(file_number, col_list, data_list)
    return data_list

def node_excision (file_number):
    check = False
    while not check:
        guide_add = True
        guide = []
        while guide_add:
            surgery_guide = ask_option("Excision guided by", ["Palpation", "USG guided", "Wire placement guided"])
            guide.append(surgery_guide)
            guide_add = ask_y_n("Add another method to guide?")
        surgery_guide = "; ".join(guide)
        frozen_samples = ask_y_n_na("Any samples sent for histopathology (frozen)?")
        if frozen_samples:
            frozen_samples = []
            sn_frozen = ask_y_n("Sentinel Node sent for histopathology (frozen)?", yes_ans="Sentinel Node")
            if sn_frozen == 'Sentinel Node':
                frozen_samples.append(sn_frozen)
            specimen_frozen = ask_y_n_na("Specimen sent for histopathology (frozen)?")
            if specimen_frozen == 'Yes':
                nipple_frozen = ask_y_n_na("Under Nipple Surface sent for histopathology (frozen)?",
                                           yes_ans='Under Nipple Surface')
                if nipple_frozen == 'Under Nipple Surface':
                    frozen_samples.append(nipple_frozen)
                other_frozen = ask_y_n_na("Any other specimen sent for histopathology (frozen)?")
                if other_frozen == 'Yes':
                    other_frozen = input("Type of tissue sent for histopathology (frozen): ")
                    frozen_samples.append(other_frozen)
            frozen = "; ".join(frozen_samples)
        else:
            frozen = "NA"
        gross_tumour = input ("Size of tumour on cross section (cm): ")
        skin = ask_y_n_na("Skin involved", yes_ans="Skin involved", no_ans="Skin not involved")
        nodes = ask_option("Nodes excised", ["Sentinel Node", "Sentinel and Axillary Nodes", "Axillary Nodes only",
                                             "Sentinel and lower axillary clearance", "Lower axillary clearance",
                                             "Other"])
        number_lymph = input("Number of lymph nodes excised (if available): ")
        level_lymph = ask_option("Level of lymph node excised", ["I", "II", "III", "Data not available", "Other"])
        sentinel_method = ask_option("Method of labelling Sentinel Node", ["Isotope", "Blue Dye", "Isotope + Blue Dye",
                                                                           "Not done", "Other"])
        sentinel_blue = ask_y_n_na("Blue Node", yes_ans="Blue Node", no_ans="No Blue Node")
        sentinel_hot = ask_y_n_na("Hot Node", yes_ans="Hot Node", no_ans="No Hot Node")
        sentinel_blue_hot = ask_y_n_na("Blue Hot Node", yes_ans="Blue Hot Node", no_ans="No Blue Hot Node")
        sentinel_non_blue_hot = ask_y_n_na("Non Blue, Hot Node", yes_ans= "Non Blue, Hot Node",
                                           no_ans="No Non Blue, Hot Node")
        sentinel_palpable = ask_y_n_na("Palpable Node", yes_ans="Palpable Node", no_ans="No Palpable Node")

        data_list = [surgery_guide, frozen, gross_tumour, skin, nodes, number_lymph, level_lymph, sentinel_method,
                     sentinel_blue, sentinel_hot, sentinel_blue_hot, sentinel_non_blue_hot, sentinel_palpable]
        col_list = names("node_excision")
        check = add_update_sql.review_input(file_number, col_list, data_list)
    return data_list


def post_surgery(file_number, user_name):
    check = False
    while not check:
        chemo = ask_y_n("Is chemotherapy planned?", "Chemotherapy planned", "No Chemotherapy")
        radio = ask_y_n("Is radiotherapy planned?", "Radiotherapy planned", "No Radiotherapy")
        other = ask_y_n("Are there any other post-surgery plans")
        if other:
            other = input("Please specify other post-surgery plans: ")
        else:
            other = "No other post surgery plans"
        drain = input("Drain removal date: ")
        total_drain = input("Total drain days: ")
        post_comp = ask_y_n("Did post-surgery complications occur?")
        if post_comp:
            df_complications_col = ["Day", "Complication", "Treatment"]
            df_complications = pd.DataFrame(columns = df_complications_col)
            day_add = True
            index = 0
            while day_add:
                comp =surgery_tables.surg_complications("post_surgery_comp")
                day = "Day "+input("Days post surgery: ")
                treatment_list = []
                complication = []
                for i in comp:
                    data = ask_y_n("On "+str(day)+ " did post surgery complication "+i+" occur?")
                    if data:
                        complication.append(i)
                        treatment = ask_option("What treatment was done for "+str(i),
                                               surgery_tables.surg_complications("surgical_treatment"))
                        if treatment == 'Non surgical treatment':
                            treatment = input ("What type of non surgical treatment was used?")
                        else:
                            treatment = "Surgical treatment - "+ treatment
                        treatment_list.append(treatment)
                complication= "; ".join(complication)
                treatment_list = "; ".join(treatment_list)
                data = [day, complication, treatment_list]
                df_complications.loc[index] = data
                index = index + 1
                day_add = ask_y_n("Add another day for post surgery complications? ")
            all_data = []
            for index in df_complications_col:
                data = "; ".join(list(df_complications.loc[:, index]))
                all_data.append(data)
            days, complications, treatments = all_data
        else:
            days, complications, treatments = ("No post surgical complications", )*3
        recur = ask_y_n("Did recurrence occur post surgery?")
        if recur:
            recurs = []
            days_recurs = []
            late_add = True
            recur = surgery_tables.surg_complications("recurrence_sites")
            while late_add:
                day = "Day " + input("Days post surgery: ")
                for i in recur:
                    data = ask_y_n("On " + str(day) + " did "+i+" recurrence occur?")
                    if data:
                        recurs.append(i)
                #recurs = "; ".join(recurs)
                if recurs == []:
                    recurs = "No recurrence post surgery"
                days_recurs.append(day)
                late_add = ask_y_n("Add another day for post surgery recurrence? ")
            all_data = [days_recurs, recurs]
            days_recurs, recurs = join_lists(all_data, "; ")
        else:
            days_recurs, recurs = ("No recurrence post surgery",)*2
        opd = input("Please input OPD notes (if any): ")
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = [chemo, radio, other,drain, total_drain, days, complications, treatments, days_recurs, recurs, opd,
                     user_name, last_update]
        col_list = names("post_surgery")
        check = add_update_sql.review_input(file_number, col_list, data_list)
    return data_list


def add_data(conn, cursor, file_number, user_name):
    table = "Surgery_Report"
    #file_row(cursor, file_number)
    enter = ask_y_n("Enter Surgery Information?")
    if enter:
        data = surgery_information(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("surgery_information"), file_number, data)
    enter = ask_y_n("Enter Node Excision Information?")
    if enter:
        data = node_excision(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("surgery_information"), file_number, data)
    enter = ask_y_n("Enter Details of Post-Surgery complications ?")
    if enter:
        data = post_surgery(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, names("post_surgery"), file_number, data)


def edit_data(conn, cursor, file_number, user_name):
    table = "Surgery_Report"
    print("Surgery Information")
    col_list = names("surgery_information")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = surgery_information(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Node Excision")
    col_list = names("node_excision")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = node_excision(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("surgery_information"), file_number, data)
    print("Post-Surgery complications")
    col_list = names("post_surgery")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = post_surgery(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
