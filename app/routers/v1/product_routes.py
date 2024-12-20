from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.product import Product
from database import get_db

from services.product_service import create_new_product, get_products


router = APIRouter()

@router.post("/")

def create_product(product: Product, db: Session = Depends(get_db)):
    product = create_new_product(product, db)
    return product

@router.get("/")

def get_all_product(db: Session = Depends(get_db)):
    items = get_products(db)
    return items

