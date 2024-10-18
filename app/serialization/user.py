def serializeUser(data) -> dict:
    return {
        "id": str(data['_id']),
        "username": str(data['username']),
        "name": str(data['name']),
    }

def serializeUsers(data) -> list:
    return [serializeUser(data=data) for data in data]