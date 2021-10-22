# This corresponds to the Model Setup lesson in Learn

# Blueprint is a Flask class. It provides a pattern for grouping related routes (endpoints).
from flask import json
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request
from flask.json import tojson_filter

'''
Instantiating a Blueprint class aka creating a Blueprint object
    - First argument = string that helps us identify the object in the server logs
    - Must register every new instance of Blueprint with app. 
        - See app/__init__.py
'''

# Creating An Endpoint
books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return json(books_response)
    elif request.method == 'POST':
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description = request_body["description"])
    
    db.session.add(new_book)
    db.session.commit()

    return make_response(f'Book {new_book.title} successfully created.', 201)

# Creating An Endpoint for a Single Book
@books_bp.route('/<book_id>', methods = ['GET'])
def handle_a_book(book_id):
    book = Book.query.get(book_id)
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
    }