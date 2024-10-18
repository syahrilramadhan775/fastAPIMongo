from dotenv import dotenv_values
from pymongo import MongoClient

env = dotenv_values("../.env")    
async def connectToDatabase():
    mongoClient = MongoClient(env["MONGO_CONNECTION_STRING"])
    db = mongoClient.get_database(f'{env['DB_NAME']}')
        
    print(db)
    return db