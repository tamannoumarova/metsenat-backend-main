from rest_framework import serializers

from common.models import University


class UniversitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = University
        fields = (
            "id",
            "name",
        )
