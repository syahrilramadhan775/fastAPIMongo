from dotenv import dotenv_values
from sqlmodel import create_engine, Session

env = dotenv_values("../.env")
connection= env["DB_CONNECTION"]
host= env["DB_HOST"]
user= env["DB_USER"]
password= env["DB_PASSWORD"]
port= env["DB_PORT"]
dbname= env["DB_NAME"]

SQLALCHEMY_DABASE_URL= "postgresql://" + user + ":" + password + "@" + host + "/" + dbname

engine= create_engine(SQLALCHEMY_DABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session