# This corresponds to the Model Setup lesson in Learn

# Blueprint is a Flask class. It provides a pattern for grouping related routes (endpoints).
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request
# The imported request object (see line 7) represents the current HTTP request.
# make_response is a helper method

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
        # Using query params: Title
        title_query = request.args.get("title")
        if title_query:
            books = Book.query.filter_by(title=title_query)
        else:
            # Using SQLAlchemy syntax to access all books from the database
            books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
    elif request.method == 'POST':
        # request_body will hold the contents of the HTTP request from the user and format it in a Python data structure.
        request_body = request.get_json()
        # a Book instance is created using the data in request_body
        new_book = Book(title=request_body["title"],
                        description = request_body["description"])
    # This adds the newly made changes to the database
    db.session.add(new_book)
    # This will save the data new Book instance to the database
    db.session.commit()

    # This returns a response to the user. Note that we are also returning a response status.
    return make_response(f'Book, "{new_book.title}", successfully created.', 201)

# Creating An Endpoint for a Single Book
@books_bp.route('/<book_id>', methods = ['GET', 'PUT', 'DELETE'])
def handle_a_book(book_id):
    # SQLAlchemy syntax to access a record by primary key, such as book_id
        # If query.get() does not match any book instances, it will return None
    book = Book.query.get(book_id)
    if book is None:
        return make_response('', 404)
    if request.method == 'GET':
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    elif request.method == 'PUT':
        form_data = request.get_json()

        book.title = form_data["title"]
        book.description = form_data["description"]

        db.session.commit()
        
        return make_response(f"Book, \"{book.title}\", successfully updated")
        
    elif request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book {book.title} successfully deleted")

        
