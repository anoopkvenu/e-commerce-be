from __future__ import annotations
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional

class Status(str, Enum):
    pending = "Pending"
    completed = "Completed"


class Order(BaseModel):
    total_price: float = Field(ge=0)
    status: Status
    
    
    
class CreateOrderProducts(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)
    
    
class CreateOrder(BaseModel):
    products: List[CreateOrderProducts] = None
    

class OrderProduct(CreateOrder):
    order_id: int 
   
   