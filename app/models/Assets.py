from pydantic import BaseModel, Field
from typing import Optional
from databases.Collection import __collections__

class AssetsModel(BaseModel):
    id: Optional[str] = Field(default_factory=str, alias="_id")
    title: str
    asset_url: str

    async def _collection_assets_model():
        return await __collections__(value="assets")