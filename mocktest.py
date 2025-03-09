from sqlmodel import SQLModel, create_engine, Session
from models.userModel import Users  # Import your Users model
import uuid

# Database URL (replace with your actual database URL)
database_url = "postgresql+psycopg2://user:pass@localhost:5432/SisEstoque"
engine = create_engine(database_url)

# Step 1: Create all tables
SQLModel.metadata.create_all(engine)
print("Tables created successfully!")

# Step 2: Insert a mocked user
with Session(engine) as session:
    # Create a mocked user
    mocked_user = Users(
        id=uuid.uuid4(),  # Generate a UUID
        username="testuser",
        email="testuser@example.com",
        passwd="hashedpassword",  # Replace with an actual hashed password
        role="user"
    )

    # Add and commit the user to the database
    session.add(mocked_user)
    session.commit()

print("Mocked user inserted successfully!")