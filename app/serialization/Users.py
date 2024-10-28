def serialization_user(data) -> dict:
    return {
        "id": data['id'],
        "name": data['name'],
        "gender": data['gender'],
    }

def serialization_users(data) -> list:
    return [serialization_user(data=data) for data in data]
