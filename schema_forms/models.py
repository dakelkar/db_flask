from create_url import encodex
class Patient_bio_info_Info:
    def __init__(self, folder_number, mr_number, name, aadhaar_card, date_first, permanent_address, current_address,
                 phone, email_id, gender, age_yrs, date_of_birth, place_birth, height_cm, weight_kg):
        self.folder_number=folder_number
        self.mr_number=mr_number
        self.name=name
        self.aadhaar_card=aadhaar_card
        self.date_first=date_first
        self.permanent_address=permanent_address
        self.current_address=current_address
        self.phone=phone
        self.email_id=email_id
        self.gender=gender
        self.age_yrs=age_yrs
        self.date_of_birth=date_of_birth
        self.place_birth=place_birth
        self.height_cm=height_cm
        self.weight_kg=weight_kg
        self.folder_hash = encodex(folder_number)
