import pytest
from model_bakery import baker
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


@pytest.mark.django_db
def test_users_str():
    username = "Testuser"
    user = baker.make("users.User", username=username)
    assert str(user) == username


@pytest.fixture
def my_class_instance():
    return User()


@pytest.mark.django_db
def test_user_refresh_token(my_class_instance):
    assert isinstance(my_class_instance.token, RefreshToken)
