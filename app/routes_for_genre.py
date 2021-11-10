from app import db
from app.models.genre import Genre
from flask import Blueprint, jsonify, make_response, request

genre_bp = Blueprint('genres', __name__, url_prefix='/genres')

@genre_bp.route('', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        genres = Genre.query.all()
        return jsonify([{"id": genre.id, "name": genre.name}for genre in genres])
    
    elif request.method == 'POST':
        request_body = request.get_json()

        new_genre = Genre(name=request_body["name"])

        db.session.add(new_genre)
        db.session.commit()

        return make_response(f"Genre, {new_genre.name}, successfully created.", 201)
