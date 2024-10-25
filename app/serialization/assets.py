def serialize_asset_model(data) -> dict:
    return {
        "id": str(data['_id']),
        "title": str(data['title']),
        "asset_url": str(data['asset_url'])
    }

def serialize_assets_model(data) -> list:
    return [serialize_asset_model(data=data) for data in data]

def serialize_asset_model_create(data) -> dict:
    return {
        "title": str(data['title']),
        "asset_url": str(data['asset_url'])
    }

def serialize_assets_model_create_many(data) -> list:
    return [serialize_asset_model_create(data=data) for data in data]