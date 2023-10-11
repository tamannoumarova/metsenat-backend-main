from django.urls import path

from sponsors.views import (
    SponsorListCreateView,
    SponsorListForSelect,
    SponsorRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path("", SponsorListCreateView.as_view(), name="sponsor_list_create"),
    path("<int:pk>/", SponsorRetrieveUpdateDestroyAPIView.as_view(), name="sponsor-detail-edit-delete"),
    path("sponsors-for-select/", SponsorListForSelect.as_view(), name="sponsors-list-select"),
]
