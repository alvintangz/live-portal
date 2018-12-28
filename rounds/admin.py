from django.contrib import admin
from rounds.models.rounds import Round, AcceptedRoundFile
from rounds.models.submissions import Submission

# ROUNDS

@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'number',
		'active',
		'visible',
		'expected_deadline'
	)

# ACCEPTED ROUND FILE

@admin.register(AcceptedRoundFile)
class AcceptedRoundFileAdmin(admin.ModelAdmin):
	list_display = ('title', 'asc_round')

# SUBMISSIONS

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