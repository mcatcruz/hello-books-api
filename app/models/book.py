from sqlalchemy.sql.schema import ForeignKey
from app import db
from app.models.book_genres import BookGenre


# class Book inherits from db.Model, which is SQLAlchemy's Model class
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", backref='book1')
    genre = db.relationship("Genre", secondary='books_genres', backref='book2')

    def to_dict(self):
        genres = []
        for genre in self.genres:
            genres.append(genre.name)

        if self.author:
            author = self.author.name
        else:
            author = None

        return {
                    "id": self.id,
                    "title": self.title,
                    "description": self.description,
                    "genres": genres,
                    "author": author
            }