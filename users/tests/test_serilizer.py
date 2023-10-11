import pytest

from ..serializers import UserLoginSerializer


@pytest.mark.django_db
def test_user_login_serializer_invalid_password(new_user, password):
    data = {"username": f"{new_user}", "password": f"{password}"}
    serializer = UserLoginSerializer(data=data)
    assert not serializer.is_valid()
    assert "Invalid password." in str(serializer.errors)


@pytest.mark.django_db
def test_user_login_serializer_user_not_found():
    data = {"username": "unknownuser", "password": "correctpassword"}
    serializer = UserLoginSerializer(data=data)
    assert not serializer.is_valid()
    assert "User not found." in str(serializer.errors)


@pytest.mark.django_db
def test_user_login_serializer_missing_fields(new_user, password):
    data = {"username": f"{new_user}", "password": f"f{password}"}
    serializer = UserLoginSerializer(data=data)
    assert not serializer.is_valid()
    assert "invalid" in str(serializer.errors)
    assert "invalid" in str(serializer.errors)
