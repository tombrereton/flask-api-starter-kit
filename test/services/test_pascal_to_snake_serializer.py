from flask import jsonify

from src.services.pascal_to_snake_serializer import JSONSerializer as ToSnakeSerializer
from src.requests.user import CreateUserRequest
from assertpy import assert_that


def test_should_serialize_to_pascal():
    # arrange
    snake_json = {"user_name": "Test User"}
    pascal_json = {"UserName": "Test User"}
    user = ToSnakeSerializer.deserialize(CreateUserRequest, pascal_json)

    # act
    actual = ToSnakeSerializer.serialize(user)

    assert_that(actual).is_equal_to(snake_json)


def test_should_deserialize_pascal_to_pascal():
    # arrange
    pascal_json = {"UserName": "Test User"}

    # act
    actual = ToSnakeSerializer.deserialize(CreateUserRequest, pascal_json)

    assert_that(actual.UserName).is_equal_to('Test User')


def test_should_serialize_list():
    # arrange
    snake_json = {"user_name": "Test User"}
    snake_users = [snake_json]

    pascal_json = {"UserName": "Test User"}
    user = ToSnakeSerializer.deserialize(CreateUserRequest, pascal_json)
    pascal_users = [user]

    # act
    actual = ToSnakeSerializer.serialize(pascal_users)

    # assert
    assert_that(str(actual)).is_equal_to(str(snake_users))
