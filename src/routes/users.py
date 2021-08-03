from http import HTTPStatus

from flask import Blueprint, jsonify
from flask import request
from apifairy import body, response, other_responses, arguments
import marshmallow as ma

from src.config import DefaultConfig
from src.requests.user import CreateUserRequestSchema, CreateUserRequest, GetUserRequest, GetUserRequestSchema
from src.responses.user import UserResponse, UserResponseSchema
from src.dtos.user import UserDto
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
@arguments(GetUserRequestSchema())
def get_all_users(get_user_request: GetUserRequest, id: int):
    if request.method == 'GET':

        user = UserDto(user_name=DefaultConfig.DEFAULT_USERNAME)

        if get_user_request.isSnakeCase:
            return jsonify(user), 200

        serialized = ToPascalJson.serialize(user)
        return jsonify(serialized), 200
