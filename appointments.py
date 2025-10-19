# appointments.py
from db import appointments_col
from bson import ObjectId
from datetime import datetime

def schedule_appointment(patient_id, doctor_id, department_id, appt_datetime, notes=""):
    doc = {
        "patient_id": ObjectId(patient_id),
        "doctor_id": ObjectId(doctor_id),
        "department_id": ObjectId(department_id),
        "appointment_datetime": appt_datetime,
        "notes": notes,
        "status": "scheduled",
        "created_at": datetime.utcnow()
    }
    return appointments_col.insert_one(doc).inserted_id

def list_appointments():
    return list(appointments_col.find())

def update_appointment(appointment_id, updates):
    return appointments_col.update_one({"_id": ObjectId(appointment_id)}, {"$set": updates}).modified_count

def delete_appointment(appointment_id):
    return appointments_col.delete_one({"_id": ObjectId(appointment_id)}).deleted_count
