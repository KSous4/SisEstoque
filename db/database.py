from sqlalchemy.orm import sessionmaker
from schemas.userSchema import User, Base
from sqlalchemy import create_engine

eng = create_engine(url='postgresql+psycopg2://user:pass@localhost:5432/db')

Session = sessionmaker(bind=eng)

Base.metadata.create_all(eng)