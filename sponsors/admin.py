from django.contrib import admin

from sponsors.models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "amount", "status", "created_at")
