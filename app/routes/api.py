from fastapi import APIRouter
from routes.v1.usersRoutes import users_routes
from routes.v1.jsonModelRoutes import json_models_routes

endpoints= APIRouter()

endpoints.include_router(users_routes)
endpoints.include_router(json_models_routes)