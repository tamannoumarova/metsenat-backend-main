import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
class TestUser:
    def test_user_login(self, client):
        user = User.objects.create(username="test_user")
        user.set_password("test_password")
        user.save()
        data = {
            "username": user.username,
            "password": "test_password",
        }

        url = reverse("user-login")
        response = client.post(url, data=data)

        assert response.status_code == 200
