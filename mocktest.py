from sqlmodel import SQLModel, create_engine, Session
from models.userModel import User
from models.clientModel import Client
from models.orderItemModel import OrderItem
from models.productModel import Product
from models.orderModel import OrderItem
from models.stockModel import Stock

# Database URL (replace with your actual database URL)
database_url = "postgresql+psycopg2://user:pass@localhost:5432/SisEstoque"
engine = create_engine(database_url)

# Step 1: Create all tables
SQLModel.metadata.create_all(engine)
print("Tables created successfully!")
