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
        return jsonify([{"name": author.name} for author in authors])

    elif request.method == 'POST':
        request_body = request.get_json()
        new_author = Author({"name": request_body['name']})

        db.session.add(new_author)
        db.session.commit()
        
        return make_response(f"Author {new_author.title} successfully created.", 201)