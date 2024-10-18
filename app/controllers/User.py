from fastapi import status
from schemas.user import (userCreate, userUpdate, userPatch)
from models.Users import Users
from bson import ObjectId
from serialization.user import ( serializeUsers, serializeUser )

class UserController():
    async def getUsers():
        collection= await Users.__collection__()
        data = list(collection.find({}))
        return { "status": status.HTTP_200_OK, "data": serializeUsers(data) }
    
    async def getUserDetail(id: None):
        collection= await Users.__collection__()
        data = collection.find_one({"_id": ObjectId(id)})
        return { "status": status.HTTP_200_OK, "data": serializeUser(data) }

    async def createUser(body: userCreate):
        collection= await Users.__collection__()
        user= collection.insert_one({'username': body.username, 'name': body.name})
        data= collection.find_one({"_id": user.inserted_id})
        return { "status": status.HTTP_201_CREATED, "data": serializeUser(data) }
    
    async def updateUser(id: None, body: userUpdate):
        collection= await Users.__collection__()
        collection.update_one({"_id": ObjectId(id)}, {"$set": { 'username': body.username, 'name': body.name }})
        data= collection.find_one({"_id": ObjectId(id)})
        return { "status": status.HTTP_200_OK, "data": serializeUser(data) }
    
    async def patchUser(id: None, body: userPatch):
        collection= await Users.__collection__()
        collection.update_one({"_id": ObjectId(id)}, {"$set": { 'name': body.name }})
        data= collection.find_one({"_id": ObjectId(id)})
        return { "status": status.HTTP_200_OK, "data": serializeUser(data) }
    
    async def deleteUser(id: None):
        collection= await Users.__collection__()
        data= collection.delete_one({"_id": ObjectId(id)})
        return {
            "status": status.HTTP_200_OK, 
            "message":"Data success deleted",
            "deleted_count": data.deleted_count, 
            "acknowledged": data.acknowledged
        }
