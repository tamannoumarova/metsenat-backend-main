import pytest
from django.urls import reverse

from users.serializers import UserLoginSerializer


@pytest.mark.django_db
def test_login_serializer_validate_with_inactive_user(new_user, password):
    serializer = UserLoginSerializer(data={"username": new_user.username, "password": password})
    new_user.is_active = False
    new_user.save(update_fields=["is_active"])

    assert serializer.is_valid() is False
    assert serializer.errors.get("non_field_errors")[0] == "User account is disabled."


@pytest.mark.django_db
class TestUserRegister:
    def test_user_register(self, client):
        data = {
            "username": "test_user",
            "password": "test_password",
        }

        url = reverse("user-register")
        response = client.post(url, data=data)

        assert response.status_code == 201
