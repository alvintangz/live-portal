from django.contrib import admin
from .models import CorporateOrganization, Mentor, Judge, Speaker, Networker

@admin.register(CorporateOrganization)
class CorporateOrganizationAdmin(admin.ModelAdmin):
	list_display = ('name', 'partner')
	ordering = ['partner']

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'organization')
	ordering = ['full_name']

@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'organization')
	ordering = ['full_name']

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'organization')
	ordering = ['full_name']

@admin.register(Networker)
class NetworkerAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'organization')
	ordering = ['full_name']