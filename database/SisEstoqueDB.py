from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
from typing import Generator

class Database:
    def __init__(self, database_url: str):
        # Engine is created once and reused
        self.__engine = create_engine(
            database_url,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800
        )

        # Create a session factory using SQLModel's Session class
        self.__SessionFactory = sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine, class_=Session
        )

    def get_session(self) -> Generator[Session, None, None]:
        # Create a new session
        session = self.__SessionFactory()
        try:
            yield session
        finally:
            # Close the session when done
            session.close()

    def create_tables(self) -> None:
        # Create tables in the database based on models
        SQLModel.metadata.create_all(self.__engine)