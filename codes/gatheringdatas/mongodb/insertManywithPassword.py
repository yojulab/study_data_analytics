# vi ..\bin\mongod.cfg
#   bindIp: 0.0.0.0
# > use admin       # in MonogoDB
# admin> db.createUser({user: "yojulab",pwd: "!yojulab*",
#   roles: [{ role: "readWrite", db: "study_test" }]})
# admin> db.getUsers()

from pymongo import MongoClient

# MongoDB connection information
host = "mongodb://192.168.0.54:27017"
username = "yojulab"
password = "!yojulab*"
database_name = "study_test"  # Replace with your actual database name
collection_name = "some_lives"  # Replace with your actual collection name

# Data to be inserted
data = [
    {"name": "Ram", "age": "26", "city": "Hyderabad"},
    {"name": "Rahim", "age": "27", "city": "Bangalore"}
]

# Connect to MongoDB
client = MongoClient(host)
# client = MongoClient(host, username=username, password=password)
db = client[database_name]
collection = db[collection_name]

# Insert data into the collection
collection.insert_many(data)

# Close the connection
client.close()
