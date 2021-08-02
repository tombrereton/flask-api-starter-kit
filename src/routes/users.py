from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify
from flask import request

from src.config import DefaultConfig
from src.dtos.user import User
from src.schema.user import UserSchema, UsersSchema
from src.services import queue_client
from src.services.custom_serializer import JSONSerializer
from src.services.parser import parse_as_bool

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


@swag_from({
    'get': {
        'parameters': [
            {
                'in': 'query',
                'name': 'isSnakeCase',
                'type': 'bool',
                'default': 'False'
            }
        ]
    },
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get User',
            'schema': UsersSchema
        }
    }
})
@users_api.route('users', methods=['GET'])
def get_user():
    if request.method == 'GET':
        is_snake_case = request.args.get("isSnakeCase")

        user = User(user_name=DefaultConfig.DEFAULT_USERNAME)
        users = [user]

        if parse_as_bool(is_snake_case):
            return jsonify(users), 200

        serialized = JSONSerializer.serialize(users)
        return jsonify(serialized), 200


