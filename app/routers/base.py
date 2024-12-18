from fastapi import APIRouter
from .product_routes import router as route_product

router = APIRouter()

router.include_router(route_product, prefix="/products", tags=["products"])