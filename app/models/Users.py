from pydantic import BaseModel, Field
from typing import Optional
from databases.Collection import __collections__

class Users(BaseModel):
    id: Optional[str] = Field(default_factory=str, alias="_id")
    username: str
    name: str
    
    async def _collection_users():
        return await __collections__(value="users")
    