from fastapi import APIRouter
from .v1.product_routes import router as route_product
from .v1.order_routes import router as route_order

router = APIRouter()

#V1 routes

router.include_router(route_product, prefix="/v1/products", tags=["products"])
router.include_router(route_order, prefix="/v1/orders", tags=["order"])