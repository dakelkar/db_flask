import modules.ask_y_n_statement as ask_y_n_statement
from sql.add_update_sql import review_input, update_multiple, review_data
import modules.pccm_names as names
from datetime import datetime


def radiation (file_number, user_name):
    check = False
    while not check:
        radio = ask_y_n_statement.ask_y_n("Radiotherapy Recieved?")
        if not radio:
            radio = ask_y_n_statement.ask_option("Reason for not recieving radiotherapy", ["Not indicated", "Unable to afford",
                                                                                           "Patients reluctance",
                                                                                           "Logistic concerns"])
            radio_date,  radio_type, imrt, radio_tox, radio_delayed_tox, radio_finish, radio_location, radio_onco = ("NA", )*8
        else:
            radio = "Radiation therapy recieved"
            radio_date = input("Date of starting radiotherapy")
            radio_type = ask_y_n_statement.ask_option("Type of radiotherapy", ["Cobalt",
                                                                                "Linear Accelerator "
                                                                                "based treatment",
                                                                               "Not known", "Other"])
            imrt = ask_y_n_statement.ask_y_n_na("Did the patient opt for Intensity Modulated/3Dimensional conformal radiotherapy ("
                                             "IMRT/3DCRT)")
            if imrt == "Yes":
                imrt = "patient opted for Intensity Modulated/3Dimensional conformal radiotherapy (IMRT/3DCRT)"
            if imrt == "No":
                imrt = ask_y_n_statement.ask_option("Reasons for not opting for IMRT/3DCRT", ["Financial", "Not advised",
                                                                                              "Not known"])
            radio_tox = ask_y_n_statement.ask_option("Did radiotherapy related acute toxicity occur?",
                                                     ["Yes", "No","Not known"])
            if radio_tox == "Yes":
                radio_tox = input("Type of toxicity: ")
            radio_delayed_tox = ask_y_n_statement.ask_option("Did radiotherapy related delayed toxicity occur?", ["Yes", "No",
                                                                                                        "Not known"])
            radio_finish = input ("Date of finishing radiotherapy: ")
            radio_location = input("Location of radiotherapy: ")
            radio_onco = ask_y_n_statement.ask_option("Name of Radiation Oncologist", ["Dr. Gautam Sharan", "Other"])
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = [radio, radio_date,  radio_type, imrt, radio_tox, radio_delayed_tox, radio_finish, radio_location,
                     radio_onco, user_name, last_update]
        col_list =names.names_radiation()
        check = review_input(file_number, col_list, data_list)
    return data_list


def add_data(conn, cursor, file_number, user_name):
    table = "Radiotherapy"
    col_list = names.names_radiation()
    data = radiation(file_number, user_name)
    update_multiple(conn, cursor, table, col_list, file_number, data)


def edit_data(conn, cursor, file_number, user_name):
    table = "Radiotherapy"
    col_list = names.names_radiation()
    enter = review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = radiation(file_number)
        update_multiple(conn, cursor, table, col_list, file_number, data)
