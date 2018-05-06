def to_bson(form, prefix = 'fld_'):
    field_list = [a for a in dir(form) if a.startswith(prefix)]
    other_list = [x for x in dir(form) if x.endswith('other')]
    for other in other_list:
        if  form[other[:-len('_other')]].data != 'other':
            form[other].data = form[other[:-len('_other')]].data
    bson = {}
    for field in field_list:
        key = field[len(prefix):]
        bson[key] = form[field].data
    return bson

def from_bson(form, p, prefix = "fld_"):
    for key in p.keys():
        field_name = prefix + key
        if hasattr(form, field_name):
            form[field_name].data = p[key]