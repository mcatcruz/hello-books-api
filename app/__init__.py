from flask import Flask

'''
Registering a Blueprint makes it so 
that the blueprints we insantiated are recognized by Flask
'''
def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app
