def to_bson(form, prefix, prefix_keep):
    #fld_prefix = "fld_"
    field_list = [a for a in dir(form) if a.startswith(prefix)]
    bson = {}
    for field in field_list:
        if not prefix_keep:
            key = field[len(prefix):]
            bson[key] = form[field].data
        else:
            key = field
            bson[key] = form[field].data
    return bson

def from_bson(form, p, prefix = "fld_", prefix_kept = True):
    for key in p.keys():
        if prefix_kept:
            field_name = key
        else:
            field_name = prefix + key
        if hasattr(form, field_name):
            print(field_name)
            form[field_name].data = p[key]