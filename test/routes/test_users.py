from unittest import mock

from assertpy import assert_that
import pytest

from src import app
from src.dtos.user import User


@pytest.fixture
def client():
    client = app.create_app().test_client()
    return client


def test_should_validates_input(client):
    # arrange
    user = {"userName": "test_user"}
    expected_msg = 'UserName\': [\'Missing data for required field'

    # act
    response = client.post('/api/users', json=user)

    # assert
    response_as_string = str(response.get_json())
    assert_that(response_as_string).contains(expected_msg)


def test_should_add_create_user_job_to_queue(client):
    # arrange
    user = {"UserName": "test_user"}
    user_dto = User(user_name="test_user")

    # act
    with mock.patch('src.services.queue_client.add_create_user_job') as mocked_method:
        response = client.post('/api/users', json=user)

        # assert
        mocked_method.assert_called_once_with(user_dto)


def test_should_get_user_added_response(client):
    # arrange
    user = {"UserName": "Test User"}

    # act

    response = client.post('/api/users', json=user)

    # assert
    response_as_string = str(response.get_json())
    assert_that(response_as_string).contains(user["UserName"])


def test_should_get_user_as_pascal_case(client):
    # act
    response = client.get('/api/users')

    # assert
    response_as_string = str(response.get_json())
    assert_that(response_as_string).contains('UserName')


def test_should_get_user_as_snake_case(client):
    # act
    response = client.get('/api/users?isSnakeCase=true')

    # assert
    response_as_string = str(response.get_json())
    assert_that(response_as_string).contains('user_name')
