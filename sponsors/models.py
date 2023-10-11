from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _


class Sponsor(models.Model):
    class PaymentType(models.TextChoices):
        cash = (
            "cash",
            _("Cash"),
        )
        card = (
            "card",
            _("Card"),
        )
        transfer = (
            "transfer",
            _("Transfer"),
        )

    class StatusChoices(models.TextChoices):
        NEW = "new", _("New")
        IN_PROCESS = "in_process", _("In process")
        CONFIRMED = "confirmed", _("Confirmed")
        CANCELLED = "cancelled", _("Cancelled")

    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    amount = models.PositiveBigIntegerField(default=0)
    payment_type = models.CharField(max_length=8, choices=PaymentType.choices)
    is_organization = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=StatusChoices.choices, default=StatusChoices.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    organization_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.full_name

    @property
    def spend_money(self):
        return self.students.aggregate(spent_money=Sum("amount")).get("spent_money") or 0
