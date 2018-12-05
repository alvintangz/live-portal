from django.contrib import admin
from .models import (
	Question,
	Answer
)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('shorten_question', 'by_name', 'formatted_created')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display = ('asc_question', 'shorten_answer', 'faq', 'formatted_updated')