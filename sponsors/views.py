from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser

from paginations import CustomPageNumberPagination
from sponsors.filters import SponsorFilter
from sponsors.serializers import (
    SponsorCreateSerializer,
    SponsorListSerializer,
    SponsorRetrieveUpdateDestroySerializer,
)
from students.models import Sponsor


class SponsorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Sponsor.objects.order_by("-created_at")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = SponsorFilter
    parser_classes = (FormParser, MultiPartParser)
    ordering_fields = ("id", "full_name", "created_at")
    search_fields = ("full_name", "created_at", "phone", "organization_name")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SponsorCreateSerializer
        return SponsorListSerializer


class SponsorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Sponsor.objects.all()
    serializer_class = SponsorRetrieveUpdateDestroySerializer


class SponsorListForSelect(APIView):
    queryset = Sponsor.objects.order_by("-full_name")
    result = Sponsor.amount
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SponsorCreateSerializer
        return SponsorListSerializer
