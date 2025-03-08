from sqlmodel import create_engine, Session
from sqlalchemy.pool import QueuePool

class Database:
    def __init__(self, database_url: str):
        
        self.__engine = create_engine(
            database_url,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800
        )

    def get_session(self) -> Session:
        return Session(self.__engine)


