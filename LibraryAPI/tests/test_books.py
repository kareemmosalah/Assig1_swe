import pytest
import json

def test_add_book(client):
    response = client.post('/api/books', json={
        "title": "Test Book",
        "author": "Author Name",
        "published_year": 2023,
        "isbn": "12345",
        "genre": "Fiction"
    })
    assert response.status_code == 201

def test_list_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200