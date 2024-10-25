from pydantic import BaseModel

class AssetBase(BaseModel):
    title: str
    asset_url: str

class AssetPath(BaseModel):
    asset_url: str