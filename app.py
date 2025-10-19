from departments import create_department, list_departments
from doctors import create_doctor, list_doctors
from patients import create_patient, list_patients
from appointments import schedule_appointment, list_appointments
from medical_records import create_medical_record, list_medical_records
from sample_data import insert_sample_data
from datetime import datetime

def main_menu():
    while True:
        print("\n--- HOSPITAL MANAGEMENT SYSTEM ---")
        print("1) Departments")
        print("2) Doctors")
        print("3) Patients")
        print("4) Appointments")
        print("5) Medical Records")
        print("6) Insert Sample Data")
        print("0) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("Departments menu: 1) Create 2) List")
            c = input("Choice: ")
            if c == "1":
                name = input("Name: ")
                desc = input("Description: ")
                print("Created id:", create_department(name, desc))
            elif c == "2":
                deps = list_departments()
                for d in deps:
                    print(d)

        elif choice == "6":
            insert_sample_data()
            print("Sample data inserted successfully.")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()

