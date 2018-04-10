

def mammography(conn, cursor, file_number):
    module_name = "mammography"
    check = False
    while not check:
        mammo_loc = ask_y_n_statement.ask_option("Mammography Diagnosis at", ["PCCM", "Outside", "Other"])
        mammo_details = ask_y_n_statement.ask_y_n("First Mammography?")
        if mammo_details:
            mammo_date = input("Date when mammography done: ")
            mammo_details = "First Mammography"
            mammo_number, mammo_rep_previous = ("NA",) * 2
        else:
            mammo_date = input("Date of last mammography done: ")
            mammo_details = "More than one Mammography"
            mammo_number = input("Number of mammographies undergone: ")
            mammo_rep_previous = input("Report of previous mammography: ")
        mammo = ask_y_n_statement.ask_y_n("Mammography diagnosis done")
        if mammo:
            mammo = "Mammography diagnosis done"
            mammo_diag_date = input("Date of mammography diagnosis: ")
            mammo_diag_acc = input("Accession number of mammography diagnosis: ")
            breast_density = ask_y_n_statement.ask_option("Density of breast",
                                                          ["a. The breasts are almost entirely fatty",
                                                           "b. There are scattered areas of fibroglandular density",
                                                           "c. The breasts are heterogeneously dense, which may obscure"
                                                           " small masses", "d. The breasts are extremely "
                                                                            "dense which lowers the sensitivity of mammography"])
            mammo_mass_location = ask_y_n_statement.ask_y_n("Is there any mass detected")
            if mammo_mass_location:
                table = "Mammography_Multiple_Mass"
                mass_number, mammo_mass_location, mammo_mass_location_quad, mammo_mass_depth, mammo_mass_dist, \
                mammo_mass_pect, mammo_mass_shape, mammo_mass_margin, mammo_mass_density = radio_tables.multiple_mass(
                    table, conn, cursor, file_number)
            else:
                mass_number = "No mass detected"
                mammo_mass_location, mammo_mass_location_quad, mammo_mass_depth, mammo_mass_dist, mammo_mass_pect, \
                mammo_mass_shape, mammo_mass_margin, mammo_mass_density = ("NA",) * 8
            calc = ask_y_n_statement.ask_y_n("Is Calcification present?")
            if calc:
                calc_number, calc_location, location_quad, calc_depth, calc_dist, calc_pect, calc_name, calc_type, \
                calc_dist = radio_tables.cal_table(file_number, conn, cursor)
            else:
                calc_number = "No Calcification detected"
                calc_location, location_quad, calc_depth, calc_dist, calc_pect, calc_name, calc_type, calc_dist = \
                    ("NA",) * 8
            arch_loc, arch_quad, arch_depth, arch_dist, arch_pect = radio_tables.mammo_arch()
            asym_loc, asym_quad, asym_depth, asym_dist, asym_pect, mammo_asymm = radio_tables.mammo_asym()
            intra_lymph = ask_y_n_statement.ask_y_n("Are intra-mammary lymph nodes present?")
            if intra_lymph:
                mammo_intra = input("Description of intra-mammary lymph nodes: ")
            else:
                mammo_intra = "Intra-mammary lymph nodes not present"
            lesion = ask_y_n_statement.ask_y_n("Skin Lesion present?")
            if lesion:
                mammo_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                            ["Right Breast", "Left Breast", "Both"])
            else:
                mammo_lesion = "NA"
            asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, \
            asso_feat_7 = radio_tables.mammo_asso_feat()
            mammo_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/diagnosis?")
            if mammo_birad:
                mammo_birad, mammo_diag = radio_tables.birads()
            else:
                mammo_birad, mammo_diag = ("NA",) * 2
        else:
            mammo = "Mammography diagnosis not done"
            mammo_diag_date, mammo_diag_acc, breast_density, mass_number, mammo_mass_location, mammo_mass_location_quad, \
            mammo_mass_depth, mammo_mass_dist, mammo_mass_pect, mammo_mass_shape, mammo_mass_margin, mammo_mass_density, \
            calc_number, calc_location, location_quad, calc_depth, calc_dist, calc_pect, calc_name, calc_type, \
            calc_dist, arch_loc, arch_quad, arch_depth, arch_dist, arch_pect, asym_quad, asym_depth, asym_dist, \
            asym_pect, mammo_asymm, mammo_intra, mammo_lesion, asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, \
            asso_feat_5, asso_feat_6, asso_feat_7, mammo_birad, mammo_diag = ("NA",) * 42
        data_list = [mammo_loc, mammo_date, mammo_details, mammo_number, mammo_rep_previous, mammo, mammo_diag_date,
                     mammo_diag_acc, breast_density, mass_number, mammo_mass_location, mammo_mass_location_quad,
                     mammo_mass_depth, mammo_mass_dist, mammo_mass_pect, mammo_mass_shape, mammo_mass_margin,
                     mammo_mass_density, calc_number, calc_location, location_quad, calc_depth, calc_dist, calc_pect,
                     calc_name, calc_type, calc_dist, arch_loc, arch_quad, arch_depth, arch_dist, arch_pect, asym_quad,
                     asym_depth, asym_dist, asym_pect, mammo_asymm, mammo_intra, mammo_lesion, asso_feat_1, asso_feat_2,
                     asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, mammo_birad, mammo_diag]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


