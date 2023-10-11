from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from common.models import University
from common.serializers import UniversitySerializer
from paginations import CustomPageNumberPagination


class UniversityListView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = University.objects.order_by("name")
    serializer_class = UniversitySerializer
    pagination_class = CustomPageNumberPagination
