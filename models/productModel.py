from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# Import the related models
from models.orderItemModel import OrderItem
from models.stockModel import Stock

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    description: Optional[str] = Field(default=None)
    price: float = Field(nullable=False)
    category: Optional[str] = Field(max_length=50)

    # Relationships
    order_items: List[OrderItem] = Relationship(back_populates="product")  # Use the imported OrderItem class
    stock: Optional[Stock] = Relationship(back_populates="product")  # Use the imported Stock class