from assertpy import assert_that
import pytest

import app


@pytest.fixture
def client():
    client = app.create_app().test_client()
    return client


def test_gets_hello_world(client):
    # arrange
    expected = {"message": "Hello World!"}

    # act
    response = client.get('/api/')

    # assert
    assert_that(response.get_json()).is_equal_to(expected)

