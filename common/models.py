from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class University(TimestampModel):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name
