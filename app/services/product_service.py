from sqlalchemy.orm import Session
from schemas.product import Product as ProductSchema
from models.product import Product as ProductModel

def create_new_product(product: ProductSchema, db: Session):
    product_obj = ProductModel(
        name = product.name,
        description = product.description,
        price = product.price,
        stock = product.stock
    )
    db.add(product_obj)
    db.commit()
    db.refresh(product_obj)
    return product_obj
    