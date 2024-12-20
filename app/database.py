from config import Settings

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from sqlalchemy.engine import URL


url = URL.create(
    **Settings.DATABASE_URL
)

engine = _sql.create_engine(url, echo=True)

sessionLocal = _orm.sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = _declarative.declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
