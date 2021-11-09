from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
# os is a built-in module that enables reading of environment variables
import os

# Gives us access to database operations such as init_app()
db = SQLAlchemy()
migrate = Migrate()

# This loads the values from .env so that os module can access them
load_dotenv()

'''
Registering a Blueprint makes it so 
that the blueprints we insantiated are recognized by Flask
'''
def create_app(test_config=None):
    app = Flask(__name__)

    # If test_config is falsy, then we do not run the test environment
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    
    # Connection string that tells Flask where to find the hello_books_development database
    # Flask uses psycopg2 package to connect to the database
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)
    
    # from .routes import books_bp
    from app.models.book import Book
    from .routes_using_models import books_bp
    app.register_blueprint(books_bp)

    from app.models.author import Author
    from .routes_for_author import author_bp
    app.register_blueprint(author_bp)

    return app
