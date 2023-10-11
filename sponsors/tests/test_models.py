import pytest
from model_bakery import baker

from sponsors.models import Sponsor
from students.models import Student, StudentSponsor

@pytest.mark.django_db
def test_sponsor_full_name():
    full_name = "Test Sponsor"
    sponsor = baker.make(Sponsor, full_name=full_name)
    assert str(sponsor) == full_name


@pytest.mark.django_db
def test_sponsor_default_status():
    sponsor = baker.make(Sponsor)
    assert sponsor.status == Sponsor.StatusChoices.NEW


@pytest.mark.django_db
def test_sponsor_custom_status():
    sponsor = baker.make(Sponsor, status=Sponsor.StatusChoices.CONFIRMED)
    assert sponsor.status == Sponsor.StatusChoices.CONFIRMED


@pytest.mark.django_db
def test_sponsor_created_at_auto_now_add():
    sponsor = baker.make(Sponsor)
    assert sponsor.created_at is not None


@pytest.mark.django_db
def test_sponsor_organization_name_optional():
    sponsor = baker.make(Sponsor, is_organization=False, organization_name=None)
    assert sponsor.organization_name is None


@pytest.mark.django_db
def test_sponsor_spend_money():
    sponsor = baker.make(Sponsor)
    student1 = baker.make(Student)
    student2 = baker.make(Student)
    student_sponsor1 = baker.make(StudentSponsor, student=student1, sponsor=sponsor, amount=50)
    student_sponsor2 = baker.make(StudentSponsor, student=student2, sponsor=sponsor, amount=200)
    expected_spent_money = student_sponsor1.amount + student_sponsor2.amount
    assert sponsor.spend_money == expected_spent_money
