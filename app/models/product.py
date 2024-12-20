import datetime as _dt
import sqlalchemy as _sql
from sqlalchemy.orm import relationship

import database as _db

class Product(_db.Base):
    __tablename__ = "products"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, nullable=False)
    description = _sql.Column(_sql.String)
    price = _sql.Column(_sql.Float, nullable=False) 
    stock = _sql.Column(_sql.Integer) 
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.now())
    order_product = relationship("OrderProduct", back_populates="product")
    
_db.Base.metadata.create_all(_db.engine)