from app import db

# class Book inherits from db.Model, which is SQLAlchemy's Model class
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)