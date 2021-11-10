# Many-to-many relationship practice

from app import db
from app.models.book import Book
from app.models.author import Author
from flask import Blueprint, jsonify, make_response, request

author_bp = Blueprint('authors', __name__, url_prefix='/authors')

@author_bp.route('', methods=['GET', 'POST'])
def handle_authors():
    authors = Author.query.all()

    if request.method == 'GET':
        return jsonify([{"name": author.name, "id": author.id} for author in authors])

    elif request.method == 'POST':
        request_body = request.get_json()
        new_author = Author(name=request_body['name'])

        db.session.add(new_author)
        db.session.commit()
        
        return make_response(f"Author {new_author.name} successfully created.", 201)

@author_bp.route('/<author_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_one_author(author_id):
    author = Author.query.get(author_id)
    if author is None:
        return make_response('Author not found', 404)

    if request.method == 'GET':
        return {'name': author.name, 'id': author.id}

    elif request.method == 'PUT':
        form_data = request.get_json()
        author.name = form_data['name']

        db.session.commit()

        return make_response(f'Author {author.name} successfully updated')
    
    elif request.method == 'DELETE':
        db.session.delete(author)
        db.session.commit()

        return make_response(f' Author {author.name} successfully deleted')

@author_bp.route('/<author_id>/books', methods=['GET', 'POST'])
def handle_authors_books(author_id):
    author = Author.query.get(author_id)
    if author is None:
        return make_response('Author not found', 404)

    if request.method == 'POST':
        request_body = request.get_json()
        new_book = Book(title=request_body['title'],
                        description=request_body['description'],
                        author=author)
        
        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} by {new_book.author.name} successfully created", 201)

    elif request.method == 'GET':
        # this returns a list of all the books that belong to a single author
        return jsonify([{"author_id": book.author_id,
                            "book_id": book.id,
                            "title": book.title,
                            "description": book.description} for book in author.books])