def clinical_tests(test):
    import modules.ask_y_n_statement as ask_y_n_statement
    test_name = test[0]
    data_list = []
    test_done = ask_y_n_statement.ask_y_n("Has "+test_name+" been done?")
    if test_done:
        test_done = test_name+" done"
        data_list.append(test_done)
        for index in range(1, len(test)):
            abnormal = test[index]
            test_diag = ask_y_n_statement.ask_option("Diagnosis", ["Normal", abnormal])
            data_list.append(test_diag)
            if test_diag == abnormal:
                test_details = input("Please provide details of "+abnormal+" diagnosis: ")
            else:
                test_details = "NA"
            data_list.append(test_details)
    else:
        test_done = test_name+" not done"
        data_list.append(test_done)
        for index in range(1, len(test)):
            not_done = ("NA", )*2
            data_list.append(not_done)
    return data_list


def multiple_mass(table, conn, cursor, file_number):
    import modules.ask_y_n_statement as ask_y_n_statement
    import sql.add_update_sql as add_update_sql
    import modules.pccm_names as pccm_names

    mass_number = int(input("Number of masses detected: "))
    if table == "SonnoMammography_Multiple_Mass":
        sonno_quad, sonno_location, sonno_clock, sonno_shape,  sonno_depth, sonno_distance, sonno_pect,sonno_orientation,\
        sonno_margin, sonno_echo, sonno_posterior = [list([]) for _ in range(11)]
    if table == "Mammography_Multiple_Mass":
        location,quad, pect, depth, distance, shape, margin, density = [list([]) for _ in range(8)]
    if table == "MRI_Multiple_Mass":
        location, quad, shape, margin, internal = [list([]) for _ in range(5)]
    for index in range(0, mass_number):
        check = False
        while not check:
            mass_id = index + 1
            if table == "Mammography_Multiple_Mass":
                mass_location = ask_y_n_statement.ask_option("Location of mass " + str(mass_id),
                                                             ["Right Breast", "Left Breast"])
                location_quad = lesion_location(mass_location)
                mass_depth = ask_y_n_statement.ask_option("Depth of " + str(mass_id), ["Anterior", "Middle",
                             "Posterior", "Other"])
                mass_dist = ask_y_n_statement.ask_option("Distance from nipple", ["<0.5 cm", ">0.5 cm", "Other"])
                pect_check = ask_y_n_statement.ask_y_n("Is distance from Pectoralis Major described for " + str(mass_id))
                if pect_check:
                    mass_pect = input("Distance from Pectoralis Major (cm): ")
                else:
                    mass_pect = "Distance from Pectoralis Major not described"
                depth.append(mass_depth)
                location.append(mass_location)
                distance.append(mass_dist)
                quad.append(location_quad)
                pect.append(mass_pect)
                mammo_mass_shape = ask_y_n_statement.ask_option("Shape of mass", ["Oval", "Round", "Irregular", "Other"])
                shape.append(mammo_mass_shape)
                mammo_mass_margin = ask_y_n_statement.ask_option("Margins of mass",
                                                             ["Circumscribed", "Obscured", "Microlobulated", "Indistinct",
                                                              "Spiculated", "Other"])
                margin.append(mammo_mass_margin)
                mammo_mass_density = ask_y_n_statement.ask_option("Density of mass",
                                                              ["High density", "Equal density", "Low density",
                                                               "Fat-containing", "Other"])
                density.append(mammo_mass_density)
                mass_id = "Mass " + str(index + 1)
                data_list = [file_number, mass_id, mass_location, location_quad,  mass_depth, mass_dist, mass_pect,
                             mammo_mass_shape,mammo_mass_margin, mammo_mass_density]
            elif table == "MRI_Multiple_Mass":
                mass_location = ask_y_n_statement.ask_option("Location of mass " + str(mass_id),
                                                             ["Right Breast", "Left Breast"])
                location.append(mass_location)
                location_quad = lesion_location(mass_location)
                quad.append(location_quad)
                mri_mass_shape = ask_y_n_statement.ask_option("Shape of mass", ["Oval", "Round", "Irregular", "Other"])
                shape.append(mri_mass_shape)
                mri_mass_margin = ask_y_n_statement.ask_option("Margins of mass",
                                                                 ["Circumscribed", "Not circumscribed", "Other"])
                if mri_mass_margin == "Not circumscribed":
                    mri_mass_notc = ask_y_n_statement.ask_option("Not circumscribed margins of mass", ["Irregular",
                                                                                                       "Spiculated"])
                    mri_mass_margin = mri_mass_margin + ": " + mri_mass_notc

                margin.append(mri_mass_margin)
                mri_mass_internal = ask_y_n_statement.ask_option("Internal enhancement characteristics",
                                                                  ["Homogeneous", "Heterogeneous", "Rim enhancement",
                                                                   "Dark internal septations"])
                internal.append(mri_mass_internal)
                mass_id = "Mass " + str(index + 1)
                data_list = [file_number, mass_id, mass_location, location_quad, mri_mass_shape, mri_mass_margin,
                             mri_mass_internal]
            elif table == "SonnoMammography_Multiple_Mass":
                mass_location = ask_y_n_statement.ask_option("Location of mass "+str(mass_id), ["Right Breast",
                                                                                                "Left Breast"])
                sonno_location.append(mass_location)
                location_quad = lesion_location(mass_location)
                sonno_quad.append(location_quad)
                location_clock = input("What is the clock position of mass "+str(mass_id)+"?")
                location_clock = location_clock + " o'clock"
                sonno_clock.append(location_clock)
                mass_shape = ask_y_n_statement.ask_option("Shape of mass " + str(mass_id), ["Oval", "Round",
                                                                                            "Irregular", "Other"])
                mass_depth = input("Depth of mass " + str(mass_id)+"(cm): ")
                mass_dist = ask_y_n_statement.ask_option("Distance from nipple", ["<0.5 cm", ">0.5 cm", "Other"])
                pect_check = ask_y_n_statement.ask_y_n(
                    "Is distance from Pectoralis Major described for mass " + str(mass_id))
                if pect_check:
                    mass_pect = input("Distance from Pectoralis Major (cm): ")
                else:
                    mass_pect = "NA"
                sonno_depth.append(mass_depth)
                sonno_distance.append(mass_dist)
                sonno_pect.append(mass_pect)
                sonno_shape.append(mass_shape)
                mass_orientation = ask_y_n_statement.ask_option("Orientation of mass " + str(mass_id), ["Parallel",
                                                                                                        "Not parallel"])
                sonno_orientation.append(mass_orientation)
                mass_margin = ask_y_n_statement.ask_option("Margin of mass " + str(mass_id), ["Circumscribed",
                                                                                              "Not circumscribed"])
                if mass_margin == "Not circumscribed":
                    mass_margin = ask_y_n_statement.ask_option("Is Not circumscribed margin" , ["Indistinct", "Angular",
                                                                                                "Microlobulated",
                                                                                                "Spiculated"])
                sonno_margin.append(mass_margin)
                mass_echo = ask_y_n_statement.ask_option("Echo pattern of mass "+ str(mass_id), ["Anechoic",
                                                                                                 "Hyperechoic",
                                                                                                 "Complex cystic "
                                                                                                 "and solid",
                                                                                                 "Hypoechoic",
                                                                                                 "Isoechoic",
                                                                                                 "Heterogeneous",
                                                                                                 "Other"])
                sonno_echo.append(mass_echo)
                mass_posterior = ask_y_n_statement.ask_option("Posterior Acoustic features", ["No posterior features",
                                                                                              "Enhancement","Shadowing",
                                                                                              "Combined pattern",
                                                                                              "Other"])
                sonno_posterior.append(mass_posterior)
                mass_id = "Mass "+ str(index+1)
                data_list = [file_number, mass_id, mass_location, location_quad, location_clock, mass_depth,
                             mass_location,mass_dist, mass_shape, mass_orientation, mass_margin, mass_echo,
                             mass_posterior]
            col_list = pccm_names.names_radio(table)
            check = add_update_sql.review_input(file_number, col_list, data_list)
        columns = ", ".join(col_list)
        add_update_sql.insert(conn, cursor, table, columns, tuple(data_list))
    if table == "SonnoMammography_Multiple_Mass":
        all_data = [[str(mass_number)],sonno_quad, sonno_location, sonno_clock, sonno_depth, sonno_distance, sonno_pect,
                    sonno_shape, sonno_orientation, sonno_margin, sonno_echo, sonno_posterior]
    elif table == "Mammography_Multiple_Mass":
        all_data = [[str(mass_number)], location, quad,  depth, distance, pect, shape, margin, density]
    elif table == "MRI_Multiple_Mass":
        all_data = [[str(mass_number)], location, quad, shape, margin, internal]
    else:
        all_data = []
    data_return = ask_y_n_statement.join_lists(all_data, "; ")
    return tuple(data_return)


def birads ():
    import modules.ask_y_n_statement as ask_y_n_statement

    mammo_birads = ask_y_n_statement.ask_option("BI-RADS", ["0", "I", "II", "III", "IV", "IVA", "IVB", "IVC", "V", "Other"])
    check = False
    while not check:
        if mammo_birads == "0":
            mammo_birads_det = "Incomplete – Need Additional Imaging Evaluation"
        elif mammo_birads == "I":
            mammo_birads_det = "Negative"
        elif mammo_birads == "II":
            mammo_birads_det = "Benign"
        elif mammo_birads == "III":
            mammo_birads_det = "Probably Benign"
        elif mammo_birads == "IV":
            mammo_birads_det = "Suspicious"
        elif mammo_birads == "IVA":
            mammo_birads_det = "Low suspicion for malignancy"
        elif mammo_birads == "IVB":
            mammo_birads_det = "Moderate suspicion for malignancy"
        elif mammo_birads == "IVC":
            mammo_birads_det = "High suspicion for malignancy"
        elif mammo_birads == "V":
            mammo_birads_det = "Highly Suggestive of Malignancy"
        else:
            mammo_birads_det = input("Details of BI-RADS category: ")
        print ("BI-RAD " + mammo_birads + ": " + mammo_birads_det)
        check = ask_y_n_statement.ask_y_n("Is this correct?")
    data_list = [mammo_birads, mammo_birads_det]
    return tuple(data_list)


def cal_table (file_number, conn, cursor):
    import modules.ask_y_n_statement as ask_y_n_statement
    import sql.add_update_sql as add_update_sql
    import modules.pccm_names as pccm_names
    table = "Calcification_Mammography"
    mass_number = int(input("Number of groups of calcifications detected? "))
    location, quad, depth, dist, pect, type, calc_type, calc_diag, distribution= [list([]) for _ in range(9)]
    for index in range(0, mass_number):
        check = False
        while not check:
            mass_id = index + 1
            mass_location = ask_y_n_statement.ask_option("Location of calcification group " + str(mass_id),
                                                         ["Right Breast", "Left Breast"])
            location.append(mass_location)
            location_quad = lesion_location(mass_location)
            quad.append(location_quad)
            calc_depth = ask_y_n_statement.ask_option("Depth of group " + str(mass_id),
                                                      ["Anterior", "Middle", "Posterior", "Other"])
            calc_dist = ask_y_n_statement.ask_option("Distance from nipple of group " + str(mass_id), ["<0.5 cm", ">0.5 cm", "Other"])
            pect_check = ask_y_n_statement.ask_y_n("Is distance from Pectoralis Major described for  group " + str(mass_id))
            if pect_check:
                calc_pect = input("Distance from Pectoralis Major (cm) of group " + str(mass_id)+": ")
            else:
                calc_pect = "NA"
            depth.append(calc_depth)
            dist.append(calc_dist)
            pect.append(calc_pect)
            mammo_calcification = ask_y_n_statement.ask_option("Calcification Type",
                                                       ["Skin", "Vascular", "Coarse or 'Popcorn-like'",
                                                        "Large Rod-like", "Round and punctate", "Eggshell or Rim",
                                                        "Dystrophic", "Suture", "Amorphous", "Coarse Heterogeneous",
                                                        "Fine Pleomorphic", "Fine Linear or Fine Linear Branching",
                                                        "Other"])
            calc_type.append(mammo_calcification)
            if mammo_calcification in {"Skin", "Vascular", "Coarse or 'Popcorn-like'", "Large Rod-like", "Round and punctate",
                                       "Eggshell or Rim", "Dystrophic", "Suture"}:
                mammo_calcification_type = "Typically Benign"
                print("Calcification Type is " + mammo_calcification_type)
                check = ask_y_n_statement.ask_y_n("Is Calcification type correct?")
            elif mammo_calcification in {"Amorphous", "Coarse Heterogeneous", "Fine Pleomorphic",
                                         "Fine Linear or Fine Linear Branching"}:
                mammo_calcification_type = "Suspicious Morphology"
                print("Calcification Type is " + mammo_calcification_type)
                check = ask_y_n_statement.ask_y_n("Is Calcification type correct?")
            else:
                mammo_calcification_type = input("Calcification type " + mammo_calcification + "? ")
            if not check:
                mammo_calcification_type = input("Calcification type " + mammo_calcification + "? ")
            calc_diag.append(mammo_calcification_type)

            mammo_calcification_distribution = ask_y_n_statement.ask_option("Distribution of calcification",
                                                                    ["Diffuse", "Regional", "Grouped", "Linear",
                                                                     "Segmental"])
            distribution.append(mammo_calcification_distribution)
            mass_id = "Group " + str(index + 1)
            data_list = [file_number, mass_id, mass_location, location_quad, calc_depth,calc_dist, calc_pect,
                         mammo_calcification, mammo_calcification_type, mammo_calcification_distribution]
            col_list = pccm_names.names_radio(table)
            check = add_update_sql.review_input(file_number, col_list, data_list)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data_list)
    all_data = [[str(mass_number)], location, quad, depth, dist, pect, calc_type, calc_diag, distribution]
    data_return = ask_y_n_statement.join_lists(all_data, "; ")
    return tuple(data_return)

def lesion_location(lesion, category = ["Location on Right Breast", "Location on Left Breast"],
                    option = ["UOQ", "UIQ","UCQ", "LOQ","LIQ","LCQ", "COQ", "CIQ","CCQ", "Data not available", "Other"]):
    import modules.ask_y_n_statement as ask_y_n_statement
    lesion_data =[]
    if lesion in {"Right Breast", "Both"}:
        lesion_rb = ask_y_n_statement.ask_option(category[0], option)
        lesion_rb_data = "RB-" + lesion_rb
        lesion_data.append(lesion_rb_data)
    if lesion in {"Left Breast", "Both"}:
        lesion_lb = ask_y_n_statement.ask_option(category[1],option)
        lesion_lb_data = "LB-" + lesion_lb
        lesion_data.append(lesion_lb_data)
    lesion_data = "|".join(lesion_data)
    return lesion_data

def mammo_arch ():
    import modules.ask_y_n_statement as ask_y_n_statement
    mammo_arch = ask_y_n_statement.ask_y_n("Is Architectural distortion present")
    if mammo_arch:
        mammo_arch = "Architectural distortion present"
        arch_loc = ask_y_n_statement.ask_option("Location of Distortion", ["Right Breast", "Left Breast", "Both"])
        arch_quad =  lesion_location(arch_loc)
        arch_depth = ask_y_n_statement.ask_option("Depth of Architectural Distortion",
                                                  ["Anterior", "Middle", "Posterior", "Other"])
        arch_dist = ask_y_n_statement.ask_option("Distance from nipple of Architectural Distortion",
                                                 ["<0.5 cm", ">0.5 cm", "Other"])
        pect_check = ask_y_n_statement.ask_y_n("Is distance from Pectoralis Major described for "
                                               "Architectural Distortion")
        if pect_check:
            arch_pect = input("Distance from Pectoralis Major (cm): ")
        else:
            arch_pect = "NA"
    else:
        mammo_arch = "Architectural distortion not present"
        arch_loc = "Not Present"
        arch_quad, arch_depth, arch_dist, arch_pect = ("Not Present",) * 4
    data_list = [mammo_arch, arch_loc, arch_quad, arch_depth, arch_dist, arch_pect]
    return data_list

def mammo_asym():
    import modules.ask_y_n_statement as ask_y_n_statement
    asym = ask_y_n_statement.ask_y_n("Is asymmetry present")
    if asym:
        asym_loc = ask_y_n_statement.ask_option("Location of Asymmetry", ["Right Breast", "Left Breast", "Both"])
        asym_quad = lesion_location(asym_loc)
        asym_depth = ask_y_n_statement.ask_option("Depth of Asymmetry", ["Anterior", "Middle", "Posterior", "Other"])
        asym_dist = ask_y_n_statement.ask_option("Distance from nipple of Asymmetry", ["<0.5 cm", ">0.5 cm", "Other"])
        pect_check = ask_y_n_statement.ask_y_n("Is distance from Pectoralis Major described for Asymmetry")
        if pect_check:
            asym_pect = input("Distance from Pectoralis Major (cm): ")
        else:
            asym_pect = "NA"
        mammo_asymm = lesion_location(asym_loc, ["Type of Asymmetry in Right Breast",
                                                 "Type of Asymmetry in Left Breast"],
                                                ["Asymmetry", "Global asymmetry", "Focal asymmetry",
                                                    "Developing asymmetry", "Other"])
    else:
        asym_quad, asym_depth, asym_dist, asym_pect, mammo_asymm = ("NA",) * 5
        asym_loc = "Not Present"
    data_list = [asym_loc, asym_quad, asym_depth, asym_dist, asym_pect, mammo_asymm ]
    return data_list

def mammo_asso_feat():
    import modules.ask_y_n_statement as ask_y_n_statement
    asso_feat = ["Skin Retraction", "Nipple Retraction", "Skin Thickening", "Trabecular Thickening",
                 "Axillary adenopathy", "Architectural Distortion", "Calcifications"]
    asso_feat_data = []
    for index in asso_feat:
        print("Associated feature: " + index)
        print("Detailed description can be added by choosing 'Other'")
        var = ask_y_n_statement.ask_option(index, ["Present", "Absent", "Other"])
        asso_feat_data.append(var)
    return asso_feat_data

