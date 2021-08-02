from unittest import mock

from assertpy import assert_that
import pytest

import app
from api.dtos.user import User


@pytest.fixture
def client():
    client = app.create_app().test_client()
    return client


def test_validates_input(client):
    # arrange
    user = {"userName": "test_user"}
    expected_msg = 'UserName\': [\'Missing data for required field'

    # act
    response = client.post('/api/users', json=user)

    # assert
    response_as_string = str(response.get_json())
    assert_that(response_as_string).contains(expected_msg)


def test_adds_create_user_job_to_queue(client):
    # arrange
    user = {"UserName": "test_user"}
    user_dto = User(user_name="test_user")

    # act
    with mock.patch('api.services.queue_client.add_create_user_job') as mocked_method:
        response = client.post('/api/users', json=user)

        # assert
        mocked_method.assert_called_once_with(user_dto)
