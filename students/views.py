from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from paginations import CustomPageNumberPagination
from students.serializers import (
    AddSponsorToStudentsSerializer,
    StudentDetailSerializer,
    StudentListCreateSerializer,
    StudentSerializer,
    StudentSponsor,
)

from .models import Student


class StudentsListView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StudentListCreateSerializer
        return StudentListCreateSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return StudentDetailSerializer
        return StudentDetailSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.order_by("-id")
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("degree", "university")
    ordering_fields = ("id", "full_name")
    search_fields = ("full_name", "university__name")
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAdminUser]


class StudentDetailViews(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    permission_classes = [permissions.IsAdminUser]


class AddSponsorToStudentsAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = StudentSponsor.objects.all()
    serializer_class = AddSponsorToStudentsSerializer

    def perform_create(self, serializer):
        serializer.save(student_id=self.kwargs["pk"])
