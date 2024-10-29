from dotenv import dotenv_values
from sqlmodel import create_engine, Session
from typing import Annotated
from fastapi import Depends

env = dotenv_values("../.env")
class DatabaseSQL():
    SQLALCHEMY_DABASE_URL= "postgresql://" + env["DB_USER"] + ":" + env["DB_PASSWORD"] + "@" + env["DB_HOST"] + "/" + env["DB_NAME"]
    engine= create_engine(SQLALCHEMY_DABASE_URL, echo=True)

    def get_session():
        with Session(DatabaseSQL.engine) as session:
            yield session

    def session_depedency():
        return Annotated[Session, Depends(DatabaseSQL.get_session)]
    
SessionDepedency= DatabaseSQL.session_depedency()