from fastapi import APIRouter, status

users= APIRouter(tags=['Users'])

#BluePrint
@users.get('/user-management/users')
def user_managements():
    return {"status": status.HTTP_200_OK, "message": "Get Users Collection"}

@users.get('/user-management/user/{id}')
def user_management():
    return {"status": status.HTTP_200_OK, "message": "Get User Data Object"}

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