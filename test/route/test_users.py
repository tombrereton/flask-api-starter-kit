from assertpy import assert_that
import pytest

import app


@pytest.fixture
def client():
    client = app.create_app().test_client()
    return client


def test_validates_input(client):
    # arrange
    user = {"userName": "test_user"}
    expected_msg = 'UserName\': [\'Missing data for required field'
    expected_msg_2 = 'UserName'

    # act
    response = client.post('/api/users', json=user)

    # assert
    response_as_string = str(response.get_json())
    assert_that(response_as_string).contains(expected_msg)


def test_creates_user_with_camelcase(client):
    # arrange
    user = {"UserName": "test_user"}

    # act
    response = client.post('/api/users', json=user)

    # assert
    assert_that(response.get_json()).is_equal_to(user)
