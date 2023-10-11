from django.contrib import admin

from .models import Student, StudentSponsor


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "tuition_fee", "university", "degree")


@admin.register(StudentSponsor)
class StudentSponsorAdmin(admin.ModelAdmin):
    list_display = ("student", "sponsor", "amount", "created_at")
