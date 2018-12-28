from django.contrib import admin
from rounds.models.submissions import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
	list_display = (
		'asc_round_file',
		'asc_team', 
		'latest', 
		'get_submitted_by_name',
		'get_view_html',
	)
	ordering = ('-latest','-submitted_at')
	list_filter = ('latest', 'asc_round', 'asc_team')