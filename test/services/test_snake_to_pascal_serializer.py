from flask import jsonify

from src.services.snake_to_pascal_serializer import JSONSerializer
from src.dtos.user import UserDto
from assertpy import assert_that


def test_should_serializes_to_pascal_case():
    # arrange
    snake_json = {"user_name": "Test User"}
    pascal_json = {"UserName": "Test User"}
    user = JSONSerializer.deserialize(UserDto, snake_json)

    # act
    actual = JSONSerializer.serialize(user)

    assert_that(actual).is_equal_to(pascal_json)


def test_should_deserializes_snake_to_snake():
    # arrange
    snake_json = {"user_name": "Test User"}

    # act
    actual = JSONSerializer.deserialize(UserDto, snake_json)

    assert_that(actual.user_name).is_equal_to('Test User')


def test_should_serialize_list():
    # arrange
    pascal_json = {"UserName": "Test User"}
    pascal_users = [pascal_json]

    snake_json = {"user_name": "Test User"}
    user = JSONSerializer.deserialize(UserDto, snake_json)
    snake_users = [user]

    # act
    actual = JSONSerializer.serialize(snake_users)

    # assert
    assert_that(str(actual)).is_equal_to(str(pascal_users))


def test_should_deserialize_list():
    # arrange
    pascal_json = {"UserName": "Test User"}
    expected_users = [pascal_json]

    snake_json = {"user_name": "Test User"}
    user = JSONSerializer.deserialize(UserDto, snake_json)
    users = [user]

    # act
    actual = JSONSerializer.serialize(users)

    # assert
    assert_that(str(actual)).is_equal_to(str(expected_users))
