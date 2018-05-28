import sys
import pymongo
import uuid

class BsonWrapper:
    def __init__(self, bson):
        self._bson = bson
        
    def keys(self):
        return self._bson.keys()

    def get_date(self, key):
        value = self[key]
        if value is not None:
            return value.date()        
        return None
        
    def __getitem__(self, key):
        if key in self._bson.keys():
            return self._bson[key]
        return None

class SectionDb(object):
    # This class wraps the DB access for patients
    key = "pk"

    def __init__(self, logger, form_class, collection_name):
        # Setup logging
        self.log = logger
        self.db = None
        self.form_class = form_class
        self.db_name = 'patients'
        self.collection_name = collection_name

    def get_from_request(self, request_data):
        form = self.form_class(request_data)
        return form

    def connect(self):
        # Connect to database
        try:
            client = pymongo.MongoClient("localhost", 27017)
            self.db = client.get_database(self.db_name).get_collection(self.collection_name)
            self.log.get_logger().info("Connection to %s.%s for %s opened." % (self.db_name, self.collection_name, self.form_class))
        except:
            self.log.get_logger().error("Error connecting to database %s: %s" % (self.form_class, sys.exc_info()))

    def get_folder_items(self, folder_number):
        db_entries = self.db.find({"folder_number": folder_number})
        if db_entries is None:
            return None

        forms = []        
        for db_entry in db_entries:
            form = self.form_class()
            form.from_bson(BsonWrapper(db_entry))
            forms.append(form)

        return forms

    def get_item(self, pk):
        db_entry = self.db.find_one({self.key: pk})
        if db_entry is None:
            return None
        
        form = self.form_class()
        form.from_bson(BsonWrapper(db_entry))
        return form

    def add_item(self, form):
        db_entry = form.to_bson()
        db_entry[self.key] = uuid.uuid4().hex
        self.db.insert_one(db_entry)
        return True, db_entry[self.key]

    def update_item(self, form):
        self.db.update_one({self.key: form.fld_pk.data}, {"$set": form.to_bson()})
        return True, form.fld_pk.data

    def delete_item(self, pk):
        # try:
        self.db.delete_one({self.key: pk})
        return True, None
