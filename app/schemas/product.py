from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    description: str
    price: float = Field(ge=0)
    stock: int = Field(ge=0)
   