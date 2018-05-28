from modules.ask_y_n_statement import ask_y_n
from modules.pccm_names import names_radio as names
import modules.ask_y_n_statement as ask_y_n_statement
import sql.add_update_sql as add_update_sql
import additional_tables.radio_tables as radio_tables
from datetime import datetime

def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Radiology(File_number) VALUES ('" + file_number + "')")


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
                                                                            "dense which lowers the sensitivity of "
                                                                            "mammography"])
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
                calc_distribution = radio_tables.cal_table(file_number, conn, cursor)
            else:
                calc_number = "No Calcification detected"
                calc_location, location_quad, calc_depth, calc_dist, calc_pect, calc_name, calc_type, calc_distribution = \
                    ("NA",) * 8
            mammo_arch, arch_loc, arch_quad, arch_depth, arch_dist, arch_pect = radio_tables.mammo_arch()
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
            calc_distribution, mammo_arch, arch_loc, arch_quad, arch_depth, arch_dist, arch_pect, asym_loc, asym_quad, asym_depth, asym_dist, \
            asym_pect, mammo_asymm, mammo_intra, mammo_lesion, asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, \
            asso_feat_5, asso_feat_6, asso_feat_7, mammo_birad, mammo_diag = ("NA",) * 42
        data_list = [mammo_loc, mammo_details, mammo_date, mammo_number, mammo_rep_previous, mammo, mammo_diag_date,
                     mammo_diag_acc, breast_density, str(mass_number), mammo_mass_location, mammo_mass_location_quad,
                     mammo_mass_depth, mammo_mass_dist, mammo_mass_pect, mammo_mass_shape, mammo_mass_margin,
                     mammo_mass_density, calc_number, calc_location, location_quad, calc_depth, calc_dist, calc_pect,
                     calc_name, calc_type, calc_distribution, mammo_arch, arch_loc, arch_quad, arch_depth, arch_dist,
                     arch_pect, asym_loc, asym_quad, asym_depth, asym_dist, asym_pect, mammo_asymm, mammo_intra, mammo_lesion,
                     asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7,
                     mammo_birad, mammo_diag]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


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


def abvs(file_number):
    module_name = "abvs"
    check = False
    while not check:
        abvs = ask_y_n_statement.ask_y_n("Automated Breast Volume Scanner (ABVS) done?")
        if abvs:
            abvs = "Automated Breast Volume Scanner done"
            abvs_date = input("Date of examination of ABVS: ")
            abvs_acc = input("Accession number of ABVS: ")
            abvs_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                       ["Right Breast", "Left Breast", "Both", "Not present"])
            if abvs_lesion in {"Right Breast", "Left Breast", "Both"}:
                abvs_lesion_data = radio_tables.lesion_location(abvs_lesion)
            else:
                abvs_lesion_data = "NA"
            abvs_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            abvs_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            abvs_pect = input("Distance from Pectoralis Major (cm): ")
            abvs_diagnosis = ask_y_n_statement.ask_option("ABVS Diagnosis",
                                                          ["Normal", "Benign", "Suspicious", "Diagnostic for Cancer"])
        else:
            abvs = "Automated Breast Volume Scanner done"
            abvs_date, abvs_acc, abvs_lesion, abvs_lesion_data, abvs_size, abvs_dist, abvs_pect, \
            abvs_diagnosis = ("NA",) * 8

        data_list = [abvs, abvs_date, abvs_acc, abvs_lesion, abvs_lesion_data, abvs_size, abvs_dist, abvs_pect,
                     abvs_diagnosis]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def sonomammo(conn, cursor, file_number):
    module_name = "sonomammo"
    check = False
    while not check:
        sonomammo = ask_y_n_statement.ask_y_n("Sono-Mammography done?")
        if sonomammo:
            sonomammo = "Sono-Mammography done"
            sonomammo_date = input("Date of examination of Sono-mammography: ")
            sonomammo_acc = input("Accession number of Sono-Mammography: ")
            sonomammo_tissue = ask_y_n_statement.ask_option("Tissue Composition",
                                                            ["a. Homogeneous background echotexture – fat",
                                                             "b. Homogeneous background echotexture – fibroglandular",
                                                             "c. Heterogeneous background echotexture", "Other"])
            mass_sonomammo = ask_y_n_statement.ask_y_n("Is there any mass detected")
            if mass_sonomammo:
                table = "SonnoMammography_Multiple_Mass"
                mass_number_sonomammo, mass_location, mass_quad, mass_clock, mass_depth, mass_distance, mass_pect, \
                mass_shape_sonomammo, mass_orientation_sonomammo, mass_margin_sonomammo, mass_echo_sonomammo, \
                mass_posterior_sonomammo = radio_tables.multiple_mass(table, conn, cursor, file_number)
            else:
                mass_number_sonomammo = "No Mass Detected"
                mass_location, mass_quad, mass_clock, mass_depth, mass_distance, mass_pect, mass_shape_sonomammo, \
                mass_orientation_sonomammo, mass_margin_sonomammo, mass_echo_sonomammo, \
                mass_posterior_sonomammo = ("NA",) * 11
            sonomammo_calc = ask_y_n_statement.ask_option("Calcification",
                                                          ["Right Breast", "Left Breast", "Both", "Not present", "Other"])
            if sonomammo_calc == "Not present":
                sonomammo_calc_type = "NA"
            else:
                sonomammo_calc_type = ask_y_n_statement.ask_option("Calcification location",
                                                                   ["Calcifications in a mass",
                                                                    "Calcifications outside of a mass",
                                                                    "Intraductal calcifications"])
            sonomammo_arch = ask_y_n_statement.ask_option("Architectural distortion",
                                                          ["Right Breast", "Left Breast", "Both", "Not present", "Other"])
            sonomammo_duct = ask_y_n_statement.ask_option("Duct Changes",
                                                          ["Right Breast", "Left Breast", "Both", "Not present", "Other"])
            sonomammo_skin = ask_y_n_statement.ask_y_n("Skin Changes")
            if sonomammo_skin:
                sonomammo_skin = ask_y_n_statement.ask_option("Type of skin changes",
                                                              ["Skin thickening", "Skin retraction"])
            else:
                sonomammo_skin = "No skin changes"
            sonomammo_edema = ask_y_n_statement.ask_option("Edema",
                                                           ["Right Breast", "Left Breast", "Both", "Not present", "Other"])
            sonomammo_vasc = ask_y_n_statement.ask_option("Vascularity",
                                                          ["Absent", "Internal vascularity", "Vessels in rim", "Other"])
            sonomammo_elast = ask_y_n_statement.ask_option("Elasticity assessment",
                                                           ["Soft", "Intermediate", "Hard", "Other"])
            sonomammo_lymph_intra = input("Description of intramammary lymph nodes: ")
            sonomammo_lymph_ax = ask_y_n_statement.ask_option("Axillary Lymph Nodes", ["Normal", "Abnormal"])
            if sonomammo_lymph_ax == "Abnormal":
                lymph_ax_cort = input("Cortical thickness: ")
                lymph_ax_hilum = ask_y_n_statement.ask_option("Axillary lymph node hilum",
                                                              ["Lost", "Thin", "Preserved", "Other"])
                lymph_ax_vasc = ask_y_n_statement.ask_option("Axillary lymph node vascularity",
                                                             ["Ventral", "Peripheral", "Other"])
            else:
                lymph_ax_cort, lymph_ax_hilum, lymph_ax_vasc = ("NA",) * 3
            sonomammo_sol_duct = ask_y_n_statement.ask_y_n("Is solitary dilated duct present?")
            if sonomammo_sol_duct:
                sol_duct_loc = ask_y_n_statement.ask_option("Location of Solitary Dilated duct",
                                                            ["Right Breast", "Left Breast", "Both"])
                sol_duct_diam = input("Diameter of solitary dilated duct (mm): ")
                sol_mass = ask_y_n_statement.ask_y_n("Is Intra-ductal solid mass present?",
                                                     "Intra-ductal Solid Mass Present",
                                                     "Intra-ductal Solid Mass Absent")
            else:
                sol_duct_loc = "Not Present"
                sol_duct_diam, sol_mass = ("NA",) * 2
            sonomammo_shear = input("Strain and shear wave velocity on elastography type/pattern: ")
            sonomammo_vtq = input("Median Shear Velocity (VTQ) in m/s: ")
            other = ask_y_n_statement.ask_y_n("Are there any other findings?")
            if other:
                print("If more than one other finding, chose Other and enter findings separated by ; ")
                sonomammo_other = ask_y_n_statement.ask_option("Other Findings", ["Simple cyst", "Clustered microcysts",
                                                                                  "Complicated cyst",
                                                                                  "Mass in or on skin",
                                                                                  "Foreign body including implants",
                                                                                  "Vascular abnormalities",
                                                                                  "AVMs (arteriovenous malformations/"
                                                                                  "pseudoaneurysms)",
                                                                                  "Mondor disease",
                                                                                  "Postsurgical ﬂuid collection",
                                                                                  "Fat necrosis", "Other"])
            else:
                sonomammo_other = "NA"
            sono_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/Diagnosis?")
            if sono_birad:
                sonomammo_birad, sonomammo_diag = radio_tables.birads()
            else:
                sonomammo_birad, sonomammo_diag = ("NA",) * 2
        else:
            sonomammo = "Sono-Mammography not done"
            sonomammo_date, sonomammo_acc, sonomammo_tissue, mass_number_sonomammo, mass_location, mass_quad, \
            mass_clock, mass_depth, mass_distance, mass_pect, mass_shape_sonomammo, mass_orientation_sonomammo, \
            mass_margin_sonomammo, mass_echo_sonomammo, mass_posterior_sonomammo, sonomammo_calc, sonomammo_calc_type, \
            sonomammo_arch, sonomammo_duct, sonomammo_skin, sonomammo_edema, sonomammo_vasc, sonomammo_elast, \
            sonomammo_lymph_intra, sonomammo_lymph_ax, lymph_ax_cort, lymph_ax_hilum, lymph_ax_vasc, sol_duct_loc, \
            sol_duct_diam, sol_mass, sonomammo_other, sonomammo_shear, sonomammo_vtq, sonomammo_birad, \
            sonomammo_diag = ("NA",) * 36
        data_list = [sonomammo, sonomammo_date, sonomammo_acc, sonomammo_tissue, mass_number_sonomammo, mass_location,
                     mass_quad, mass_clock, mass_depth, mass_distance, mass_pect, mass_shape_sonomammo,
                     mass_orientation_sonomammo, mass_margin_sonomammo, mass_echo_sonomammo, mass_posterior_sonomammo,
                     sonomammo_calc, sonomammo_calc_type, sonomammo_arch, sonomammo_duct, sonomammo_skin,
                     sonomammo_edema, sonomammo_vasc, sonomammo_elast, sonomammo_lymph_intra, sonomammo_lymph_ax,
                     lymph_ax_cort, lymph_ax_hilum, lymph_ax_vasc, sol_duct_loc, sol_duct_diam, sol_mass,
                     sonomammo_shear, sonomammo_vtq, sonomammo_other, sonomammo_birad, sonomammo_diag]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def mri_breast(conn, cursor, file_number, user_name):
    module_name = "mri_breast"
    check = False
    while not check:
        mri_breast = ask_y_n_statement.ask_y_n("Has MRI-Breast been done?")
        if mri_breast:
            mri_breast = "MRI-Breast done"
            mri_breast_date = input("Date of examination of MRI: ")
            mri_breast_acc = input("Accession number of MRI (Include location): ")
            fgt_mri = ask_y_n_statement.ask_option("Ammount of Fibroglandular Tissue",
                                                   ["a. Almost entirely fat", "b. Scattered fibroglandular tissue",
                                                    "c. Heterogeneous fibroglandular tissue",
                                                    "d. Extreme fibroglandular tissue", "Other"])
            bpe_level_mri = ask_y_n_statement.ask_option("Background parenchymal enhancement Level",
                                                         ["Minimal", "Mild", "Moderate", "Marked", "Other"])
            bpe_symm_mri = ask_y_n_statement.ask_option("Background parenchymal enhancement Symmetry",
                                                        ["Symmetric", "Asymmetric", "Other"])
            focus_mri = input("Details of Focus: ")
            mass_mri = ask_y_n_statement.ask_y_n("Are masses detected?")
            if mass_mri:
                mass_mri = "Mass Detected"
                table = "MRI_Multiple_Mass"
                mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal = \
                    radio_tables.multiple_mass(table, conn, cursor, file_number)
            else:
                mass_mri = "No Mass Detected"
                mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal = ("NA",) * 6
            asso_feat = ["Nipple Retraction", "Nipple Invasion", "Skin Retraction", "Skin Thickening",
                         "Axillary adenopathy", "Pectoralis muscle invasion", "Chest wall invasion",
                         "Architectural Distortion"]
            asso_feat_data = []
            for index in (asso_feat):
                print("Associated feature: " + index)
                print("Detailed description can be added by choosing 'Other'")
                var = ask_y_n_statement.ask_option(index,
                                                   ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
                asso_feat_data.append(var)
            asso_feat_9 = ask_y_n_statement.ask_option("Associated Feature: Skin Invasion",
                                                       ["Direct invasion", "Inﬂammatory cancer", "Other"])
            asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, \
            asso_feat_8 = asso_feat_data
            fat_lesions = ask_y_n_statement.ask_option("Fat Containing Lesions",
                                                       ["Lymph nodes: Normal", "Lymph nodes: Abnormal", "Fat necrosis",
                                                        "Hamartoma", "Postoperative seroma", "hematoma with fat"])
            mri_breast_kinetics_initial = ask_y_n_statement.ask_option("Kinetic curve assessment Signal intensity "
                                                                       "(SI)/time curve description (Initial Phase)",
                                                                       ["Slow", "Medium", "Fast", "Other"])
            mri_breast_kinetics_delayed = ask_y_n_statement.ask_option("Kinetic curve assessment Signal intensity "
                                                                       "(SI)/time curve description (Delayed Phase)",
                                                                       ["Persistent", "Plateau", "Washout", "Other"])
            mri_breast_non_enhance = ask_y_n_statement.ask_option("Non-enhancing findings",
                                                                  ["Ductal precontrast high signal on T1W", "Cyst",
                                                                   "Postoperative collections (hematoma/seroma)",
                                                                   "Post-therapy skin thickening and trabecular "
                                                                   "thickening","Signal void from foreign bodies, "
                                                                                "clips, etc.", "Other"])
            mri_breast_implant = input("Implant related findings: ")
            mri_breast_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                             ["Right Breast", "Left Breast", "Both", "Not present"])
            if mri_breast_lesion in {"Right Breast", "Left Breast", "Both"}:
                mri_breast_lesion_location = radio_tables.lesion_location(mri_breast_lesion)
                mri_breast_lesion_depth = input("Lesion depth: ")
            else:
                mri_breast_lesion_location, mri_breast_lesion_depth = ("NA",) * 2
            mri_breast_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            mri_breast_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            mri_breast_pect = input("Distance from Pectoralis Major (cm): ")
            mri_breast_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/Diagnosis?")
            if mri_breast_birad:
                mri_breast_birad, mri_breast_birad_diag = radio_tables.birads()
            else:
                mri_breast_birad, mri_breast_birad_diag = ("NA",) * 2
        else:
            mri_breast = "MRI-Breast not done"
            mri_breast_date, mri_breast_acc, fgt_mri, bpe_level_mri, bpe_symm_mri, focus_mri, mass_mri, mri_mass_number, \
            mass_location, mass_quad, mass_shape, mass_margin, mass_internal, asso_feat_1, asso_feat_2, asso_feat_3, \
            asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, asso_feat_8, asso_feat_9, fat_lesions, \
            mri_breast_lesion, mri_breast_lesion_location, mri_breast_lesion_depth, mri_breast_kinetics_initial, \
            mri_breast_kinetics_delayed, mri_breast_non_enhance, mri_breast_implant, mri_breast_size, mri_breast_dist, \
            mri_breast_pect, mri_breast_birad, mri_breast_birad_diag = ("NA",) * 35
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = [mri_breast, mri_breast_date, mri_breast_acc, fgt_mri, bpe_level_mri, bpe_symm_mri, focus_mri,
                     mass_mri, mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal,
                     asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7,
                     asso_feat_8, asso_feat_9, fat_lesions, mri_breast_kinetics_initial, mri_breast_kinetics_delayed,
                     mri_breast_non_enhance, mri_breast_implant, mri_breast_lesion, mri_breast_lesion_location,
                     mri_breast_lesion_depth, mri_breast_size, mri_breast_dist, mri_breast_pect, mri_breast_birad,
                     mri_breast_birad_diag, user_name, last_update]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def add_data(conn, cursor, file_number, user_name):
    table = "Radiology"
    #file_row(cursor, file_number)
    enter = ask_y_n("Enter Mammography Report?")
    if enter:
        data = mammography(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("mammography"), file_number, data)
    enter = ask_y_n("Enter 3D Tomosynthesis?")
    if enter:
        data = tomosynthesis(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("tomosynthesis"), file_number, data)
    enter = ask_y_n("Enter Automated Breast Volume Scanner")
    if enter:
        data = abvs(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("abvs"), file_number, data)
    enter = ask_y_n("Enter Sono-Mammography")
    if enter:
        data = sonomammo(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("sonomammo"), file_number, data)
    enter = ask_y_n("Enter MRI-Breast")
    if enter:
        data = mri_breast(conn, cursor, file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, names("mri_breast"), file_number, data)


def edit_data(conn, cursor, file_number, user_name):
    table = "Radiology"
    print("Mammography")
    col_list = names("mammography")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        tables = ['Calcification_Mammography', 'Mammography_Multiple_Mass']
        for i in tables:
            add_update_sql.delete_multiple(cursor, i, file_number)
        data = mammography(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("3D-Tomosynthesis")
    col_list = names("tomosynthesis")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = tomosynthesis(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Automated Breast Volume Scan")
    col_list = names("abvs")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = abvs(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Sono-Mammography")
    col_list = names("sonomammo")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        add_update_sql.delete_multiple(cursor, 'SonnoMammography_Multiple_Mass', file_number)
        data = sonomammo(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("MRI Breast")
    col_list = names("mri_breast")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        add_update_sql.delete_multiple(cursor, 'MRI_Multiple_Mass', file_number)
        data = mri_breast(conn, cursor, file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
