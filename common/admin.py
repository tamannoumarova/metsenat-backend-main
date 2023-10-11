from django.contrib import admin

from .models import University


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ["name", "phone"]
    search_fields = ["name"]
