from pydantic import BaseModel
# from typing import Any, Annotated

class AssetBase(BaseModel):
    title: str
    asset_url: str