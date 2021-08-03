from http import HTTPStatus
from flask import Blueprint
from apifairy import response

from src.responses.welcome import WelcomeResponseSchema

home_api = Blueprint('home', __name__)


@home_api.route('/')
@response(WelcomeResponseSchema)
def welcome():
    """
    1 liner about the routes
    A more detailed description of the endpoint
    ---
    """
    result = {'message': 'Hello World!'}
    return WelcomeResponseSchema().dump(result), 200
