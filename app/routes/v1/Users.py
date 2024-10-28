from fastapi import APIRouter, status, Depends, Query
from models.Users import Users
from sqlmodel import Session, select
from typing import Annotated
from databases.DatabaseSQL import get_session

SessionDep = Annotated[Session, Depends(get_session)]
users= APIRouter(tags=['Users'])

@users.get('/user-management/users')
def user_managements(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[Users]:
    users = session.exec(select(Users).offset(offset).limit(limit)).all()
    return users

@users.get('/user-management/user/{id}')
def user_management(session: SessionDep):
    # return {"status": status.HTTP_200_OK, "message": "Get User Data Object"}
    users = session.exec(select(Users).where(id==1)).one()

@users.post('/user-management/user')
def user_management_create():
    return {"status": status.HTTP_201_OK, "message": "Get User Data Object"}

@users.put('/user-management/user/{id}')
def user_management_put():
    return {"status": status.HTTP_200_OK, "message": "Put User Data Object"}

@users.patch('/user-management/user/{id}/name')
def user_management_patch():
    return {"status": status.HTTP_200_OK, "message": "Patch User Data Object Name Reference"}

@users.delete('/user-management/user/{id}/delete')
def user_management_delete():
    return {"status": status.HTTP_200_OK, "message": "Delete User Data Object"}