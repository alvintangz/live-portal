# django modules
from django.contrib import admin
# models
from .models import (
	CorporateOrganization,
	CorporateIndividual,
)
from .resources import (
	CorporateOrganizationResource,
	CorporateIndividualResource,
)
# import export
from import_export.admin import ImportExportModelAdmin

@admin.register(CorporateOrganization)
class CorporateOrganizationAdmin(ImportExportModelAdmin):
	resource_class = CorporateOrganizationResource
	list_display = ('name', 'partner')
	ordering = ['-partner', 'name']
	fieldsets = (
		(None, {
            'fields': ('name',)
        }),
		('Entries if partner', {
            'classes': ('collapse',),
            'fields': ('partner',
				'logo',
				'partner_type',
				'description',),
        }),
	)

@admin.register(CorporateIndividual)
class CorporateIndividualAdmin(ImportExportModelAdmin):
	resource_class = CorporateIndividualResource
	list_display = ('full_name', 'organization', 'type_of', 'order')
	list_filter = ('type_of', 'organization')