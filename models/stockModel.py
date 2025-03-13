from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date

# Import the related model
from models.productModel import Product

class Stock(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id", unique=True, nullable=False)
    available_quantity: int = Field(nullable=False)
    last_updated: date = Field(nullable=False)

    # Relationship with Product
    product: Product = Relationship(back_populates="stock")  # Use the imported Product class