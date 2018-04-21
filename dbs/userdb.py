import sys
import pymongo

class UserDb(object):
#wraps db access for users

    def __init__(self, logger):
        # Setup logging
        self.log = logger
        self.db = None


    def connect(self):
        # Connect to database
        try:
            client = pymongo.MongoClient("localhost", 27017)
            self.db = client.patients.users
            self.log.get_logger().info("Connection to patients database opened.")
        except:
            self.log.get_logger().error("Error connecting to database patients: %s", sys.exc_info())



    # user add and password functions #
    #################################
    def add_user(self, name, email, username, password):
        try:
            user = self.db.find_one({"username": username})
            if user is not None:
                return False

            self.db.insert_one({"name": name, "email": email, "username": username, "password": password})
            return True
        except:
            self.log.get_logger().error("Error adding user: %s", sys.exc_info())
            return False


    def get_password(self, username):
        try:
            user = self.db.find_one({'username': username})
            print(username, user)
            if user is None:
                return None, None
            else:
                return user['password'], user['name']
        except:
            self.log.get_logger().error("Error retrieving user from database: %s", sys.exc_info())
            return None, None
