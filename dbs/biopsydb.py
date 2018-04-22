import sys
import pymongo
from schema_forms import models
from datetime import datetime


class BiopsyDb(object):
    # This class wraps the DB access for patients
    key = "folder_number"

    def __init__(self, logger):
        # Setup logging
        self.log = logger
        self.db = None

    def connect(self):
        # Connect to database
        try:
            client = pymongo.MongoClient("localhost", 27017)
            self.db = client.patients.biopsies
            self.log.get_logger().info("Connection to Biopsy database opened.")
        except:
            self.log.get_logger().error("Error connecting to database biopsies: %s", sys.exc_info())

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
        biopsies = self.db.find()
        return [self.to_biopsy_info(p) for p in biopsies]
        # except:
        #     self.log.get_logger().error("Error retrieving patients from database: %s", sys.exc_info())
        #     return
    def get_biopsy(self, folder_number):
         # try:
        biopsy_entry = self.db.find_one({ self.key: folder_number })
        if biopsy_entry is None:
            return None
            
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
        try:
            biopsy_entry = self.from_biopsy_info(biopsy)
            self.db.insert_one(biopsy_entry)
            return True, None
        except:
             self.log.get_logger().error("Error adding event to database: %s", sys.exc_info())
             return False, sys.exc_info()


    def update_biopsy(self, biopsy):
        """
        :param models.PatientForm patient: model to update from
        """
        #try:
        self.db.update_one({self.key: biopsy.folder_number },
                                        { "$set": self.from_biopsy_info(biopsy)})
        return True, None
        #except:
        #    self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
         #   return False, sys.exc_info()

    def delete_biopsy(self, folder_number):
        # try:
        self.db.delete_one({self.key: folder_number})
        return True, None  # except:
        #     self.log.get_logger().error("Error deleting patient %s from database: %s", folder_number, sys.exc_info())
        #     return False, sys.exc_info()
