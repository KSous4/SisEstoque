from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql+psycopg2://user:pass@localhost/logs"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
