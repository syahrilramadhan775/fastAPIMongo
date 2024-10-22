from fastapi import FastAPI
from databases.Collection import lifespan
from routes.v1.api import endpoints
import uvicorn
from dotenv import dotenv_values

env = dotenv_values("../.env")   
app = FastAPI(lifespan=lifespan)
app.include_router(endpoints, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run("main:app", host=env["HOST"], port=int(env["PORT"]), reload=env["RELOAD"])
