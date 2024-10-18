from pydantic import BaseModel, Field
from typing import Optional
from databases.Collection import __collections__

class JsonModel(BaseModel):
    id: Optional[str] = Field(default_factory=str, alias="_id")
    title: str
    content_json: str
    description_json: str

    async def __collection__():
        return await __collections__(value="jsonModel_100")