import sys
import pymongo

class UserDb(object):
#wraps db access for users

    def __init__(self, logger):
        # Setup logging
        self.log = logger
        self.db = None
        self.doc_type = 'users'


    def connect(self, url):
        # Connect to database
        try:
            client = pymongo.MongoClient(url)
            self.db = client.bcdb.folders
            self.log.get_logger().info("Connection to patients database opened.")
        except:
            self.log.get_logger().error("Error connecting to database patients: %s", sys.exc_info())



    # user add and password functions #
    #################################
    def add_user(self, name, email, username, password):
        try:
            user = self.db.find_one({'$and':[{"username": username}, {'doc_type': self.doc_type}]})
            if user is not None:
                return False

            self.db.insert_one({"name": name, "email": email, "username": username, "password": password,
                                'doc_type': self.doc_type})
            return True
        except:
            self.log.get_logger().error("Error adding user: %s", sys.exc_info())
            return False


    def get_password(self, username):
        try:
            user = self.db.find_one({'$and':[{"username": username}, {'doc_type': self.doc_type}]})
            if user is None:
                return None, None
            else:
                return user['password'], user['name']
        except:
            self.log.get_logger().error("Error retrieving user from database: %s", sys.exc_info())
            return None, None

