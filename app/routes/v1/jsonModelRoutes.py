from fastapi import APIRouter, Request, Body
from controllers.JsonModel import JsonModelController

json_models_routes= APIRouter(tags=['Json Model'])

@json_models_routes.get("/json-models")
async def JsonModels():
    return await JsonModelController.getJsonModel()

@json_models_routes.post("/json-model")
async def JsonModel(request: Request, body=Body( ... )):
    return await JsonModelController.createJsonModel(request=request, body=body)

@json_models_routes.put("/json-model/{id}")
async def JsonModel(request: Request, id, body=Body(...)):
    return await JsonModelController.updateJsonModel(request=request, id=id, body=body)

@json_models_routes.patch("/json-model/{id}/scenario")
async def JsonModel(request: Request, id, body=Body(...)):
    return await JsonModelController.patchJsonModelScenario(request=request, id=id, body=body)

@json_models_routes.delete("/json-model/{id}/delete")
async def User(request: Request, id):
    return await JsonModelController.deleteJsonModel(request=request, id=id)