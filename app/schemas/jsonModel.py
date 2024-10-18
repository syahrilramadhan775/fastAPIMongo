from pydantic import BaseModel

class jsonModelBase(BaseModel):
    title: str
    content_json: str
    description_json: str

class jsonModelCreate(jsonModelBase):
    pass

class jsonModelUpdate(jsonModelBase):
    pass

class scenarioPatch(BaseModel):
    conten_json: str