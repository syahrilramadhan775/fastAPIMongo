from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    gender: str

class UserPatch(BaseModel):
    name: str