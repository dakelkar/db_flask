import sys
import pymongo
import uuid
from schema_forms.form_utilities import BsonWrapper

class SectionDb(object):
    # This class wraps the DB access for patients
    key = "pk"

    def __init__(self, logger, form_class, collection_name):
        # Setup logging
        self.log = logger
        self.db = None
        self.form_class = form_class
        self.db_name = 'bcdb'
        self.collection_name = 'folders'
        self.doc_type = collection_name

    def get_from_request(self, request_data):
        form = self.form_class(request_data)
        return form

    def connect(self, url):
        # Connect to database
        try:
            client = pymongo.MongoClient(url)
            self.db = client.get_database(self.db_name).get_collection(self.collection_name)
            self.log.get_logger().info("Connection to %s.%s for %s opened." % (self.db_name, self.collection_name, self.form_class))
        except:
            self.log.get_logger().error("Error connecting to database %s: %s" % (self.form_class, sys.exc_info()))

    def get_folder_items(self, folder_pk):
        db_entries = self.db.find({'$and':[{"folder_pk": folder_pk}, {'is_delete':False}, {'doc_type' : self.doc_type}]})
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

    def add_item(self, form, update_by):
        form.fld_doc_type.data = self.doc_type
        form.fld_is_delete.data = False
        db_entry = form.to_bson(update_by)
        db_entry[self.key] = uuid.uuid4().hex
        self.db.insert_one(db_entry)
        return True, db_entry[self.key]

    def update_item(self, form, update_by):
        db_entry = form.to_bson(update_by)
        self.db.update_one({self.key: form.fld_pk.data}, {"$set": db_entry})
        return True, form.fld_pk.data

    def delete_item(self, pk, update_by):
        status = 'Item not found'
        form = self.get_item(pk)
        if form is not None:
            status = form.fld_pk.data
            form.fld_is_delete.data = True
            #TODO set only is_delete as True rest form remain same
            self.update_item(form, update_by)
        return True, status
