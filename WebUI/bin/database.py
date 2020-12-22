from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import os
import datetime

db_server = os.environ['DB_SERVER']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER']
db_pwd = os.environ['DB_PWD']
db_string = f'postgresql://{db_user}:{db_pwd}@{db_server}/{db_name}'


engine = create_engine(db_string)
Base = declarative_base()


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def create_session():
    return Session(bind=engine)
    

def _get_date():
    return datetime.datetime.now()

class Entity(Base):
    __tablename__ = 'entity'
    id = Column(Integer, primary_key=True)
    mac = Column(String)
    ip = Column(String)
    last_seen = Column(DateTime, default=_get_date )    

    def __repr__(self):
        return [self.id,self.mac,self.ip,self.last_seen]    
