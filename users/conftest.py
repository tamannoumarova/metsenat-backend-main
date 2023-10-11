import pytest
from model_bakery import baker


@pytest.fixture
def password():
    return "p@s$word"


@pytest.fixture
def new_user():
    return baker.make("users.User")
