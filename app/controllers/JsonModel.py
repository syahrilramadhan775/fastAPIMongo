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
from schemas.jsonModel import jsonModelBase

class JsonModelController():
    async def getJsonModel():
        collection = await JsonModel.__collection__()
        data = list(collection.find({}))
        return JSONResponse(content={"status": status.HTTP_200_OK, "data": serializeJsonModels(data)})

    async def createJsonModel(body: jsonModelBase):
        print(body.title)
        # collection = await JsonModel.__collection__()
        # user= collection.insert_one(serializeJsonModelCreate(body))
        # data= collection.find_one({"_id": user.inserted_id})
        # return { "status": status.HTTP_201_CREATED, "data": serializeJsonModel(data) }
    
    # async def updateJsonModel(id: None, body: None):
    #     collection = await JsonModel.__collection__()
    #     collection.update_one({"_id": ObjectId(id)}, {"$set": serializeJsonModelUpdate(body)})
    #     data= collection.find_one({"_id": ObjectId(id)})
    #     return { "status": status.HTTP_200_OK, "data": serializeJsonModel(data) }
    
    # async def patchJsonModelScenario(request: None, id: None, body: None):
    #     collection = await JsonModel.__collection__()
    #     collection.update_one({"_id": ObjectId(id)}, {"$set": serializeJsonModelPacth(body)})
    #     data= collection.find_one({"_id": ObjectId(id)})
    #     return { "status": status.HTTP_200_OK, "data": serializeJsonModel(data) }

    # async def deleteJsonModel(request: None, id: None):
        collection = await JsonModel.__collection__()
        data= collection.delete_one({"_id": ObjectId(id)})
        return {
            "status": status.HTTP_200_OK, 
            "message":"Data success deleted",
            "deleted_count": data.deleted_count, 
            "acknowledged": data.acknowledged
        }
