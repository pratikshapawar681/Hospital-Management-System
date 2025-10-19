# db.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "hospital_db")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
departments_col = db['departments']
doctors_col = db['doctors']
patients_col = db['patients']
appointments_col = db['appointments']
medical_records_col = db['medical_records']

