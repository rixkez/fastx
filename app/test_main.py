from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get():
    response = client.get("/books")
    assert response.status_code == 200

def test_create():
    response = client.post("/books", json={
        "title": "Random Title",
        "author": "Random Author",
        "pages": 123,
        "price": 9.99
    })
    assert response.status_code == 200

def test_update():
    response = client.put(
        "/books/695b91208f64321df89c5cde",
        json={"title": "Updated", "author": "Updated", "pages": 100, "price": 10.0}
    )
    assert response.status_code == 404 
    
def test_delete():
    response = client.delete("/books/695b91208f64321df89c5cde")
    assert response.status_code == 404
