from create_hash import encodex
class FolderSection:
    def __init__(self, name, action, status, last_modified_by, last_modified_on, pks, is_list):
        self.name = name
        self.action = action
        self.status = status
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        if pks is None:
            pks = []
        self.pks = pks
        self.is_list = is_list


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
    