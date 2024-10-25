from fastapi import Request, status, Response
from bson import ObjectId
from models.Assets import AssetsModel
from serialization.assets import (serialize_asset_model, serialize_assets_model)
from schemas.assets import AssetBase

class Settings:
    def __init__(self, collection) -> None:
        self.collection = collection

    async def _init(self):
        self.collection = await AssetsModel._collection_assets_model()
    async def collections():
        return await AssetsModel._collection_assets_model()

class AssetModelController():
    
    async def index():
        # return {"test": AssetModelController._asset_collection}
        # collection = await AssetsModel._collection_assets_model()
        # print(await test)
        # data = list(collection.find({}))
        # return {"status": status.HTTP_200_OK, "data": serialize_assets_model(data=data)}

    async def create(request: AssetBase):
        collection = await AssetsModel._collection_assets_model()
        asset = collection.insert_one({"title": request.title, "asset_url": request.asset_url})
        data = collection.find_one({"_id": ObjectId(asset.inserted_id)})
        return {"status": status.HTTP_201_CREATED, "data": serialize_asset_model(data=data)}

    async def show(id):
        collection = await AssetsModel._collection_assets_model()
        data = collection.find_one({'_id': ObjectId(id)})
        return {"status": status.HTTP_200_OK, "data": serialize_asset_model(data=data)}
    
    async def update(id, request: Request):
        return {"message": "ini update"}
    
    async def patch(id, request: Request):
        return {"message": "ini patch"}
    
    async def delete(id):
        return {"message": "ini delete"}