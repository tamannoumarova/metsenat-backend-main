from datetime import datetime

from django.db.models import Sum
from django.utils.dates import MONTHS
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from sponsors.models import Sponsor
from students.models import Student, StudentSponsor


class DashboardAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        paid_amount = StudentSponsor.objects.aggregate(paid_amount=Sum("amount")).get("paid_amount") or 0
        requested_amount = Student.objects.aggregate(requested_amount=Sum("tuition_fee")).get("requested_amount") or 0
        amount_tobe_paid = requested_amount - paid_amount
        amount_collected = Sponsor.objects.filter(status="confirmed").aggregate(Sum("amount")).get('amount__sum') or 0
        total_balance = amount_collected - paid_amount

        data = {"amount_collected": amount_collected, "paid_amount": paid_amount, "total_balance": total_balance,
                "requested_amount": requested_amount,
                "amount_tobe_paid": amount_tobe_paid, }
        return Response(data)


class MonthlyStatAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        year = datetime.now().year
        result = {"sponsors": [], "students": []}

        for index, month in MONTHS.items():
            students = Student.objects.filter(created_at__year=year, created_at__month=index).count()
            sponsors = Sponsor.objects.filter(created_at__year=year, created_at__month=index).count()
            result.get("students").append({str(month): students if students > 0 else 0})
            result.get("sponsors").append({str(month): sponsors if students > 0 else 0})

        return Response(result)
