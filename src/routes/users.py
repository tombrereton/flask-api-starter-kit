from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify
from flask import request
from apifairy import authenticate, body, response, other_responses


from src.config import DefaultConfig
from src.requests.user import UserRequestSchema, UserRequest
from src.responses.user import UserResponseSchema
from src.dtos.user import UserDto
from src.services import queue_client
from src.services.pascal_to_snake_serializer import JSONSerializer
from src.services.snake_to_pascal_serializer import JSONSerializer as ToPascalJson
from src.services.parser import parse_as_bool

users_api = Blueprint('users', __name__)


# @swag_from({
#     'parameters': [
#         {
#             'in': 'body',
#             'name': 'User',
#             'schema': UserRequestSchema
#         }
#     ],
#     'responses': {
#         HTTPStatus.OK.value: {
#             'description': 'User Created',
#         },
#         HTTPStatus.BAD_REQUEST.value: {
#             'description': 'Request Body is Invalid',
#         }
#     }
# })
@users_api.route('users', methods=['POST'])
@body(UserRequestSchema)
def create_user():
    """Create a User."""
    if request.method == 'POST':
        user_schema = UserRequestSchema()
        errors = user_schema.validate(request.get_json())
        if errors:
            return errors, 400

        user_pascal = JSONSerializer.deserialize(UserRequest, request.get_json())
        user_snake_case = JSONSerializer.deserialize(UserDto, JSONSerializer.serialize(user_pascal))

        add_msg = queue_client.add_create_user_job(user_snake_case)

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
            'schema': UserResponseSchema
        }
    }
})
@users_api.route('users', methods=['GET'])
def get_user():
    if request.method == 'GET':
        is_snake_case = request.args.get("isSnakeCase")

        user = UserDto(user_name=DefaultConfig.DEFAULT_USERNAME)
        users = [user]

        if parse_as_bool(is_snake_case):
            return jsonify(users), 200

        serialized = ToPascalJson.serialize(users)
        return jsonify(serialized), 200
