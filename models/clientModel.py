from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# Import the related model
from models.orderModel import ServiceOrder

class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    phone: Optional[str] = Field(max_length=20)
    address: Optional[str] = Field(max_length=255)
    email: Optional[str] = Field(max_length=100)

    # Relationship with ServiceOrder
    service_orders: List[ServiceOrder] = Relationship(back_populates="client")  # Use the imported ServiceOrder class