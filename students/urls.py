from django.urls import path

from students.views import (
    AddSponsorToStudentsAPIView,
    StudentDetailView,
    StudentListCreateView,
)


app_name = "students"

urlpatterns = [
    path("", StudentListCreateView.as_view(), name="student_list_create"),
    path("<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("<int:pk>/sponsors/", AddSponsorToStudentsAPIView.as_view(), name="add_sponsor"),
]
