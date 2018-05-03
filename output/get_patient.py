import pymongo
import pandas as pd

def get_patients():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.patients
    patient_list = []

    for patient in db.patients.find():
        patient_list.append(patient)
    keys = []
    for key in patient_list[0]:
        keys.append(key)
    index = 0
    patients = pd.DataFrame(columns=keys)
    for patient in patient_list:
        data_list = []
        for key in keys:
            data = patient.get(key)
            data_list.append(data)
        patients.loc[index] = data_list
        index = index + 1