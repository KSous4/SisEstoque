from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

# Import the related models
from models.orderModel import ServiceOrder
from models.productModel import Product

class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    service_order_id: int = Field(foreign_key="serviceorder.id", nullable=False)
    product_id: int = Field(foreign_key="product.id", nullable=False)
    quantity: int = Field(nullable=False)
    unit_price: float = Field(nullable=False)

    # Relationships
    service_order: ServiceOrder = Relationship(back_populates="order_items")  # Use the imported ServiceOrder class
    product: Product = Relationship(back_populates="order_items")  # Use the imported Product class