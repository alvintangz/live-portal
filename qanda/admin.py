from django.contrib import admin
from .models import (
	Question,
	Answer
)

class AnswerInline(admin.StackedInline):
	model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('shorten_question', 'by_name', 'formatted_created')
	inlines = (AnswerInline,)