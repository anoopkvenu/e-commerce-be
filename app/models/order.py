import datetime as _dt
import sqlalchemy as _sql
from sqlalchemy.orm import relationship
from .product import Product

import database as _db
    

class Order(_db.Base):
    __tablename__ = "orders"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    total_price = _sql.Column(_sql.Float, nullable=False) 
    status = _sql.Column(_sql.String, nullable=False) #define enum
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.now())
    order_product = relationship("OrderProduct", back_populates="order")
    
    
class OrderProduct(_db.Base):
    __tablename__ = "order_products"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    order_id = _sql.Column(_sql.Integer, _sql.ForeignKey("orders.id"))
    product_id = _sql.Column(_sql.Integer, _sql.ForeignKey("products.id"))
    quantity = _sql.Column(_sql.Integer, nullable=False)
    order = relationship("Order", back_populates="order_product")
    product = relationship("Product", back_populates="order_product")
    
_db.Base.metadata.create_all(_db.engine)

# note: Can be add fields like tracking details, addess details, payment details. Skiped those fields for now