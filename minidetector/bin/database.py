from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import os

db_server = os.environ['DB_SERVER']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER']
db_pwd = os.environ['DB_PWD']
db_string = "postgresql://{}:{}@{}/{}".format(db_user, db_pwd, db_server, db_name)

engine = create_engine(db_string, pool_size=0, max_overflow=20)
Base = declarative_base()


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def create_session():
    return Session(bind=engine)


class Entity(Base):
    __tablename__ = 'entity'
    id = Column(Integer, primary_key=True)
    mac = Column(String)
    ip = Column(String)

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id} MAC={self.mac} IP={self.ip}>'
