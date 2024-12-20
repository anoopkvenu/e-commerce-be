from fastapi.testclient import TestClient

from app.main import app
from database import get_db
from test.fixtures import create_and_delete_database
from test.utils import override_get_db


client = TestClient(app)
app.dependency_overrides[get_db] = override_get_db


def test_product_get():
    response = client.get("v1/products")
    assert response.status_code == 200
    products = response.json()
    print(products)
    assert len(products) == 3
    assert products[1]["stock"] == 4


def test_create_product():
    data = {
        "name": "New Prod",
        "description": "string",
        "price": "2.0",
        "stock": "2"
    }
    response = client.post("v1/products", json= data,  headers={"content-type": "application/json"})
    assert response.status_code == 200
    product = response.json()
    assert product["name"] == "New Prod"
    
    

def test_order_create():
    data = {
        "products": [{
            "product_id": 1,
            "quantity": 1
            }, {
            "product_id": 2,
            "quantity": 1
            }
        ]
    }
    response = client.post("v1/orders", json= data,  headers={"content-type": "application/json"})
    assert response.status_code == 200