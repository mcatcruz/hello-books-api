# Many-to-many relationship practice

from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

author_bp = Blueprint('authors', __name__, url_prefix='/authors')

@author_bp.route('', methods=['GET', 'POST'])
def handle_authors():
    pass