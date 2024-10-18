from fastapi import FastAPI
from databases.Collection import lifespan
from routes.v1.api import endpoints

app = FastAPI(lifespan=lifespan)

app.include_router(endpoints, prefix='/api/v1')