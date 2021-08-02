from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify
from flask import request

from src.dtos.user import User
from src.schema.user import UserSchema
from src.services import queue_client
from src.services.custom_serializer import JSONSerializer

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

        user_as_snake_case = user_schema.dump(request.get_json())
        user_dto = JSONSerializer.deserialize(User, user_as_snake_case)

        add_msg = queue_client.add_create_user_job(user_dto)

        return jsonify(add_msg), 200
