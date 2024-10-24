def serialize_asset_model(data) -> dict:
    return {
        "id": str(data['_id']),
        "title": str(data['title']),
        "url": str(data['asset_url'])
    }

def serialize_assets_model(data) -> list:
    return [serialize_asset_model(data=data) for data in data]