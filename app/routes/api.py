from fastapi import APIRouter
from routes.v1.Users import users

endpoints = APIRouter()

endpoints.include_router(users)