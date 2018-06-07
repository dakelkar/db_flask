class FolderSection:
    def __init__(self, id, name, action, status, forms, folder_pk, last_modified_by, last_modified_on, pks, is_list):
        self.id = id
        self.name = name
        self.action = action
        self.status = status
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.forms = forms
        self.count = len(forms)
        self.folder_pk = folder_pk
        if pks is None:
            pks = []
        self.pks = pks
        self.is_list = is_list