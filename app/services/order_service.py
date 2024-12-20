from __future__ import annotations
from sqlalchemy.orm import Session
from models.product import Product as ProductModel
from schemas.order import Status
from models.order import Order as OrderModel, OrderProduct as OrderProductModel
from typing import List


def create_new_order(cart_list, db: Session):
    products = fetch_products(cart_list, db)
    product_obj = OrderModel(status =  Status.pending)
    product_obj = validate_create_order(cart_list, products, product_obj, db)

    return product_obj


def fetch_products(product_list, db:Session):
    product_ids = list(map(lambda v: v.product_id, product_list.products))
    return db.query(ProductModel).filter(ProductModel.id.in_(product_ids)).all()


def validate_create_order(cart_list, products, product_obj, db):
    total_price = 0
    order_items = []
    new_inventory = []
    
    for cart_item in cart_list.products:
        product = next(item for item in products if item.id == cart_item.product_id)
        if product.stock < cart_item.quantity:
            raise Exception("Required stock is not available for the product.")

        total_price = total_price + (cart_item.quantity * product.price)
        order_items.append(create_order_obj(product, cart_item))
        
        new_inventory.append({"id": product.id, "stock": product.stock - cart_item.quantity})
    
    product_obj.total_price = total_price

    db.add(product_obj)
    db.commit()
    db.refresh(product_obj)

    for item in order_items:
        item.order_id = product_obj.id
    
    db.add_all(order_items)
    db.commit()

    update_stock(new_inventory, db)
    
    return product_obj


def create_order_obj(product, cart_item): 
        order_product = OrderProductModel(
            product_id = product.id,
            quantity = cart_item.quantity
        )
        return order_product
    
    
def update_stock(inventory, db):
    for item in inventory:
        db.query(ProductModel).filter_by(id=item["id"]).update({ProductModel.stock: item["stock"]})
    db.commit()