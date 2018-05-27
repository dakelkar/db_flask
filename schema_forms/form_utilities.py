from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FloatField, RadioField, FormField, \
    SubmitField, HiddenField, BooleanField, SelectMultipleField, FieldList
from datetime import datetime

def to_bson(form, prefix = 'fld_'):
    field_list = [a for a in dir(form) if a.startswith(prefix)]
    other_list = [x for x in dir(form) if x.endswith('other')]
    for other in other_list:
        if  form[other[:-len('_other')]].data != 'other':
            form[other].data = form[other[:-6]].data
    bson = {}
    for field in field_list:
        key = field[len(prefix):]
        value = form[field].data
        o = getattr(form, field)
        if o.type  == "DateField":
            value = datetime.combine(value, datetime.min.time())
        bson[key] = value
    return bson

def from_bson(form, p, prefix = "fld_"):
    if p is None:
        return None
    for key in p.keys():
        field_name = prefix + key
        if hasattr(form, field_name):
            form[field_name].data = p[key]

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