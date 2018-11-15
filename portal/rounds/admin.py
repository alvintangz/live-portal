from django.contrib import admin
from .models import Round, AcceptedRoundFile, Submission

# ROUNDS

@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
	list_display = ('number', 'title', 'active', 'visible', 'expected_deadline')

# ACCEPTED ROUND FILE

@admin.register(AcceptedRoundFile)
class AcceptedRoundFileAdmin(admin.ModelAdmin):
	list_display = ('title', 'get_asc_round_number')

	def get_asc_round_number(self, x):
		return x.asc_round.number

# SUBMISSIONS

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
	list_display = ('get_asc_round_number', 'get_asc_team_number', 'latest')

	def get_asc_round_number(self, x):
		return x.asc_round.number

	def get_asc_team_number(self, x):
		return x.asc_team.number