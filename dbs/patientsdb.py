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
            "age_diagnosis":patient.age_diagnosis,
            "date_of_birth": datetime.combine(patient.date_of_birth, datetime.min.time()),
            "place_birth":  patient.place_birth,
            "height_cm": patient.height_cm,
            "weight_kg": patient.weight_kg,
            "form_status":patient.form_status,
            "last_update":datetime.combine(patient.last_update, datetime.min.time())
        }

    def to_patient_bio_info_info(self, p):
        patient_bio_info_info = models.Patient_bio_info_Info(folder_number=p[self.key], mr_number=p['mr_number'],
                                          name=p['name'], aadhaar_card=p['aadhaar_card'], date_first=p['date_first'].date(),
                                          permanent_address=p['permanent_address'],
                                          current_address=p['current_address'], phone=p['phone'],
                                          email_id=p['email_id'], gender=p['gender'], age_yrs=p['age_yrs'],
                                          age_diagnosis=p['age_diagnosis'],date_of_birth=p['date_of_birth'].date(),
                                          place_birth=p['place_birth'], height_cm=p['height_cm'],
                                          weight_kg=p['weight_kg'], form_status=p['form_status'],
                                          last_update=p['last_update'].date())
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

    