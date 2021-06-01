
def surg_complications(var):
    if var == "post_surgery_comp":
        var_list = ["Seroma",
                    "Soakage",
                    "Flap Necrosis",
                    "Hematoma",
                    "Surgical Site Infection",
                    "Delayed Wound Healing",
                    'Implant Loss',
                    "Lymphoedema"]
    elif var == "recurrence_sites":
        var_list = ["Loco-regional",
                    "Breast",
                    "Axilla",
                    "Distant"]
    elif var == "surgical_treatment":
        var_list = ["Non surgical treatment",
                    'Implant extrusion/removal',
                    'Re-suturing',
                    'Debridement',
                    'Nipple-areola excision',
                    'Wait and Watch approach',
                    'Take back to theatre']
    else:
        var_list = "No such variable"
    return var_list

def pedicle(ped_type):
    if ped_type == "secondary":
        pedicle = ['Inferior Pedicle',
                    'Inferior Lateral Pedicle',
                    'Inferior Lateral+Medial Pedicle',
                    'Superior Pedicle',
                    'Superio-Medial Pedicle',
                    'Inferior Medial Pedicle',
                    'Other']
    elif ped_type == "primary":
        pedicle = ["Lower Pedicle",
                   "Superior Pedicle",
                   "Superio-medial Pedicle",
                   "Lateral Pedicle",
                   "Inferior Pedicle",
                   "Inferior Medial Pedicle",
                   "Inferior Medial and Lateral Pedicle",
                   "Other"]
    else:
        pedicle = "Other"
    return pedicle


def incision(var):
    if var == "conservative_incision":
        var_list = ["Circum-areolar",
                    "Radial",
                    "Inframammary (IMF)",
                    "Lateral Crease",
                    'Axillary',
                    'Wise Pattern',
                    'Vertical Scar']
    elif var == "reconstruction_incision":
        var_list = ["Inframmamary Fold Incision",
                    'Lateral Fold',
                    'Wise Pattern',
                    'Radial',
                    'Transverse Oblique',
                    'Oblique with Supra-areolar',
                    'Oblique',
                    'Other']
    else:
        var_list = "Not found"
    return var_list