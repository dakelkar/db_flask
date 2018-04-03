import sys
import pymongo
import models
from datetime import datetime


class PatientsDb(object):
    # This class wraps the DB access for patients
    key = "folder_number"
    
    def from_patient_info(self, patient):
        return {
            self.key: patient.folder_number,
            "MR_number": patient.mr_number,
            "Name": patient.name,
            "Aadhaar_Card": patient.aadhaar_card,
            "FirstVisit_Date": datetime.combine(patient.date_first, datetime.min.time()),
            "Permanent_Address": patient.permanent_address,
            "Current_Address": patient.current_address,
            "Phone": patient.phone,
            "Email_ID": patient.email_id,
            "Gender": patient.gender,
            "Age_yrs": patient.age_yrs,
            "Date_of_Birth": datetime.combine(patient.date_of_birth, datetime.min.time()),
            "Place_Birth":  patient.place_birth,
            "Height_cm": patient.height_cm,
            "Weight_kg": patient.weight_kg,
            "BMI": (str(round(patient.weight_kg / (patient.height_cm * patient.height_cm))))}

    def to_patient_info(self, p):
        patient_info = models.PatientInfo(folder_number=p[self.key], mr_number=p['MR_number'], name=p['Name'],
                                          aadhaar_card=p['Aadhaar_Card'], date_first=p['FirstVisit_Date'].date(),
                                          permanent_address=p['Permanent_Address'],
                                          current_address=p['Current_Address'], phone=p['Phone'],
                                          email_id=p['Email_ID'], gender=p['Gender'], age_yrs=p['Age_yrs'],
                                          date_of_birth=p['Date_of_Birth'].date(), place_birth=p['Place_Birth'],
                                          height_cm=p['Height_cm'], weight_kg=p['Weight_kg'])
        return patient_info

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
        :returns list of models.PatientInfo
        """
        # try:
        patients = self.db.patients.find()
        return [self.to_patient_info(p) for p in patients]
        # except:
        #     self.log.get_logger().error("Error retrieving patients from database: %s", sys.exc_info())
        #     return

    def get_patient(self, folder_number):
         # try:
        patient_entry = self.db.patients.find_one({ self.key: folder_number })
        patient = self.to_patient_info(patient_entry)
        return patient
         # except:
         #    self.log.get_logger().error("Error retrieving patient %s from database: %s", folder_number, sys.exc_info())
         #    return

    def add_patient(self, patient):
        """
        adds a patient to the db
        :param models.PatientInfo patient: the patient to insert
        """
        #try:
        patient_entry = self.from_patient_info(patient)
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
                                        { "$set": self.from_patient_info(patient)})
            return True, None
        except:
            self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
            return False, sys.exc_info()

    def delete_patient(self, folder_number):
        try:
            self.db.patients.delete_one({self.key: folder_number})
            return True, None
        except:
            self.log.get_logger().error("Error deleting patient %s from database: %s", folder_number, sys.exc_info())
            return False, sys.exc_info()

    #################################
    # TODO: move users into their own db file
    # TODO: move users into their own db file
    # TODO: move users into their own db file
    # TODO: move users into their own db file

    def get_password(self, username):
        try:
            user = self.db.users.find_one({ "username": username })
            if user is None:
                return None, None
            else:
                return user['password'], user['name']
        except:
            self.log.get_logger().error("Error retrieving user from database: %s", sys.exc_info())
            return None, None

    def add_user(self, name, email, username, password):
        try:
            user = self.db.users.find_one({"username": username})
            if user is not None:
                return False

            self.db.users.insert_one({"name": name, "email": email, "username": username, "password": password })
            return True
        except:
            self.log.get_logger().error("Error adding user: %s", sys.exc_info())
            return False
