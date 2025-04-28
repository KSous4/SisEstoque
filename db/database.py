from sqlalchemy.orm import sessionmaker
from schemas.userSchema import User, Base
from sqlalchemy import create_engine

eng = create_engine(url='postgresql+psycopg2://user:pass@localhost:5432/db')

Session = sessionmaker(bind=eng)

def getDB():
    db = Session()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(eng)