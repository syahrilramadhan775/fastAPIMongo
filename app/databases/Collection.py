from contextlib import asynccontextmanager
from databases.Mongo import connectToDatabase
from typing import Optional

@asynccontextmanager
async def lifespan(self):
    global db
    db = await connectToDatabase()
    print("start connected database success !!")
    
    yield
    print("shutdown the server!!")


async def __collections__(value: Optional[str] = None):
    global db
    print(db.get_collection(f'{value}'))
    return db.get_collection(f'{value}')