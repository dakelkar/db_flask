import sys
import pymongo
from schema_forms import models
from datetime import datetime


class PatientsDb(object):
    # This class wraps the DB access for patients
    key = "folder_number"
    ###########################3
    # Patient_Info def

    def from_patient_bio_info_info(self, patient):
        return {
            self.key: patient.folder_number,
            "mr_number": patient.mr_number,
            "name": patient.name,
            "aadhaar_card": patient.aadhaar_card,
            "date_first": datetime.combine(patient.date_first, datetime.min.time()),
            "permanent_address": patient.permanent_address,
            "current_address": patient.current_address,
            "phone": patient.phone,
            "email_id": patient.email_id,
            "gender": patient.gender,
            "age_yrs": patient.age_yrs,
            "date_of_birth": datetime.combine(patient.date_of_birth, datetime.min.time()),
            "place_birth":  patient.place_birth,
            "height_cm": patient.height_cm,
            "weight_kg": patient.weight_kg
        }

    def to_patient_bio_info_info(self, p):
        patient_bio_info_info = models.Patient_bio_info_Info(folder_number=p[self.key], mr_number=p['mr_number'],
                                          name=p['name'], aadhaar_card=p['aadhaar_card'], date_first=p['date_first'].date(),
                                          permanent_address=p['permanent_address'],
                                          current_address=p['current_address'], phone=p['phone'],
                                          email_id=p['email_id'], gender=p['gender'], age_yrs=p['age_yrs'],
                                          date_of_birth=p['date_of_birth'].date(), place_birth=p['place_birth'],
                                          height_cm=p['height_cm'], weight_kg=p['weight_kg'])
        return patient_bio_info_info

    def __init__(self, logger):
        # Setup logging
        self.log = logger
        self.db = None

    def connect(self):
        # Connect to database
        try:
            client = pymongo.MongoClient("localhost", 27017)
            self.db = client.patients
            self.log.get_logger().info("Connection to patients database opened.")
        except:
            self.log.get_logger().error("Error connecting to database patients: %s", sys.exc_info())

    def get_patients(self):
        """
        :returns list of models.Patient_bio_info_Info
        """
        # try:
        patients = self.db.patients.find()
        return [self.to_patient_bio_info_info(p) for p in patients]
        # except:
        #     self.log.get_logger().error("Error retrieving patients from database: %s", sys.exc_info())
        #     return

    def get_patient(self, folder_number):
         # try:
        patient_entry = self.db.patients.find_one({ self.key: folder_number })
        patient = self.to_patient_bio_info_info(patient_entry)
        return patient
         # except:
         #    self.log.get_logger().error("Error retrieving patient %s from database: %s", folder_number, sys.exc_info())
         #    return

    def add_patient(self, patient):
        """
        adds a patient to the db
        :param models.Patient_bio_info_Info patient: the patient to insert
        """
        #try:
        patient_entry = self.from_patient_bio_info_info(patient)
        self.db.patients.insert_one(patient_entry)
        return True, None
        # except:
        #     self.log.get_logger().error("Error adding event to database: %s", sys.exc_info())
        #     return False, sys.exc_info()

    def update_patient(self, patient):
        """
        :param models.PatientForm patient: model to update from
        """
        try:
            self.db.patients.update_one({self.key: patient.folder_number },
                                        { "$set": self.from_patient_bio_info_info(patient)})
            return True, None
        except:
            self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
            return False, sys.exc_info()

    def delete_patient(self, folder_number):
        #try:
        self.db.patients.delete_one({self.key: folder_number})
        return True, None
        # except:
        #     self.log.get_logger().error("Error deleting patient %s from database: %s", folder_number, sys.exc_info())
        #     return False, sys.exc_info()

    ###########################3
    # Biopsy def

    def from_biopsy_info(self, biopsy):
        return {
            self.key: biopsy.folder_number,
            "consent_stat_biopsy": biopsy.consent_stat_biopsy,
            "consent_form_biopsy" : biopsy.consent_form_biopsy,
            "block_serial_number_biopsy" : biopsy.block_serial_number_biopsy,
            "block_location_biopsy" : biopsy.block_location_biopsy,
            "block_current_location_biopsy" : biopsy.block_current_location_biopsy,
            "biopsy_custody_pccm" : biopsy.biopsy_custody_pccm,
            "biopsy_block_id" : biopsy.biopsy_block_id,
            "biopsy_block_number" : biopsy.biopsy_block_number,
            "biopsy_date" : datetime.combine(biopsy.biopsy_date, datetime.min.time()),
            "biopsy_lab_id" : biopsy.biopsy_lab_id,
            "biopsy_type" : biopsy.biopsy_type,
            "biopsy_tumour_diagnosis" : biopsy.biopsy_tumour_diagnosis,
            "biopsy_tumour_grade" : biopsy.biopsy_tumour_grade,
            "biopsy_lymphovascular_emboli" : biopsy.biopsy_lymphovascular_emboli,
            "dcis_biopsy" : biopsy.dcis_biopsy,
            "tumour_er_biopsy" : biopsy.tumour_er_biopsy,
            "tumour_er_percent_biopsy" : biopsy.tumour_er_percent_biopsy,
            "tumour_pr_biopsy" : biopsy.tumour_pr_biopsy,
            "tumour_pr_percent_biopsy" : biopsy.tumour_pr_percent_biopsy,
            "tumour_her2_biopsy" : biopsy.tumour_her2_biopsy,
            "tumour_her2_grade_biopsy" : biopsy.tumour_her2_grade_biopsy,
            "tumour_ki67_biopsy" : biopsy.tumour_ki67_biopsy,
            "fnac" : biopsy.fnac,
            "fnac_location" : biopsy.fnac_location,
            "fnac_diagnosis" : biopsy.fnac_diagnosis
        }


    def to_biopsy_info(self, p):
        biopsy_info = models.BiopsyInfo(folder_number=p[self.key],
                    consent_stat_biopsy = p["consent_stat_biopsy"],consent_form_biopsy = p['consent_form_biopsy'],
                    block_serial_number_biopsy = p['block_serial_number_biopsy'],
                    block_location_biopsy = p['block_location_biopsy'],
                    block_current_location_biopsy = p['block_current_location_biopsy'],
                    biopsy_custody_pccm = p['biopsy_custody_pccm'],biopsy_block_id = p['biopsy_block_id'],
                    biopsy_block_number = p['biopsy_block_number'], biopsy_date = p['biopsy_date'].date(),
                    biopsy_lab_id = 'biopsy_lab_id', biopsy_type = p['biopsy_type'],
                    biopsy_tumour_diagnosis = p['biopsy_tumour_diagnosis'], biopsy_tumour_grade = p['biopsy_tumour_grade'],
                    biopsy_lymphovascular_emboli = p['biopsy_lymphovascular_emboli'], dcis_biopsy = p['dcis_biopsy'],
                    tumour_er_biopsy = p['tumour_er_biopsy'], tumour_er_percent_biopsy = p['tumour_er_percent_biopsy'],
                    tumour_pr_biopsy = p['tumour_pr_biopsy'], tumour_pr_percent_biopsy = p['tumour_pr_percent_biopsy'],
                    tumour_her2_biopsy = p['tumour_her2_biopsy'], tumour_her2_grade_biopsy = p['tumour_her2_grade_biopsy'],
                    tumour_ki67_biopsy = p['tumour_ki67_biopsy'],fnac = p['fnac'],fnac_location = p['fnac_location'],
                    fnac_diagnosis = p['fnac_diagnosis'])
        return biopsy_info

    def get_biopsies(self):
        """
        :returns list of models.BiopsyInfo
        """
        # try:
        biopsies = self.db.biopsies.find()
        return [self.to_biopsy_info(p) for p in biopsies]
        # except:
        #     self.log.get_logger().error("Error retrieving patients from database: %s", sys.exc_info())
        #     return
    def get_biopsy(self, folder_number):
         # try:
        biopsy_entry = self.db.biopsies.find_one({ self.key: folder_number })
        biopsy = self.to_biopsy_info(biopsy_entry)
        return biopsy
         # except:
         #    self.log.get_logger().error("Error retrieving patient %s from database: %s", folder_number, sys.exc_info())
         #    return


    def add_biopsy(self, biopsy):
        """
        adds a patient to the db
        :param models.Patient_bio_info_Info patient: the patient to insert
        """
        #try:
        biopsy_entry = self.from_biopsy_info(biopsy)
        self.db.biopsies.insert_one(biopsy_entry)
        return True, None
        # except:
        #     self.log.get_logger().error("Error adding event to database: %s", sys.exc_info())
        #     return False, sys.exc_info()


    def update_biopsy(self, biopsy):
        """
        :param models.PatientForm patient: model to update from
        """
        #try:
        self.db.biopsies.update_one({self.key: biopsy.folder_number },
                                        { "$set": self.from_biopsy_info(biopsy)})
        return True, None
        #except:
        #    self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
         #   return False, sys.exc_info()

    def delete_biopsy(self, folder_number):
        # try:
        self.db.biopsies.delete_one({self.key: folder_number})
        return True, None  # except:
        #     self.log.get_logger().error("Error deleting patient %s from database: %s", folder_number, sys.exc_info())
        #     return False, sys.exc_info()
    #################################
    # user add and password functions #
    #################################
    def add_user(self, name, email, username, password):
        try:
            user = self.db.users.find_one({"username": username})
            if user is not None:
                return False

            self.db.users.insert_one({"name": name, "email": email, "username": username, "password": password})
            return True
        except:
            self.log.get_logger().error("Error adding user: %s", sys.exc_info())
            return False

    def get_password(self, username):
        try:
            user = self.db.users.find_one({"username": username})
            if user is None:
                return None, None
            else:
                return user['password'], user['name']
        except:
            self.log.get_logger().error("Error retrieving user from database: %s", sys.exc_info())
            return None, None