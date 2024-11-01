from fastapi import APIRouter
from schemas.user import (userCreate, userUpdate, userPatch)
from controllers.User import UserController

users_routes= APIRouter(tags=['Users'])

@users_routes.get("/users")
async def Users():
    return await UserController.getUsers()

@users_routes.get("/users/{id}/detail")
async def Users(id):
    return await UserController.getUserDetail(id=id)

@users_routes.get("/users/search")
async def user_expression(q: str):
    return await UserController.get_user_search(q)

@users_routes.post("/user")
async def User(body: userCreate):
    return await UserController.createUser(body=body)

@users_routes.put("/user/{id}")
async def User(id, body: userUpdate):
    return await UserController.updateUser(id=id, body=body)

@users_routes.patch("/user/{id}/name")
async def User(id, body: userPatch):
    return await UserController.patchUser(id=id, body=body)

@users_routes.delete("/user/{id}/delete")
async def User(id):
    return await UserController.deleteUser(id=id)