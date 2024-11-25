from django.contrib import admin
from .models import Event, Members, Certificate, ApplyClub

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ("member_id", "student_code", "name", "department", "joining_year", "leaving_year", "batch", "email", "blood_group", "position", "facebook_link", "linkedin_link", "image")
    search_fields = ("student_code", "email", "member_id")
    list_filter = ("student_code", "email", "member_id",  "joining_year")



@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'batch', 'year', 'event_title')
    search_fields = ('email', 'user_id')


@admin.register(ApplyClub)
class ClubJoinRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_code', 'department', 'batch',)
    list_filter = ('department', 'batch',)
    search_fields = ('name', 'student_code', 'university_email', "personal_email")