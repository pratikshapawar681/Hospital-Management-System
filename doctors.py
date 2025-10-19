# doctors.py
from db import doctors_col
from bson import ObjectId
from datetime import datetime

def create_doctor(name, specialization, department_id=None, phone=None, email=None):
    doc = {
        "name": name,
        "specialization": specialization,
        "department_id": ObjectId(department_id) if department_id else None,
        "phone": phone,
        "email": email,
        "created_at": datetime.utcnow()
    }
    return doctors_col.insert_one(doc).inserted_id

def list_doctors():
    return list(doctors_col.find())

def update_doctor(doctor_id, updates):
    if "department_id" in updates:
        updates["department_id"] = ObjectId(updates["department_id"])
    return doctors_col.update_one({"_id": ObjectId(doctor_id)}, {"$set": updates}).modified_count

def delete_doctor(doctor_id):
    return doctors_col.delete_one({"_id": ObjectId(doctor_id)}).deleted_count
