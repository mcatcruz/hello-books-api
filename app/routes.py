# Blueprint is a Flask class. It provides a pattern for grouping related routes (endpoints).
from flask import Blueprint

'''
Instantiating a Blueprint class aka creating a Blueprint object
    - First argument = string that helps us identify the object in the server logs
    - Must register every new instance of Blueprint with app. 
        - See app/__init__.py
'''
hello_world_bp = Blueprint('hello_world', __name__)

'''
Defining an endpoint - Example 1
    - Note that hello_world_bp is used as a decorator.
    - Note that the .route() instance method is being used.
        - First argument = defines URL of the request
        - Second argument = defines HTTP method to use
    - The decorated function will run every time an HTTP request matches the decorator
    - The return value is the HTTP response
'''
@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    response_body = "Hello, World!"
    return response_body

'''
Defining an endpoint - Example 2
'''

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def endpoint_with_json_response():
    json_response_body = {
                            "name": "Monica Cruz",
                            "message": "Mabuhay!",
                            "hobbies": ["Reading", "Baking", "Crossword Puzzles"]
                         }
    return json_response_body