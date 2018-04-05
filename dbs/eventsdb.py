import sys
import pymongo
from datetime import datetime


class EventsDb(object):
    # This class wraps the DB access for events

    def __init__(self, logger):
        # Setup logging
        self.log = logger
        self.db = None

    def connect(self):
        # Connect to database
        try:
            client = pymongo.MongoClient("localhost", 27017)
            self.db = client.events
            self.log.get_logger().info("Connection to events database opened.")
        except:
            self.log.get_logger().error("Error connecting to database events: %s", sys.exc_info())

    def get_events(self):
        try:
            events = self.db.events.find()
            return events
        except:
            self.log.get_logger().error("Error retrieving events from database: %s", sys.exc_info())
            return

    def get_event(self, name):
        try:
            event = self.db.events.find_one({ "name": name })
            return event
        except:
            self.log.get_logger().error("Error retrieving event %s from database: %s", name, sys.exc_info())
            return

    def add_event(self, name, description, event_type, date, time, duration, recurring):
        try:
            self.db.events.insert_one({"name": name,
                                       "description": description,
                                       "type": event_type,
                                       "date": datetime.combine(date, time),
                                       "duration": duration,
                                       "recurring": recurring})
            return True, None
        except:
            self.log.get_logger().error("Error adding event to database: %s", sys.exc_info())
            return False, sys.exc_info()

    def update_event(self, name, description, event_type, date, time, duration, recurring):
        try:
            self.db.events.update_one({"name": name }, { "$set": {
                                       "description": description,
                                       "type": event_type,
                                       "date": datetime.combine(date, time),
                                       "duration": duration,
                                       "recurring": recurring}})
            return True, None
        except:
            self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
            return False, sys.exc_info()

    def delete_event(self, name):
        try:
            self.db.events.delete_one({"name": name})
            return True, None
        except:
            self.log.get_logger().error("Error deleting event %s from database: %s", name, sys.exc_info())
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
