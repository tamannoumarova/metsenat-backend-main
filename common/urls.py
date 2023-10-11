from django.urls import path

from common.views import UniversityListView


app_name = "common"

urlpatterns = [path("universities/", UniversityListView.as_view(), name="university_list")]
