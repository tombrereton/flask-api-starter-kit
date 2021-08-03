from http import HTTPStatus

from apifairy import body, other_responses, response
from flask import Blueprint, jsonify
from flask import request

from src.config import DefaultConfig
from src.dtos.user import UserDto
from src.requests.user import CreateUserRequestSchema, CreateUserRequest
from src.responses.user import UserResponseSchema
from src.services import queue_client
from src.services.pascal_to_snake_serializer import JSONSerializer as ToSnakeJson
from src.services.snake_to_pascal_serializer import JSONSerializer as ToPascalJson

users_api = Blueprint('users', __name__)


@users_api.route('users', methods=['POST'])
@other_responses({
    200: 'User Created',
    400: 'Request Body is Invalid'
})
@body(CreateUserRequestSchema())
def post(user_request: CreateUserRequest):
    """Create a User."""
    if request.method == 'POST':
        user_snake_case = ToSnakeJson.deserialize(UserDto, ToSnakeJson.serialize(user_request))
        add_msg = queue_client.add_create_user_job(user_snake_case)

        return jsonify(add_msg), 200


@users_api.route('users/<int:id>', methods=['GET'])
@response(UserResponseSchema, HTTPStatus.OK.value, "Get Users")
def get_all_users(id: int):
    if request.method == 'GET':

        user = UserDto(user_name=DefaultConfig.DEFAULT_USERNAME)

        serialized = ToPascalJson.serialize(user)
        return serialized, 200
