def tomosynthesis(file_number):
    module_name = "tomosynthesis"
    check = False
    while not check:
        tomo = ask_y_n_statement.ask_y_n("3D digital Tomosynthesis done")
        if tomo:
            tomo = "3D digital Tomosynthesis done"
            print ("Please add details of tomography in mammography section")
            tomo_date = input("Date of Tomosynthesis examination: ")
            tomo_acc = input("Accession number of Tomosynthesis: ")
        else:
            tomo = "3D digital Tomosynthesis not done"
            tomo_date, tomo_acc, = ("NA",) * 2

        data_list = [tomo, tomo_date, tomo_acc, ]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))



