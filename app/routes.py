# Blueprint is a Flask class. It provides a pattern for grouping related routes (endpoints).
from flask import Blueprint, jsonify
from flask.json import tojson_filter

'''
Instantiating a Blueprint class aka creating a Blueprint object
    - First argument = string that helps us identify the object in the server logs
    - Must register every new instance of Blueprint with app. 
        - See app/__init__.py
'''
hello_world_bp = Blueprint('hello_world', __name__)

'''
Defining an endpoint - Example 1
    - Note that hello_world_bp is a decorator.
    - Note that the .route() instance method is being used.
        - First argument = defines URL of the request
        - Second argument = defines HTTP method to use
    - The decorated function will run every time an HTTP request matches the decorator
    - The return value is the HTTP response
'''
@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    response_body = "Hello, World!"
    return response_body

'''
Defining an endpoint - Example 2
'''

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def endpoint_with_json_response():
    json_response_body = {
                            "name": "Monica Cruz",
                            "message": "Mabuhay!",
                            "hobbies": ["Reading", "Baking", "Crossword Puzzles"]
                         }
    return json_response_body

'''
Debugging a broken endpoint
'''

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    # The broken code: response_body["hobbies"] + new_hobby
    response_body["hobbies"].append(new_hobby)
    return response_body

# Read All Books Endpoint

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

# This list represents the database
books = [
    Book(1, 'Notes from A Liar and Her Dog', 'children \'s fiction'),
    Book(2, 'In The Dream House', 'autobiography'),
    Book(3, 'Ten Women', 'fiction')
]

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('', methods=['GET'])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            'id': book.id,
            'title': book.title,
            'description': book.description
        })
    return jsonify(books_response)

# Read One Book Endpoint
@books_bp.route('/<book_id>', methods=['GET'])
def handle_one_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book_id == book.id:
            return jsonify({
                'id': book.id, 
                "title": book.title, 
                "description": book.description
                })
