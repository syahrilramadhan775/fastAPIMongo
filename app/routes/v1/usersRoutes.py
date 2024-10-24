from fastapi import APIRouter
from schemas.user import (userCreate, userUpdate, userPatch)
from controllers.User import UserController

users_routes= APIRouter()

@users_routes.get("/users", tags=['Users'])
async def Users():
    return await UserController.getUsers()

@users_routes.get("/users/{id}/detail", tags=['Users'])
async def Users(id):
    return await UserController.getUserDetail(id=id)

@users_routes.post("/user", tags=['Users'])
async def User(body: userCreate):
    return await UserController.createUser(body=body)

@users_routes.put("/user/{id}", tags=['Users'])
async def User(id, body: userUpdate):
    return await UserController.updateUser(id=id, body=body)

@users_routes.patch("/user/{id}/name", tags=['Users'])
async def User(id, body: userPatch):
    return await UserController.patchUser(id=id, body=body)

@users_routes.delete("/user/{id}/delete", tags=['Users'])
async def User(id):
    return await UserController.deleteUser(id=id)