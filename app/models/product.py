import datetime as _dt
import sqlalchemy as _sql

import database as _db

class Product(_db.base):
    __tablename__ = "products"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String)
    description = _sql.Column(_sql.String)
    price = _sql.Column(_sql.Integer, primary_key=True, index=True) # Set +ve int
    stock = _sql.Column(_sql.Integer, primary_key=True, index=True) # set stock +ve
    created_at = _sql.Column(_sql.DateTime, default=_dt.timezone.utc)