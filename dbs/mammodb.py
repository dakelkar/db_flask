import sys
import pymongo
from schema_forms.mammo_form import RadiologyForm

class MammoDb(object):
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
            self.db = client.patients.mammographies
            self.log.get_logger().info("Connection to mammographies database opened.")
        except:
            self.log.get_logger().error("Error connecting to database mammographies: %s", sys.exc_info())

    def get_mammography(self, folder_number):
        # try:
        mammography_entry = self.db.find_one({self.key: folder_number})
        if mammography_entry is None:
            return None
        
        mammography = RadiologyForm()
        mammography.from_bson(mammography_entry)
        return mammography
        # except:  #    self.log.get_logger().error("Error retrieving patient %s from database: %s", folder_number, sys.exc_info())  #    return

    def add_mammography(self, mammography):
        mammography_entry = mammography.to_bson()
        print(mammography_entry)
        self.db.insert_one(mammography_entry)
        return True, None

    def update_mammography(self, mammography):
        """
        :param models.MammographyInfo mammography: model to update from
        """
        # try:
        self.db.update_one({self.key: mammography.fld_folder_number.data}, {"$set": mammography.to_bson()})
        return True, None
        # except:
        #    self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
        #   return False, sys.exc_info()

    def delete_mammography(self, folder_number):
        # try:
        self.db.delete_one({self.key: folder_number})
        return True, None
        # except:
        #     self.log.get_logger().error("Error deleting patient %s from database: %s", folder_number, sys.exc_info())
        #     return False, sys.exc_info()

    #################################