from fastapi import APIRouter
from models.Model import modelSessions
from schemas.Users import UserBase, UserPatch
from controllers.User import UserController

SessionDep = modelSessions
users= APIRouter(tags=['Users'])

@users.get('/user-management/users')
def user_managements(session: SessionDep):
    return UserController.index(session)

@users.get('/user-management/user/{id}')
def user_management(session: SessionDep, id):
    return UserController.show(session, id)

@users.post('/user-management/user')
def user_management_create(session: SessionDep, request: UserBase):
    return UserController.create(session, request)

@users.put('/user-management/user/{id}')
def user_management_put(session: SessionDep, id, request: UserBase):
    return UserController.update(session, id, request)

@users.patch('/user-management/user/{id}/name')
def user_management_patch(session: SessionDep, id, request: UserPatch):
    return UserController.patch(session, id, request)

@users.delete('/user-management/user/{id}/delete')
def user_management_delete(session: SessionDep, id):
    return UserController.destroy(session, id)