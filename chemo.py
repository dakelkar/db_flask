def drug_list():
    drugs = ["5-FluoroUracil", "Anthracycline","Anastrozole", "Carboplatin", "Cisplatin", "Cyclophosphamide",
             "Docitaxel", "Doxorubicin", 'Epirubicin', "Exemestane", "Fulvestrant", "Gemcitabine","Goserelin",
             "Herceptin(Trastuzumab)", "Letrozole", "Leuprolide", "Paclitaxel", "Tamoxifen", "Other"]
    return drugs

def toxicity():
    toxic_cond = ["Fever",
                  "Anaemia",
                  "Neutropenia",
                  "Breathlessness",
                  "Vomiting",
                  "Nausea",
                  "Loose Motions",
                  "Cough",
                  "Urinary Infections",
                  "Cardiotoxicity",
                  "Neuropathy"
                  "Other"]
    return toxic_cond


def tox_table (file_number, cyc_name, week, drug_cyc):
    import modules.ask_y_n_statement as ask_y_n_statement
    import additional_tables.chemo as chemo
    import pandas as pd
    import modules.pccm_names as names
    from sql.add_update_sql import review_df as review
    tox_all= pd.DataFrame(columns=names.names_nact("Tox_table"))
    tox_index = 0
    drugs = "/".join(drug_cyc)
    check_tox = False
    while not check_tox:
        tox = ask_y_n_statement.ask_y_n("Were there any toxic effects in  " + week + " of "+cyc_name)
        tox_grade_list, tox_list, tox_treatment, resp_treatment_list = [list([]) for _ in range(4)]
        if tox:
            for index in chemo.toxicity():
                tox_grade = ask_y_n_statement.ask_option(("the grade of "+index+" in "+cyc_name +"? "),
                            ["Mild", "Moderate", "Severe", "Not Present", "Other"])
                if tox_grade not in {"Not Present"}:
                    tox = index
                    check = False
                    while not check:
                        treatment = input("Treatment given for "+ tox_grade + " " + index+" (include all details): ")
                        resp_treatment = ask_y_n_statement.ask_option(("Response to treatment given for " + tox_grade +
                                                                       " " + index),
                                                                      ["Partial", "Complete", "No Effect", "Other"])
                        data = [file_number, week, cyc_name, drugs, tox, tox_grade, treatment, resp_treatment]
                        tox_all.loc[tox_index] = data
                        check = review(tox_all.loc[tox_index])
                    tox_grade_list.append(tox_grade)
                    tox_list.append(index)
                    tox_treatment.append(treatment)
                    resp_treatment_list.append(resp_treatment)
                    tox_index = tox_index +1
        else:
            tox = "No Toxicity"
            tox_grade,treatment, resp_treatment = ("NA", )*3
            tox_list = ["No Toxicity"]
            tox_grade_list, tox_treatment, resp_treatment_list = [["NA"]]*3
            data = [file_number, week, cyc_name, drugs, tox, tox_grade, treatment, resp_treatment]
            tox_all.loc[tox_index] = data

        all_data = [tox_grade_list, tox_list, tox_treatment, resp_treatment_list]
        response = ask_y_n_statement.join_lists(all_data, "; ")
        check_tox = review(tox_all)
    return response

def get_cycle_data(drug_cycle, tox_cycle):
    import pandas as pd
    data_cycle = []
    for index in (
    ["Drug", "Toxicity", "Toxicity_Grade", "Toxicity_Treatment", "Toxicity_Response", "ChangedTreatment_Toxicity"]):
        col_name = index + "_week"
        data_df = pd.DataFrame()
        data_df[col_name] = tox_cycle[["Week", index]].apply(lambda x: ':'.join(x), axis=1)
        data = list(data_df.loc[:, (col_name)])
        data = "|".join(data)
        data_cycle.append(data)
    dose_ = drug_cycle.loc[:, ("Drugs", "Dose")]
    dose_sum_cycle = dose_.groupby("Drugs").sum()
    drug_dose = []
    for index in range(0, len(list(dose_sum_cycle.index))):
        dose_unit_ = list(drug_cycle.loc[:, "Dose_unit"])[index]
        data = list(dose_sum_cycle.index)[index] + ": " + str(
            list(dose_sum_cycle.loc[:, "Dose"])[index]) + " " + dose_unit_
        drug_dose.append(data)
    drug_dose = "|".join(drug_dose)
    return data_cycle, drug_dose