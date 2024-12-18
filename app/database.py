import config as _config

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

engine = _sql.create_engine(_config.settings.DATABASE_URL)

sessionLocal = _orm.sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = _declarative.declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()