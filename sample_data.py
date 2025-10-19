# sample_data.py
from departments import create_department
from doctors import create_doctor
from patients import create_patient
from appointments import schedule_appointment
from datetime import datetime, timedelta

def insert_sample_data():
    cardio_id = create_department("Cardiology", "Heart department")
    ent_id = create_department("ENT", "Ear Nose Throat")
    
    doc1 = create_doctor("Dr. Alice", "Cardiologist", cardio_id)
    doc2 = create_doctor("Dr. Bob", "ENT Specialist", ent_id)
    
    pat1 = create_patient("John Doe", datetime(1990,5,4), "M", phone="9999999999")
    pat2 = create_patient("Jane Smith", datetime(1985,8,12), "F", phone="8888888888")
    
    schedule_appointment(pat1, doc1, cardio_id, datetime.utcnow() + timedelta(days=1))
    schedule_appointment(pat2, doc2, ent_id, datetime.utcnow() + timedelta(days=2))
    
    print("Sample data inserted successfully.")
