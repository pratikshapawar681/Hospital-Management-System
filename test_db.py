from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["hospital_db"]

# Insert one test department
db.departments.insert_one({"name": "Cardiology", "description": "Heart Dept"})

# Print databases and collections
print("Databases:", client.list_database_names())
print("Collections:", db.list_collection_names())

# Print inserted document
print("Departments:", list(db.departments.find()))

