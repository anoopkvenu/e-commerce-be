from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.order import Order, CreateOrder
from database import get_db

from services.order_service import create_new_order


router = APIRouter()

@router.post("/")

def create_order(order: CreateOrder, db: Session = Depends(get_db)):
    order = create_new_order(order, db)
    return order


