from models.Users import UsersDML
from serialization.Users import (serialization_users, serialization_user)
from fastapi import status
class UserController:

    def index(session: None):
        return {"status": status.HTTP_200_OK, "data": serialization_users(UsersDML.collection(session))}
    
    def show(session: None, id: int):
        users = UsersDML.first(session, id)
        
        if users == None:
            return {"status": 404, "message": "User Not Found"}
        
        return {"status": status.HTTP_200_OK, "data": serialization_user(UsersDML.first(session, id))}
    
    def create(session: None, request: None):
        return {"status": status.HTTP_201_CREATED, "data": serialization_user(UsersDML.insert(session, request))}
    
    def update(session: None, id: int, request: None):
        return {"status": status.HTTP_200_OK, "data": serialization_user(UsersDML.update(session, id, request))}

    def patch(session: None, id: int, request: None):
        return {"status": status.HTTP_200_OK, "data": serialization_user(UsersDML.patch(session, id, request))}

    def destroy(session: None, id: int):
        return UsersDML.delete(session, id)