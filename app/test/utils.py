from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.product import Product
from config import Settings


class TestDatabase:
    def __init__(self, session: Session):
        self.session = session
        
    def populate_test_database(self):
        product_1 = Product(
            name="Product 2",
            stock=10,
            price=10
        )
        
        product_2 = Product(
            name="Product 1",
            stock=4,
            price=10
        )
        
        product_3 = Product(
            name="Product 3",
            stock=84,
            price=10
        )
        
        self.session.add_all([product_1, product_2, product_3])
        self.session.commit()


def override_get_db():
    test_engine = create_engine(Settings.TEST_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()