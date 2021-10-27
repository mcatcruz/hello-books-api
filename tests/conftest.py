'''
A standard pytest file that holds test configurations and common test helper functions. 
Essentially, this file is run before any other test files. 
This allows fixtures registered here to be available to any other test file.
'''

import pytest
from app import create_app
from app import db

@pytest.fixture
def app():
    # When we run our tests, this line will run and create an app object. It's using the same create_app function defined in app/__init__.py
    # Passing in a truthy config object so that it will run testing environment (see __init__.py)
    app = create_app({"TESTING": True})

    # This syntax designates that the following code should have an application context. 
    # This lets various functionality in Flask determine what the current running app is. 
    # This is particularly important when accessing the database associated with the app.
    with app.app_context():
        # At the start of each test, this recreates the tables needed for our models.
        # The recreated tables begin empty.
        db.create_all()
        # The fixture will suspend here and return the value of app for use in tests or other fixtures
        # The lines after the yield statement will run after the test using the the value of app has been completed.
        yield app
    
    # After the test runs, this code specifies that we should drop all of the tables, deleting any data that was created during the test.
    with app.app_context():
        db.drop_all()

# This fixture will request the existing app fixture to run first.
@pytest.fixture
# The responsibility of this fixture is to make a test client, which is an object able to simulate a client making HTTP requests.
# In our tests, we will use this fixture to send HTTP requests.
def client(app):
    return app.test_client()        


from app.models.book import Book
@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(title="Ocean Book",
                      description="watr 4evr")
    mountain_book = Book(title="Mountain Book",
                         description="i luv 2 climb rocks")

    db.session.add_all([ocean_book, mountain_book])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()