from src.services.custom_serializer import JSONSerializer
from src.dtos.user import User
from assertpy import assert_that


def test_serializes_to_pascal_case():
    # arrange
    snake_json = {"user_name": "Test User"}
    pascal_json = {"UserName": "Test User"}
    user = JSONSerializer.deserialize(User, snake_json)

    # act
    actual = JSONSerializer.serialize(user)

    assert_that(actual).is_equal_to(pascal_json)


def test_deserializes_snake_to_snake():
    # arrange
    snake_json = {"user_name": "Test User"}

    # act
    actual = JSONSerializer.deserialize(User, snake_json)

    assert_that(actual.user_name).is_equal_to('Test User')
