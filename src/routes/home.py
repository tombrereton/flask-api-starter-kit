from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from

from src.responses.welcome import WelcomeResponseSchema

home_api = Blueprint('home', __name__)


@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': WelcomeResponseSchema
        }
    }
})
def welcome():
    """
    1 liner about the routes
    A more detailed description of the endpoint
    ---
    """
    result = {'message': 'Hello World!'}
    return WelcomeResponseSchema().dump(result), 200
