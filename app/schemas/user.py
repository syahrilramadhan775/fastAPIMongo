from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    name: str

class userCreate(UserBase):
    username: str
    name: str

class userUpdate(UserBase):
    username: str
    name: str

class userPatch(BaseModel):
    name: str