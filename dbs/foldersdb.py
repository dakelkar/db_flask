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

    def connect(self, url):
        client = pymongo.MongoClient(url)

        self.db = client.bcdb.folders
        self.log.get_logger().info("Connection to folders database opened.")

    def get_folders(self):
        folders = self.db.find({'$and':[{ 'doc_type': 'folder'}, { 'is_delete': False }]})
        return folders

    def folder_check(self, folder_pk):
        # to check if folder has been marked deleted or missing
        folder_form = self.get_item(folder_pk)
        if folder_form is None:
            return None
        is_delete = folder_form.fld_is_delete.data
        folder_number = None
        if not is_delete:
            folder_number = folder_form.fld_folder_number.data
        return folder_number

    def get_item(self, folder_pk):
        folder_entry = self.db.find_one({ self.key: folder_pk })
        if folder_entry is None:
            return None
        folder = self.FoldersForm()
        folder.from_bson(BsonWrapper(folder_entry))
        return folder

    def get_folder_by_number(self, folder_number, is_delete):
        folder_entry = self.db.find_one({'$and':[{ 'folder_number': folder_number }, { 'is_delete': is_delete }]})
        if folder_entry is None:
            return None
        folder = self.FoldersForm()
        folder.from_bson(BsonWrapper(folder_entry))
        return folder

    def add_item(self, form, username):
        folder_number = form.fld_folder_number.data
        folder = self.get_folder_by_number(folder_number, is_delete=False)
        if folder is not None:
            return False, "Folder number already exists"
        form.fld_folder_pk.data = uuid.uuid4().hex
        form.fld_doc_type.data = 'folder'
        form.fld_is_delete.data = False
        folder_entry = form.to_bson(username)
        self.db.insert_one(folder_entry)
        return True, form.fld_folder_number.data

    def update_item(self, form, username):
        folder_pk = form.fld_folder_pk.data
        db_entry = form.to_bson(username)
        self.db.update_one({self.key: folder_pk}, {"$set": db_entry})
        return True, form.fld_folder_pk.data

    def delete_item(self, folder_pk, username):
        status = 'Folder not found'
        form = self.get_item(folder_pk)
        if form is not None:
            status = form.fld_folder_number.data
            form.fld_is_delete.data = True
            self.update_item(form, username)
        return True, status


