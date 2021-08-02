from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint
from flask import request

from api.schema.user_schema import UserSchema

users_api = Blueprint('users', __name__)


@swag_from({
    'parameters': [
        {
            'in': 'body',
            'name': 'User',
            'schema': UserSchema
        }
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'User Created',
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Request Body is Invalid',
        }
    }
})
@users_api.route('users', methods=['POST'])
def create_user():
    if request.method == 'POST':
        user_schema = UserSchema()

        errors = user_schema.validate(request.get_json())
        if errors:
            return errors, 400

        user = user_schema.load(request.get_json())
        return user_schema.dump(user), 200
