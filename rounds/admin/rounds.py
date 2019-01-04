from django.contrib import admin
from rounds.models.rounds import Round, AcceptedRoundFile

class AcceptedRoundFileInline(admin.StackedInline):
	model = AcceptedRoundFile
	extra = 1

@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'number',
		'active',
		'visible',
		'expected_deadline'
	)
	inlines = (AcceptedRoundFileInline,)
	ordering = ('number',)