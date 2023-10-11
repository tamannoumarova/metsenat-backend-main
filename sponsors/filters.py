from django_filters import rest_framework as filters

from sponsors.models import Sponsor


class SponsorFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Sponsor
        fields = ("status", "amount", "start_date", "end_date")
