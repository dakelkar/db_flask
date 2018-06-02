import sys
import pymongo
from schema_forms.form_utilities import BsonWrapper
import uuid

class FoldersDb(object):
    # This class wraps the DB access for folders
    key = "folder_pk"

    def __init__(self, logger, FoldersForm):
        # Setup logging
        self.log = logger
        self.FoldersForm = FoldersForm
        self.db = None

    def get_from_request(self, request_data):
        form = self.FoldersForm(request_data)
        return form

    def connect(self):
        client = pymongo.MongoClient("localhost", 27017)
        self.db = client.folders
        self.log.get_logger().info("Connection to folders database opened.")

    def get_folders(self):
        folders = self.db.folders.find()
        return folders

    def get_item(self, folder_pk):
        folder_entry = self.db.folders.find_one({ self.key: folder_pk })
        if folder_entry is None:
            return None
        folder = self.FoldersForm()
        folder.from_bson(BsonWrapper(folder_entry))
        return folder

    def get_folder_by_number(self, folder_number):
        folder_entry = self.db.folders.find_one({ 'folder_number': folder_number })
        if folder_entry is None:
            return None
        folder = self.FoldersForm()
        folder.from_bson(BsonWrapper(folder_entry))
        return folder

    def add_item(self, form, username):
        folder_number = form.fld_folder_number.data
        folder = self.get_folder_by_number(folder_number)
        if folder is not None:
            return False, "Folder number already exists"
        doc_type = 'folder'
        is_delete = False
        folder_pk = uuid.uuid4().hex
        form.fld_folder_pk.data = folder_pk
        form.doc_type.data = doc_type
        form.is_delete.data = is_delete
        folder_entry = form.to_bson(username)
        self.db.folders.insert_one(folder_entry)
        return True, form.fld_folder_number.data

    #def update_item(self, form, update_by):
    #    try:
    #        self.db.folders.update_one({self.key: FoldersForm.folder_number },
    #                                    { "$set": self.FoldersForm(folder_number)})
    #        return True, None
    #    except:
    #        self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
    #        return False, sys.exc_info()

    def update_item(self, form, update_by):
        db_entry = form.to_bson(update_by)
        self.db.update_one({self.key: form.fld_pk.data}, {"$set": db_entry})
        return True, form.fld_pk.data




    def delete_item(self, folder_number):
        self.db.folder.delete_one({self.key: folder_number})
        return True, None

