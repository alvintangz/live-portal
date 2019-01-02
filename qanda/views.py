# django modules
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# models
from .models import Question, Answer
# helpers
from users.auth.mixins import DelegateRequiredMixin

class AllAnswersListView(DelegateRequiredMixin, ListView):
	model = Answer
	template_name = "qanda/answers.html"
	context_object_name = "answers"
	paginate_by = 10

class FAQAnswersListView(DelegateRequiredMixin, ListView):
	model = Answer
	template_name = "qanda/answers.html"
	context_object_name = "answers"
	paginate_by = 10

	def get_queryset(self):
		return Answer.objects.is_faq()

class AskView(DelegateRequiredMixin, CreateView):
	template_name = "qanda/ask.html"
	success_url = reverse_lazy('qanda-ask-success')
	model = Question
	fields = ['question', 'by_anonymous']

	def form_valid(self, form):
		form.instance.by = self.request.user
		return super(AskView, self).form_valid(form)