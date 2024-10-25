from fastapi import status, Body
from bson import ObjectId
from models.Assets import AssetsModel
from serialization.assets import (serialize_asset_model, serialize_assets_model, serialize_assets_model_create_many)
from schemas.assets import (AssetBase, AssetPath)

class AssetModelController():
    async def index():
        collection = await AssetsModel._collection_assets_model()
        data = list(collection.find({}))
        return {"status": status.HTTP_200_OK, "data": serialize_assets_model(data=data)}

    async def create(request: AssetBase):
        collection = await AssetsModel._collection_assets_model()
        asset = collection.insert_one({"title": request.title, "asset_url": request.asset_url})
        data = collection.find_one({"_id": ObjectId(asset.inserted_id)})
        return {"status": status.HTTP_201_CREATED, "data": serialize_asset_model(data=data)}
    
    async def create_many(request: None):
        collection = await AssetsModel._collection_assets_model()
        requests_data = serialize_assets_model_create_many(request)
        collection.insert_many(requests_data)
        data = collection.find().sort('_id', -1).limit(len(requests_data))
        return {"status": status.HTTP_201_CREATED, "data": serialize_assets_model(data=data)}

    async def show(id):
        collection = await AssetsModel._collection_assets_model()
        data = collection.find_one({'_id': ObjectId(id)})
        return {"status": status.HTTP_200_OK, "data": serialize_asset_model(data=data)}
    
    async def update(id, request: AssetBase):
        collection = await AssetsModel._collection_assets_model()
        collection.update_one({'_id': ObjectId(id)}, {"$set": {"title": request.title, "asset_url": request.asset_url}})
        data = collection.find_one({"_id": ObjectId(id)})
        return {"status": status.HTTP_200_OK, "data": serialize_asset_model(data=data)}
    
    async def patch(id, request: AssetPath):
        collection = await AssetsModel._collection_assets_model()
        collection.update_one({"_id": ObjectId(id)}, {"$set": {"asset_url": request.asset_url}})
        data = collection.find_one({"_id": ObjectId(id)})
        return {"status": status.HTTP_200_OK, "data": serialize_asset_model(data=data)}
    
    async def delete(id):
        collection = await AssetsModel._collection_assets_model()
        data = collection.delete_one({"_id": ObjectId(id)})
        return {
            "status": status.HTTP_200_OK, 
            "message":"Data success deleted",
            "deleted_count": data.deleted_count,
        }