import datetime as _dt
import sqlalchemy as _sql

import database as _db

class Product(_db.Base):
    __tablename__ = "products"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String)
    description = _sql.Column(_sql.String)
    price = _sql.Column(_sql.Float) 
    stock = _sql.Column(_sql.Integer) 
    created_at = _sql.Column(_sql.DateTime, default=_dt.timezone.utc)
    
_db.Base.metadata.create_all(_db.engine)