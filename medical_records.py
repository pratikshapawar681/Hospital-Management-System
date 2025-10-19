# medical_records.py
from db import medical_records_col
from bson import ObjectId
from datetime import datetime

def create_medical_record(patient_id, doctor_id, record_date, diagnosis, prescriptions=None, tests=None, notes=""):
    doc = {
        "patient_id": ObjectId(patient_id),
        "doctor_id": ObjectId(doctor_id) if doctor_id else None,
        "record_date": record_date,
        "diagnosis": diagnosis,
        "prescriptions": prescriptions or [],
        "tests": tests or [],
        "notes": notes,
        "created_at": datetime.utcnow()
    }
    return medical_records_col.insert_one(doc).inserted_id

def list_medical_records():
    return list(medical_records_col.find())

def delete_medical_record(record_id):
    return medical_records_col.delete_one({"_id": ObjectId(record_id)}).deleted_count
