from routes.api import endpoints
from dotenv import dotenv_values
from fastapi import FastAPI
import uvicorn

env = dotenv_values("../.env")   
app = FastAPI()
app.include_router(endpoints, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run("main:app", host=env["HOST"], port=int(env["PORT"]), reload=env["RELOAD"])