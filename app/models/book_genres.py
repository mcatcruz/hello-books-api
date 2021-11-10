from app import db

book_genre_table = db.Table('book_genre', db.Model.metadata, 
    db.Column('book_id', db.ForeignKey('book.id'), primary_key=True),
    db.Column('genre_id', db.ForeignKey('genre.id'), primary_key=True)
)