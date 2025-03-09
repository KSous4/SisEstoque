from sqlmodel import SQLModel,Field
from typing import Optional
import uuid

class Users(SQLModel, table=True):

    id :uuid.UUID = Field(default_factory=uuid.uuid4,primary_key=True)
    username:str 
    email:str 
    passwd:str
    role:str
    