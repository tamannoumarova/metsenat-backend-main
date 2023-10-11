import pytest
from model_bakery import baker

from sponsors.models import Sponsor
from students.models import Student


@pytest.fixture
def new_student():
    university = baker.make("common.University")
    return Student.objects.create(
        full_name="kimdur", degree="master", tuition_fee=45367, phone=9273827, university=university
    )


@pytest.fixture
def new_sponsor():
    return Sponsor.objects.create(
        full_name="Test1", phone="72353655", amount=38000, is_organization=True, organization_name=" testOrganization"
    )
