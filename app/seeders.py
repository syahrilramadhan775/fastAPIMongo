from dotenv import dotenv_values
from pymongo import MongoClient
import pandas as pd
import json

env = dotenv_values("../.env") 
mongoClient = MongoClient(env["MONGO_CONNECTION_STRING"])
db = mongoClient.get_database(f'{env['DB_NAME']}')
userCollection = db.get_collection('jsonModel_100')
data= pd.read_csv('test.csv')

for index, row in data.iterrows():
    userCollection.insert_one({'title': row['name'], 'content_json': row['username'], 'description_json': row['description_json']})
    print(row['name'])