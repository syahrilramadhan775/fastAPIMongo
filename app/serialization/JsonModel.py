import json

def serializeJsonModel(data) -> dict:
    return {
        "id": str(data['_id']),
        "title": str(data['title']),
        "content_json": json.loads(data['content_json']),
        "description_json": json.loads(data['description_json']),
    }

def serializeJsonModels(data) -> list:
    return [serializeJsonModel(data=data) for data in data]

def serializeJsonModelCreate(data) -> dict:
    return {
        "title": str(data['title']),
        "content_json": json.dumps(data['content_json'])
    }

def serializeJsonModelUpdate(data) -> dict:
    return {
        "title": str(data["title"]),
        "content_json": json.dumps(data["content_json"])
    }

def serializeJsonModelPacth(data) -> dict:
    return { "content_json": json.dumps(data["content_json"]) }