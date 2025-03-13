from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date

# Import the related models
from models.userModel import User
from models.clientModel import Client
from models.orderItemModel import OrderItem

class ServiceOrder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    issue_date: date = Field(nullable=False)
    status: str = Field(max_length=50, nullable=False)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    client_id: int = Field(foreign_key="client.id", nullable=False)

    # Relationships
    user: User = Relationship(back_populates="service_orders")  # Use the imported User class
    client: Client = Relationship(back_populates="service_orders")  # Use the imported Client class
    order_items: List[OrderItem] = Relationship(back_populates="service_order")  # Use the imported OrderItem class