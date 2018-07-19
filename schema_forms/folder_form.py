from wtforms import StringField, TextAreaField, validators, SubmitField, HiddenField, SelectField
from db_dict.common_dict import CommonDict
from datetime import datetime
from schema_forms.form_utilities import BaseForm

class FoldersForm(BaseForm):
    fld_folder_number = StringField('Folder Number', [validators.required()])
    fld_folder_description = TextAreaField('Folder Description')
    fld_folder_pk = HiddenField()
    fld_doc_type = HiddenField()
    fld_is_delete = HiddenField()
    last_update = HiddenField()
    update_by = HiddenField()
    fld_form_status = SelectField("Form Status", choices=CommonDict.folder_status_choice)
    submit = SubmitField()

    def to_bson(self, update_by):
        bson = super().to_bson()
        bson['last_update'] = datetime.today()
        bson['update_by'] = update_by
        return bson

    def from_bson(self, p):
        super().from_bson(p)
        self.last_update.data = p.get_date('last_update')
        self.update_by.data = p['update_by']


