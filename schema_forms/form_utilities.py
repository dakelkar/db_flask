from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SelectField,HiddenField
from datetime import datetime
from db_dict.common_dict import CommonDict


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


def to_bson(form, prefix = 'fld_'):
    
    # handle 'other' fields (_other suffix)
    other_list = [x for x in dir(form) if x.endswith('other')]
    for other in other_list:
        if  form[other[:-len('_other')]].data != 'other':
            form[other].data = form[other[:-6]].data
    
    # handle normal fields (prefix fld_)
    field_list = [a for a in dir(form) if a.startswith(prefix)]
    bson = {}
    for field in field_list:
        key = field[len(prefix):]
        value = form[field].data
        o = getattr(form, field)
        # setting is_delete to boolean everytime form is submitted
        if key == 'is_delete':
            result = False
            if value == 'True' or value == True:
                result = True
            value = result
        # handle dates!
        if o.type  == "DateField":
            value = datetime.combine(value, datetime.min.time())
        bson[key] = value

    # handle form fields (suffix _form)
    form_fields = [x for x in dir(form) if x.endswith('_form')]
    for field in form_fields:
        key = field[:-len('_form')]
        bson[key] = form[field].to_bson()

    return bson

def from_bson(form, p, prefix = "fld_"):
    if p is None:
        return None

    # handle normal fields (prefix fld_)
    field_list = [a for a in dir(form) if a.startswith(prefix)]
    for field in field_list:
        key = field[len(prefix):]
        if key in p.keys():
            form[field].data = p[key]

    # handle form fields (suffix _form)
    form_fields = [x for x in dir(form) if x.endswith('_form')]
    for field in form_fields:
        key = field[:-len('_form')]
        if key in p.keys():
            form[field].from_bson(p[key])


class BaseForm(FlaskForm):
    class Meta:
        csrf = False

    def to_bson(self):
        bson = to_bson(self)
        return bson

    def from_bson(self, p):
        from_bson(self, p)

    @property
    def title(self):
        return type(self).__name__

    @classmethod
    def append_select_fields(cls, fields):
        for field in fields:
            setattr(cls, field[0], SelectField(field[1][0], choices=field[1][1]))
            setattr(cls, field[0] + "_other", StringField("Other"))
        return cls


class SectionForm(BaseForm):
    def get_summary(self):
        return self.fld_form_status.data
    
    def from_bson(self, p):
        super().from_bson(p)
        self.last_update.data = p.get_date('last_update')
        self.update_by.data = p['update_by']

    fld_pk = HiddenField()
    fld_doc_type = HiddenField()
    fld_is_delete = HiddenField()
    fld_folder_pk = HiddenField()
    last_update = HiddenField()
    update_by = HiddenField()
    fld_form_status = SelectField("Form Status", choices=CommonDict.form_status_choice)
    fld_comments= TextAreaField("Any additional comments for data in this form?")

    def to_bson(self, update_by):
        bson = super().to_bson()
        bson['last_update'] = datetime.today()
        bson['update_by'] = update_by
        return bson
