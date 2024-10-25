from fastapi import APIRouter, Body
from controllers.Assets import AssetModelController
from schemas.assets import (AssetBase, AssetPath)

assets_routes=APIRouter(tags=['Assets Data'])

@assets_routes.get('/assets')
async def assets():
    return await AssetModelController.index()

@assets_routes.get('/asset/{id}/detail')
async def asset(id):
    return await AssetModelController.show(id=id)

@assets_routes.post('/asset')
async def asset_create(request: AssetBase):
    return await AssetModelController.create(request)

@assets_routes.post('/asset-many')
async def asset_create_many(request = Body(...)):
    return await AssetModelController.create_many(request)

@assets_routes.put('/asset/{id}')
async def asset_update(id, request: AssetBase):
    return await AssetModelController.update(id=id, request=request)

@assets_routes.patch('/asset/{id}/path')
async def asset_patch(id, request: AssetPath):
    return await AssetModelController.patch(id=id, request=request)

@assets_routes.delete('/asset/{id}/delete')
async def asset_delete(id):
    return await AssetModelController.delete(id=id)