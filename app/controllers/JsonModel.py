from serialization.JsonModel import (
    serializeJsonModels, 
    serializeJsonModel, 
    serializeJsonModelCreate, 
    serializeJsonModelUpdate, 
    serializeJsonModelPacth,
)
from bson import ObjectId
from models.JsonModel import JsonModel
from fastapi import status
from fastapi.responses import JSONResponse

class JsonModelController():
    async def getJsonModel():
        collection = await JsonModel._collection_json_model()
        data = list(collection.find({}))
        return JSONResponse(content={"status": status.HTTP_200_OK, "data": serializeJsonModels(data)})

    async def createJsonModel(request: None, body: None):
        collection = await JsonModel._collection_json_model()
        user= collection.insert_one(serializeJsonModelCreate(body))
        data= collection.find_one({"_id": user.inserted_id})
        return JSONResponse(content={"status": status.HTTP_200_OK, "data": serializeJsonModel(data)})
    
    async def updateJsonModel(id: None, body: None):
        collection = await JsonModel._collection_json_model()
        collection.update_one({"_id": ObjectId(id)}, {"$set": serializeJsonModelUpdate(body)})
        data= collection.find_one({"_id": ObjectId(id)})
        return JSONResponse(content={"status": status.HTTP_200_OK, "data": serializeJsonModel(data)})
    
    async def patchJsonModelScenario(request: None, id: None, body: None):
        collection = await JsonModel._collection_json_model()
        collection.update_one({"_id": ObjectId(id)}, {"$set": serializeJsonModelPacth(body)})
        data= collection.find_one({"_id": ObjectId(id)})
        return JSONResponse(content={"status": status.HTTP_200_OK, "data": serializeJsonModel(data)})

    async def deleteJsonModel(request: None, id: None):
        collection = await JsonModel._collection_json_model()
        data= collection.delete_one({"_id": ObjectId(id)})
        return {
            "status": status.HTTP_200_OK, 
            "message":"Data success deleted",
            "deleted_count": data.deleted_count, 
            "acknowledged": data.acknowledged
        }
