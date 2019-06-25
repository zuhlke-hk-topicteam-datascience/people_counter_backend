from flask import Flask
from flaskr.blueprints.hello_world import HELLO_WORLD

def init_db():
    '''Initializes the database'''

def create_app(test_config=None):
    '''Create the Flask app'''
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    if test_config is not None:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(HELLO_WORLD)

    return app
