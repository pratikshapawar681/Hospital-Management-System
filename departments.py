# departments.py
from db import departments_col
from datetime import datetime
from bson import ObjectId

def create_department(name, description=""):
    doc = {"name": name, "description": description, "created_at": datetime.utcnow()}
    return departments_col.insert_one(doc).inserted_id

def list_departments():
    return list(departments_col.find())

def update_department(dept_id, updates):
    return departments_col.update_one({"_id": ObjectId(dept_id)}, {"$set": updates}).modified_count

def delete_department(dept_id):
    return departments_col.delete_one({"_id": ObjectId(dept_id)}).deleted_count
