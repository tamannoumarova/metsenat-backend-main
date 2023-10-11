import pytest
from model_bakery import baker


@pytest.mark.django_db
def test_users_str():
    username = "example_name"
    user = baker.make("users.User", username=username)
    assert user.__str__() == username
