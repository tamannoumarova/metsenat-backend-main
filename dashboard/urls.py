from django.urls import path

from .views import DashboardAPIView, MonthlyStatAPIView


urlpatterns = [
    path("", DashboardAPIView.as_view(), name="dashboard"),
    path("mounthly-count/", MonthlyStatAPIView.as_view(), name="count"),
]
