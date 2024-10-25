from config.fileSystem import FileSystems
from datetime import timedelta

client = FileSystems('s3')._connection_()
bucketName = FileSystems('s3')._get_bucket()
filePath = FileSystems('s3')._get_local_path()

def serialize_asset_model(data) -> dict:
    return {
        "id": str(data['_id']),
        "title": str(data['title']),
        # "asset_url": str(data['asset_url'])
        "asset_url": client.presigned_get_object(bucketName, str(data['asset_url']), expires=timedelta(hours=1))
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