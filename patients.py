# patients.py
from db import patients_col
from bson import ObjectId
from datetime import datetime

def create_patient(name, dob, gender, phone=None, address=None, primary_doctor_id=None):
    doc = {
        "name": name,
        "dob": dob,
        "gender": gender,
        "phone": phone,
        "address": address,
        "primary_doctor_id": ObjectId(primary_doctor_id) if primary_doctor_id else None,
        "allergies": [],
        "created_at": datetime.utcnow()
    }
    return patients_col.insert_one(doc).inserted_id

def list_patients():
    return list(patients_col.find())

def update_patient(patient_id, updates):
    if "primary_doctor_id" in updates and updates["primary_doctor_id"]:
        updates["primary_doctor_id"] = ObjectId(updates["primary_doctor_id"])
    return patients_col.update_one({"_id": ObjectId(patient_id)}, {"$set": updates}).modified_count

def delete_patient(patient_id):
    return patients_col.delete_one({"_id": ObjectId(patient_id)}).deleted_count
