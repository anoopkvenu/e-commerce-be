from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.product import Product
from database import get_db


router = APIRouter()