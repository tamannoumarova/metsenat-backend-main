import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sponsors.models import Sponsor


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", "spend_money", "created_at", "status")


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", "payment_type", "is_organization", "organization_name")

    def validate(self, attrs):
        if attrs.get("is_organization") and not attrs.get("organization_name"):
            raise ValidationError(detail="Organization name must be set.")
        return attrs

    def validate_phone(self, phone: str):  # noqa
        regex = "\\+?[1-9][0-9]{7,14}$"
        if re.search(regex, phone) and phone.startswith("+"):
            return phone
        raise ValidationError(
            detail='Phone number must be entered in the format:  " "+998 99 999 99 99 .Up to 15 digits allowed.'
        )


class SponsorRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            "id",
            "full_name",
            "phone",
            "payment_type",
            "amount",
            "is_organization",
            "status",
            "created_at",
            "organization_name",
        )
        read_only = "id"
