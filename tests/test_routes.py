'''
	This file will hold the tests for the code in our app/routes.py file.
    Remember: Arrange Act Assert
'''

# The client parameter will detect the client fixture in conftest.py
def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
        }
    
def test_no_data_in_test_database(client):
    # Act
    response = client.get("books/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

def test_get_all_books_with_data(client, two_saved_books):
    # Act
    response = client.get('/books')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
        },
        {
        "id": 2,
        "title": "Mountain Book",
        "description": "i luv 2 climb rocks"
        }]

def test_post_book(client):
    # Arrange
    book = {"title": "Wind Book", "description": "breezy"}
    # Act
    response = client.post('/books', json = book)
 
    # Assert
    assert response.status_code == 201

    response = client.get("/books")
    response_body = response.get_json()
    book["id"] = 1
    assert book in response_body