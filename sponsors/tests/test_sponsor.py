import pytest

from ..serializers import SponsorCreateSerializer


@pytest.mark.django_db
def test_serializer_validation():
    data = {
        "full_name": "sponsor name",
        "phone": "+1231231223",
        "amount": 20000,
        "is_organization": True,
        "organization_name": "organization name",
    }
    serializer = SponsorCreateSerializer(data)
    assert serializer.validate(data)


@pytest.mark.django_db
def test_serializer_phone_validation():
    data = {
        "full_name": "sponsor name",
        "phone": "+1231231223",
        "amount": 20000,
        "is_organization": True,
        "organization_name": "organization name",
    }
    serializer = SponsorCreateSerializer(data)
    assert serializer.validate_phone(data.get("phone"))
