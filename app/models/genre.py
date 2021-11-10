from app import db
from app.models.book_genres import book_genre_table

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    book = db.relationship("Book", secondary=book_genre_table)
