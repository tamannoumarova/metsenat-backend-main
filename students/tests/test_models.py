import pytest
from model_bakery import baker

from common.models import University
from students.models import Student


@pytest.fixture
def student():
    return Student.objects.create(
        full_name="John Doe",
        degree="bachelors",
        tuition_fee=1000000,
        phone="+9998822334455",
        university=University.objects.create(name="John Doe University"),
    )


@pytest.mark.django_db
def test_student_str():
    full_name = "Test students"
    student = baker.make("students.Student", full_name=full_name)
    assert str(student) == full_name


@pytest.mark.django_db
def test_student_total_sponsor_amount_is_none(student):
    assert student.total_sponsor_amount == 0
