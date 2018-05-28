from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FloatField, RadioField, FormField, \
    SubmitField, HiddenField, BooleanField, SelectMultipleField, FieldList
from datetime import datetime
from db_dict.common_dict import CommonDict

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

    @classmethod
    def append_fields(cls, fields):
        for field in fields:
            setattr(cls, field[0], SelectField(field[1][0], choices=field[1][1]))
            setattr(cls, field[0] + "_other", StringField("Other"))
        return cls

    @classmethod
    def append_select_fields(cls, fields):
        for field in fields:
            setattr(cls, field[0], SelectField(field[1][0], choices=field[1][1]))
            setattr(cls, field[0] + "_other", StringField("Other"))
        return cls


class SectionForm(BaseForm):
    def get_summary(self):
        return self.fld_form_status.data

    fld_pk = HiddenField()
    fld_folder_number = HiddenField()
    last_update = HiddenField()
    fld_form_status = SelectField("Form Status",  choices= CommonDict.form_status_choice)
    pass
