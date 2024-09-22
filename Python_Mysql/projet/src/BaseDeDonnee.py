from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://root@db/Python_Mysql" 
ConnexionBDD = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ConnexionBDD)

def get_db():
    db = SessionLocal()
    try:                   
        yield db
    finally:
        db.close()

BDD = declarative_base()