from fastapi import APIRouter
from controllers.User import UserController
from controllers.JsonModel import JsonModelController
from schemas.user import (userCreate, userUpdate, userPatch)
from schemas.jsonModel import (jsonModelBase)

endpoints= APIRouter()

@endpoints.get("/users", tags=['Users'])
async def Users():
    return await UserController.getUsers()

@endpoints.get("/users/{id}/detail", tags=['Users'])
async def Users(id):
    return await UserController.getUserDetail(id=id)

@endpoints.post("/user", tags=['Users'])
async def User(body: userCreate):
    return await UserController.createUser(body=body)

@endpoints.put("/user/{id}", tags=['Users'])
async def User(id, body: userUpdate):
    return await UserController.updateUser(id=id, body=body)

@endpoints.patch("/user/{id}/name", tags=['Users'])
async def User(id, body: userPatch):
    return await UserController.patchUser(id=id, body=body)

@endpoints.delete("/user/{id}/delete", tags=['Users'])
async def User(id):
    return await UserController.deleteUser(id=id)

# JSON MODEL
@endpoints.get("/json-models", tags=['Json Model'])
async def JsonModels():
    return await JsonModelController.getJsonModel()

@endpoints.post("/json-model", tags=['Json Model'])
async def JsonModel(body=jsonModelBase):
    return JsonModelController.createJsonModel(body=body)

# @endpoints.put("/json-model/{id}", tags=['Json Model'])
# async def JsonModel(id, body=Body(...)):
#     return JsonModelController.updateJsonModel(id=id, body=body)

# @endpoints.patch("/json-model/{id}/scenario", tags=['Json Model'])
# async def JsonModel(id, body=Body(...)):
#     return JsonModelController.patchJsonModelScenario(id=id, body=body)

@endpoints.delete("/json-model/{id}/delete", tags=['Json Model'])
async def User(id):
    return JsonModelController.deleteJsonModel(id=id)