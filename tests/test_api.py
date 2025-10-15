from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test 1: Root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Cloud Native World!"}

# Test 2: Health endpoint
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# Test 3: Create a new item
def test_create_item():
    data = {
        "name": "Storage Service",
        "description": "A cloud storage test item",
        "price": 25.5,
        "tax": 5.0
    }
    response = client.post("/items/", json=data)
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "Storage Service"
    assert result["price"] == 25.5

# Test 4: Read all items
def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
