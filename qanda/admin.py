from django.contrib import admin
from django import forms
from .models import (
	Question,
	Answer
)
from tinymce.widgets import TinyMCE

class AnswerForm(forms.ModelForm):
	answer = forms.CharField(widget=TinyMCE(attrs={'cols':100, 'rows':10}))

	class Meta:
		model = Answer
		exclude = ()

class AnswerInline(admin.StackedInline):
	model = Answer
	form = AnswerForm

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('shorten_question', 'by_name', 'formatted_created')
	inlines = (AnswerInline,)