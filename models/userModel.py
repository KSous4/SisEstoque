from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# Import the related model
from models.orderModel import ServiceOrder

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    email: str = Field(max_length=100, unique=True, nullable=False)
    password: str = Field(max_length=100, nullable=False)
    role: str = Field(max_length=50, nullable=False)

    # Relationship with ServiceOrder
    service_orders: List[ServiceOrder] = Relationship(back_populates="user")  # Use the imported ServiceOrder class