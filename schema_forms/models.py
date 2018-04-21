from create_hash import encodex
class FolderSection:
    def __init__(self, name, action, status, last_modified_by, last_modified_on):
        self.name = name
        self.action = action
        self.status = status
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on


class Patient_bio_info_Info:
    def __init__(self, folder_number, mr_number, name, aadhaar_card, date_first, permanent_address, current_address,
                 phone, email_id, gender, age_yrs, age_diagnosis, date_of_birth, place_birth, height_cm, weight_kg,
                 form_status, last_update):
        self.folder_number=folder_number
        self.mr_number=mr_number
        self.name=name
        self.aadhaar_card=aadhaar_card
        self.date_first=date_first
        self.permanent_address=permanent_address
        self.current_address=current_address
        self.phone=phone
        self.email_id=email_id
        self.gender=gender
        self.age_yrs=age_yrs
        self.age_diagnosis=age_diagnosis
        self.date_of_birth=date_of_birth
        self.place_birth=place_birth
        self.height_cm=height_cm
        self.weight_kg=weight_kg
        self.form_status=form_status
        self.last_update = last_update
        self.folder_hash = encodex(folder_number)

class BiopsyInfo:
    def __init__(self, folder_number, consent_stat_biopsy,consent_form_biopsy, block_serial_number_biopsy,
                 block_location_biopsy, block_current_location_biopsy, biopsy_custody_pccm, biopsy_block_id,
                 biopsy_block_number, biopsy_date, biopsy_lab_id, biopsy_type, biopsy_tumour_diagnosis,
                 biopsy_tumour_grade, biopsy_lymphovascular_emboli, dcis_biopsy, tumour_er_biopsy,
                 tumour_er_percent_biopsy, tumour_pr_biopsy, tumour_pr_percent_biopsy, tumour_her2_biopsy,
                 tumour_her2_grade_biopsy, tumour_ki67_biopsy, fnac, fnac_location, fnac_diagnosis):
        self.folder_number = folder_number
        self.consent_stat_biopsy = consent_stat_biopsy
        self.consent_form_biopsy = consent_form_biopsy
        self.block_serial_number_biopsy = block_serial_number_biopsy
        self.block_location_biopsy = block_location_biopsy
        self.block_current_location_biopsy = block_current_location_biopsy
        self.biopsy_custody_pccm = biopsy_custody_pccm
        self.biopsy_block_id = biopsy_block_id
        self.biopsy_block_number = biopsy_block_number
        self.biopsy_date = biopsy_date
        self.biopsy_lab_id = biopsy_lab_id
        self.biopsy_type = biopsy_type
        self.biopsy_tumour_diagnosis = biopsy_tumour_diagnosis
        self.biopsy_tumour_grade = biopsy_tumour_grade
        self.biopsy_lymphovascular_emboli = biopsy_lymphovascular_emboli
        self.dcis_biopsy = dcis_biopsy
        self.tumour_er_biopsy =tumour_er_biopsy
        self.tumour_er_percent_biopsy = tumour_er_percent_biopsy
        self.tumour_pr_biopsy = tumour_pr_biopsy
        self.tumour_pr_percent_biopsy = tumour_pr_percent_biopsy
        self.tumour_her2_biopsy = tumour_her2_biopsy
        self.tumour_her2_grade_biopsy = tumour_her2_grade_biopsy
        self.tumour_ki67_biopsy = tumour_ki67_biopsy
        self. fnac = fnac
        self.fnac_location = fnac_location
        self.fnac_diagnosis = fnac_diagnosis
        self.folder_hash = encodex(folder_number)

class MammographyInfo:
    def __init__(self, folder_number, mammo_location, mammo_details, mammo_date, mammo_accesion,mammo_number,
                mammo_report_previous, mammo_breast_density, mammo_mass_present, mammo_mass_number,
                mammo_mass_location_right_breast, mammo_mass_location_left_breast, mammo_mass_depth,mammo_mass_dist,
                mammo_mass_pect, mammo_mass_shape, mammo_mass_margin, mammo_mass_density, mammo_calcification_present,
                mammo_calc_number, mammo_calc_location_right_breast, mammo_calc_location_left_breast, mammo_calc_depth,
                mammo_calc_dist, mammo_calcification_type, mammo_calcification_diagnosis, mammo_arch_present,
                mammo_arch_location_right_breast, mammo_arch_location_left_breast, mammo_arch_depth, mammo_arch_dist,
                mammo_assym_present, mammo_assym_location_right_breast, mammo_assym_location_left_breast,
                mammo_assym_depth, mammo_assym_type_right_breast, mammo_assym_type_left_breast,
                mammo_intra_mammary_lymph_nodes_present, mammo_intra_mammary_lymph_nodes_description, mammo_lesion,
                mammo_lesion_right_breast, mammo_lesion_left_breast, mammo_asso_feature_skin_retraction,
                mammo_asso_feature_nipple_retraction, mammo_asso_feature_skin_thickening,
                mammo_asso_feature_trabecular_thickening, mammo_asso_feature_axillary_adenopathy,
                mammo_asso_feature_architectural_distortion, mammo_asso_feature_calicifications, mammo_birad):
        self.folder_number = folder_number
        self.mammo_location = mammo_location
        self.mammo_details = mammo_details
        self.mammo_date = mammo_date
        self.mammo_accesion = mammo_accesion
        self.mammo_number = mammo_number
        self.mammo_report_previous = mammo_report_previous
        self.mammo_breast_density = mammo_breast_density
        self.mammo_mass_present = mammo_mass_present
        self.mammo_mass_number = mammo_mass_number
        self.mammo_mass_location_right_breast = mammo_mass_location_right_breast
        self.mammo_mass_location_left_breast = mammo_mass_location_left_breast
        self.mammo_mass_depth = mammo_mass_depth
        self.mammo_mass_dist = mammo_mass_dist
        self.mammo_mass_pect = mammo_mass_pect
        self.mammo_mass_shape = mammo_mass_shape
        self.mammo_mass_margin = mammo_mass_margin
        self.mammo_mass_density = mammo_mass_density
        self.mammo_calcification_present = mammo_calcification_present
        self.mammo_calc_number = mammo_calc_number
        self.mammo_calc_location_right_breast = mammo_calc_location_right_breast
        self.mammo_calc_location_left_breast = mammo_calc_location_left_breast
        self.mammo_calc_depth = mammo_calc_depth
        self.mammo_calc_dist = mammo_calc_dist
        self.mammo_calcification_type = mammo_calcification_type
        self.mammo_calcification_diagnosis = mammo_calcification_diagnosis
        self.mammo_arch_present = mammo_arch_present
        self.mammo_arch_location_right_breast = mammo_arch_location_right_breast
        self.mammo_arch_location_left_breast = mammo_arch_location_left_breast
        self.mammo_arch_depth = mammo_arch_depth
        self.mammo_arch_dist = mammo_arch_dist
        self.mammo_assym_present = mammo_assym_present
        self.mammo_assym_location_right_breast = mammo_assym_location_right_breast
        self.mammo_assym_location_left_breast = mammo_assym_location_left_breast
        self.mammo_assym_depth = mammo_assym_depth
        self.mammo_assym_type_right_breast = mammo_assym_type_right_breast
        self.mammo_assym_type_left_breast = mammo_assym_type_left_breast
        self.mammo_intra_mammary_lymph_nodes_present = mammo_intra_mammary_lymph_nodes_present
        self.mammo_intra_mammary_lymph_nodes_description = mammo_intra_mammary_lymph_nodes_description
        self.mammo_lesion = mammo_lesion
        self.mammo_lesion_right_breast = mammo_lesion_right_breast
        self.mammo_lesion_left_breast = mammo_lesion_left_breast
        self.mammo_asso_feature_skin_retraction = mammo_asso_feature_skin_retraction
        self.mammo_asso_feature_nipple_retraction = mammo_asso_feature_nipple_retraction
        self.mammo_asso_feature_skin_thickening = mammo_asso_feature_skin_thickening
        self.mammo_asso_feature_trabecular_thickening = mammo_asso_feature_trabecular_thickening
        self.mammo_asso_feature_axillary_adenopathy = mammo_asso_feature_axillary_adenopathy
        self.mammo_asso_feature_architectural_distortion = mammo_asso_feature_architectural_distortion
        self.mammo_asso_feature_calicifications = mammo_asso_feature_calicifications
        self.mammo_birad = mammo_birad
        self.folder_hash = encodex(folder_number)