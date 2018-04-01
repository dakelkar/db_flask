import sys
import pymongo
from datetime import date


class PatientsDb(object):
    # This class wraps the DB access for patients

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
        try:
            patients = self.db.patients.find()
            return patients
        except:
            self.log.get_logger().error("Error retrieving patients from database: %s", sys.exc_info())
            return

    def get_patient(self, folder_number):
        try:
            patient = self.db.patients.find_one({ "File_number": folder_number })
            return patient
        except:
            self.log.get_logger().error("Error retrieving patient %s from database: %s", folder_number, sys.exc_info())
            return

    def add_patient(self, folder_number, mr_number, name, aadhaar_card, date_first, permanent_address, current_address,
                    phone, email_id, gender, age_yrs, date_of_birth, place_birth, height_cm, weight_kg):
        try:
            self.db.patients.insert_one({"File_number": folder_number,
                                        "MR_number": mr_number,
                                        "Name": name,
                                        "Aadhaar_Card": aadhaar_card,
                                        "FirstVisit_Date": str(date_first),
                                        "Permanent_Address": permanent_address,
                                        "Current_Address": current_address,
                                        "Phone": phone,
                                        "Email_ID":email_id,
                                        "Gender":gender,
                                        "Age_yrs":age_yrs,
                                        "Date_of_Birth":str(date_of_birth),
                                        "Place_Birth":place_birth,
                                        "Height_cm":height_cm,
                                        "Weight_kg": weight_kg,
                                        "BMI": (str(round(weight_kg / (height_cm * height_cm))))})
            return True, None
        except:
            self.log.get_logger().error("Error adding event to database: %s", sys.exc_info())
            return False, sys.exc_info()

    def update_patient(self, folder_number, mr_number, name, aadhaar_card, date_first, permanent_address,
                       current_address, phone, email_id, gender, age_yrs, date_of_birth, place_birth, height_cm,
                       weight_kg):
        try:
            self.db.patients.update_one({"File_number": folder_number }, { "$set": {
                                       "MR_number": mr_number,
                                       "Name": name,
                                       "Aadhaar_Card": aadhaar_card,
                                       "FirstVisit_Date": date_first,
                                       "Permanent_Address": permanent_address,
                                       "Current_Address": current_address,
                                        "Phone": phone,
                                        "Email_ID":email_id,
                                        "Gender":gender,
                                        "Age_yrs":age_yrs,
                                        "Date_of_Birth":date_of_birth,
                                        "Place_Birth":place_birth,
                                        "Height_cm":height_cm,
                                        "Weight_kg": weight_kg,
                                        "BMI": (str(round(weight_kg / (height_cm * height_cm))))}})
            return True, None
        except:
            self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
            return False, sys.exc_info()

    def delete_patient(self, folder_number):
        try:
            self.db.patients.delete_one({"folder_number": folder_number})
            return True, None
        except:
            self.log.get_logger().error("Error deleting patient %s from database: %s", folder_number, sys.exc_info())
            return False, sys.exc_info()

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
