import pytest
from django.urls import reverse
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
class TestProfile:
    def test_profile_get(self, new_user):
        client.force_authenticate(new_user)
        url = reverse("user-profile")
        response = client.get(url)
        assert response.status_code == 200

    def test_profile_put(self, new_user):
        client.force_authenticate(new_user)
        url = reverse("user-profile")
        response = client.put(url)
        assert response.status_code == 200
