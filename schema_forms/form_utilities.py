def to_bson(form, prefix = 'fld_'):
    field_list = [a for a in dir(form) if a.startswith(prefix)]
    bson = {}
    for field in field_list:
        key = field[len(prefix):]
        bson[key] = form[field].data
    return bson

def from_bson(form, p, prefix = "fld_"):
    for key in p.keys():
        field_name = prefix + key
        if hasattr(form, field_name):
            print(field_name)
            form[field_name].data = p[key]