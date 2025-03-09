from sqlmodel import Session  # Import Session from sqlmodel
from database.SisEstoqueDB import Database

# Initialize the Database instance (replace with your actual database URL)
database_url = "postgresql+psycopg2://user:pass@localhost:5432/SisEstoque"
db_instance = Database(database_url)

def get_db_session() -> Session:
    # Use the get_session method to yield a session
    session = next(db_instance.get_session())
    try:
        yield session
    finally:
        # Close the session when done
        session.close()