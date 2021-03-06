from http import HTTPStatus
from unittest import mock
from unittest.mock import call

from assertpy import assert_that
import pytest

from src import app
from src.dtos.user import UserDto
from src.services.snake_to_pascal_serializer import JSONSerializer as PascalJson


@pytest.fixture
def client():
    client = app.create_app().test_client()
    return client


def test_should_validate_input(client):
    # arrange
    user = {"userName": "test_user"}
    expected_msg = 'UserName\': [\'Missing data for required field'

    # act
    response = client.post('/api/users', json=user)

    # assert
    response_as_string = str(response.get_json())
    assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST.value)
    assert_that(response_as_string).contains(expected_msg)


def test_should_add_create_user_job_to_queue(client):
    # arrange
    user = {"UserName": "test_user"}
    user_dto = UserDto(user_name="test_user")

    # act
    with mock.patch('src.services.queue_client.add_create_user_job') as mocked_method:
        attrs = {'return_value': 'mocked response'}
        mocked_method.configure_mock(**attrs)
        response = client.post('/api/users', json=user)

        # assert
        mocked_method.assert_called_once_with(user_dto)


def test_should_add_many_create_user_jobs(client):
    # arrange
    user = {"UserName": "test_user"}
    user_2 = {"UserName": "test_user_2"}
    create_users = {"Users": [user, user_2]}

    user_dto = UserDto(user_name=user["UserName"])
    user_dto_2 = UserDto(user_name=user_2["UserName"])
    calls = [call(user_dto), call(user_dto_2)]

    # act
    with mock.patch('src.services.queue_client.add_create_user_job') as mocked_method:
        attrs = {'return_value': 'mocked response'}
        mocked_method.configure_mock(**attrs)
        response = client.post('/api/users/many', json=create_users)

        # assert
        mocked_method.assert_has_calls(calls)


def test_should_get_user_added_response(client):
    # arrange
    user = {"UserName": "Test User"}

    # act

    response = client.post('/api/users', json=user)

    # assert
    response_as_string = str(response.get_json())
    assert_that(response_as_string).contains(user["UserName"])


def test_should_get_users_as_pascal_case(client):
    # act
    response = client.get('/api/users/1')

    # assert
    assert_that(response.get_json()).is_length(1)
    assert_that(next(iter(response.get_json()))).contains('UserName')
