# django modules
from django.contrib import admin
# models
from .models import (
	CorporateOrganization,
	CorporateIndividual,
)

@admin.register(CorporateOrganization)
class CorporateOrganizationAdmin(admin.ModelAdmin):
	list_display = ('name', 'partner')
	ordering = ['partner', 'name']

@admin.register(CorporateIndividual)
class CorporateIndividualAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'organization', 'type_of', 'order')
	list_filter = ('organization', 'type_of')