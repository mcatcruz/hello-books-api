from flask import Flask

'''
Registering a Blueprint: see line 9-10
'''
def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app
