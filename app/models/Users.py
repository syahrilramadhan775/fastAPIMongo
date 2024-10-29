from sqlmodel import Field, SQLModel, select

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str | None = Field(default=None, index=True)
    gender: str | None = Field(default=None)

class UsersDML():
    def collection(session: None):
        users = session.exec(select(Users).order_by(Users.id)).all() 
        return users
    
    def first(session: None, id: int):
        users = session.exec(select(Users).where(Users.id == id)).first()
        return users
    
    def insert(session: None, request: None):
        user = Users(name=request.name, gender=request.gender)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    def update(session: None, id: int, request: None):
        user = session.exec(select(Users).where(Users.id == id)).first()
        user.name= request.name
        user.gender= request.gender

        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    def patch(session: None, id: int, request: None):
        user = session.exec(select(Users).where(Users.id == id)).first()
        user.name= request.name

        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    def delete(session: None, id: int):
        user = session.exec(select(Users).where(Users.id == id)).first()

        if user == None:
            return {"status": 404, "message": "User Not Found"}

        session.delete(user)
        session.commit()
        return {"status": 200, "message": "id "+ id +" success deleted"}