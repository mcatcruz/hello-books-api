from sqlalchemy.sql.schema import ForeignKey
from app import db

class BookGenre(db.Model):
    __tablename__ = "books_genres"
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True,nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True,nullable=False)
