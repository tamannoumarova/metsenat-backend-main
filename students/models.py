from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from sponsors.models import Sponsor


class Student(models.Model):
    class StudentTypes(models.TextChoices):
        BACHELOR = "bachelors", _("Bachelors")
        MASTER = "master", _("Master")

    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50, choices=StudentTypes.choices)
    tuition_fee = models.FloatField(default=0)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    university = models.ForeignKey("common.University", on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.full_name

    @property
    def total_sponsor_amount(self):
        total_amount = self.sponsors.aggregate(total_amount=Sum("amount"))
        return total_amount.get("total_amount") or 0


class StudentSponsor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="sponsors")
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name="students")
    amount = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.sponsor.status != "confirmed":
            raise ValidationError({"amount": "sponsor to'lovi tasdiqlanmagan!"})
        if self.sponsor.amount < self.amount:
            raise ValidationError({"amount": f"sponsorda {self.amount} summa yo'q"})

    def __str__(self):
        return f"{self.sponsor}-> {self.student}"
