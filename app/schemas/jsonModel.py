from pydantic import BaseModel, Json
from typing import Any

class jsonModelBase(BaseModel):
    title: str
    content_json: Json[Any]
    description_json: Json[Any]

class jsonModelCreate(jsonModelBase):
    pass

class jsonModelUpdate(jsonModelBase):
    pass

class scenarioPatch(BaseModel):
    conten_json: str