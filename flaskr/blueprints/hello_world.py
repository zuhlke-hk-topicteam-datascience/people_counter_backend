from flask import Blueprint

HELLO_WORLD = Blueprint('hello_world', __name__)

 # a simple page that says hello
@HELLO_WORLD.route('/')
def hello():
    return 'Hello, World!'
