import modules.ask_y_n_statement as ask_y_n_statement
from sql.add_update_sql import review_df, view_multiple, delete_multiple, delete_rows
import modules.pccm_names as names
import pandas as pd
from datetime import datetime


def follow_up(file_number, user_name):
    follow = True
    follow_index = 0
    col_list = ["File_number"] + names.name_follow_up()
    follow_up_data = pd.DataFrame(columns=col_list)
    while follow:
        check = False
        while not check:
            time_follow = ask_y_n_statement.ask_option("Follow-up Period", ["3 months", "6 months", "9 months", "1 year",
                                                                           "1 year, 3 months", "1 year, 6 months",
                                                                           "1 year, 9 months", "2 years",
                                                                           "2 years, 6 months",
                                                                           "3 years", "3 years, 6 months", "4 years",
                                                                           "4 years, 6 months", "5 years", "6 years",
                                                                           "7 years", "8 years", "9 years", "10 years",
                                                                           "Other"])
            follow_notes = input ("Details of follow up information: ")
            follow_report = ask_y_n_statement.ask_y_n("Does follow-up contain other reports (USG/Mammography)?")
            follow_mammo, follow_usg = ("NA",)*2
            if follow_report:
                follow_mammo = input("Results of Mammography: ")
                follow_usg = input("Results of USG abdomen/Pelvis: ")
            follow_other = ask_y_n_statement.ask_y_n("Are there other reports in follow-up?")
            if not follow_other:
                other_type, other_result = ("NA", )*2
            else:
                other_type_list = []
                other_result_list = []
                while follow_other:
                    other_type = input("Type of other report: ")
                    other_result = input("Result of "+other_type+": ")
                    other_type_list.append(other_type)
                    other_result_list.append(other_result)
                    follow_other = ask_y_n_statement.ask_y_n("Add more reports?")
                all_data = [other_type_list, other_result_list]
                all_data = ask_y_n_statement.join_lists(all_data, "; ")
                other_type, other_result = all_data
            last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
            data_list = [file_number, time_follow, follow_notes, follow_mammo, follow_usg, other_type, other_result,
                         user_name, last_update]
            follow_up_data.loc[follow_index] = data_list
            check = review_df(follow_up_data.loc[follow_index])
        follow_index = follow_index + 1
        follow_up_period = list(follow_up_data.loc[:, "Follow_up_Period"])
        print("Follow up periods added: "+"; ".join(follow_up_period))
        follow = ask_y_n_statement.ask_y_n("Add another follow-up period?")
    return follow_up_data


def add_data(conn, file_number, user_name):
    data = follow_up(file_number, user_name)
    data.to_sql("Follow_up_Data", conn, index=False, if_exists="append")


def edit_data(conn, cursor, file_number, user_name):
    table = "Follow_up_Data"
    col_list = names.name_follow_up()
    enter = view_multiple(conn, table, col_list, file_number)
    if enter == "Add data":
        data = follow_up(file_number, user_name)
        data.to_sql("Follow_up_Data", conn, index=False, if_exists="append")
    if enter == "Re-enter data":
        table = "Follow_up_Data"
        col_list = ["File_number"] + names.name_follow_up()
        sql = ('SELECT ' + ", ".join(col_list[:-2]) + " FROM '" + table + "' WHERE File_number = '"+file_number+"'")
        df = pd.read_sql(sql, conn)
        follow_up_period = list(df.loc[:, "Follow_up_Period"])
        delete_data = True
        while delete_data:
            check_delete = False
            while not check_delete:
                col_data = ask_y_n_statement.ask_option("Which entry do you want to modify?", follow_up_period)
                check_delete = ask_y_n_statement.ask_y_n("Are you sure you want to delete data for follow-up period "+col_data)
            delete_rows(cursor, table,"Follow_up_Period", col_data)
            add_data(conn, file_number, user_name)
            delete_data = ask_y_n_statement.ask_y_n("Do you want to re-enter another follow up period")

