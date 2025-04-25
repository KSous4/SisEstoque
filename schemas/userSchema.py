from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from time import time

Base = declarative_base()

class User(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    createdAt = Column(Float, default=time())
    email = Column(String)
    name = Column(String)
    passwd = Column(String) 


    def __repr__(self):
        return f'<User(id={self.id},createdAt={self.createdAt},email={self.email},name={self.name},passwd={self.passwd})>'