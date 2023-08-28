import pymongo as mg
import pandas as pd

client = mg.MongoClient(host='mongodb://localhost:27017')

database = client['db_NHIS']

collection = database['NSC2_BND']

cursor = collection.find({})

list_BND = list(cursor)

print(list_BND)
pass