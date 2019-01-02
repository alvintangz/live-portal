from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	
	list_display = (
		'position_title',
		'full_name',
		'show_delegates',
		'show_partners',
		'show_judges',
	)

	ordering = ['position_title']