from assertpy import assert_that

from api.schema.user_schema import UserSchema, to_snake_case


def test_should_convert_pascal_to_snake_case():
    # arrange
    pascal_case = "UserName"
    expected = "user_name"

    # act
    actual = to_snake_case(pascal_case)

    assert_that(actual).is_equal_to(expected)


def test_should_convert_pascal_to_snake_case_with_schema():
    # arrange
    user = {"UserName": "Test User"}
    expected = {"user_name": "Test User"}
    user_schema = UserSchema()

    # act
    actual = user_schema.load(user)
    converted = user_schema.dump(actual)

    # assert
    assert_that(converted).is_equal_to(expected)


def test_should_get_pascal_case_from_schema():
    # arrange
    user = {"UserName": "Test User"}
    user_schema = UserSchema()

    # act
    actual = user_schema.load(user)

    # assert
    assert_that(actual).is_equal_to(user)
