from app import db
from app.models.book_genres import BookGenre

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    book = db.relationship("Book", secondary='books_genres')
