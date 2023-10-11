from rest_framework import serializers

from students.models import Student, StudentSponsor


class StudentListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("full_name", "degree", "tuition_fee", "total_sponsor_amount", "university", "amount")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["university"] = instance.university.name
        return data


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "full_name",
            "phone",
            "degree",
            "tuition_fee",
            "total_sponsor_amount",
            "created_at",
            "university",
        )
        read_only_fields = ("id",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["university"] = instance.university.name
        return data


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = (
            "id",
            "full_name",
            "degree",
            "tuition_fee",
            "total_sponsor_amount",
            "phone",
            "created_at",
            "university",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["university"] = instance.university.name
        return data


class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ("id", "sponsor", "amount")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["sponsor"] = instance.sponsor.full_name
        return data


class StudentDetailSerializers(serializers.ModelSerializer):
    sponsors = StudentSponsorSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ("id", "full_name", "phone", "university", "degree", "total_sponsor_amount", "tuition_fee", "sponsors")
        read_only_fields = ("id",)


class AddSponsorToStudentsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = StudentSponsor
        fields = ("id", "sponsor", "amount")

    def validate(self, attrs):
        sponsor = attrs["sponsor"]
        sponsor_money = sponsor.amount - sponsor.spend_money
        if attrs["amount"] <= sponsor_money:
            return attrs
        raise serializers.ValidationError(detail={"detail": "Amount must be less than sponsor's amount."})
