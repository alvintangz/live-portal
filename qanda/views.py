from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from users.decorators import delegate_required
from .models import Question, Answer
from django.urls import reverse_lazy

@method_decorator(delegate_required, name='dispatch')
class AllAnswersListView(ListView):
	model = Answer
	template_name = "qanda/answers.html"
	context_object_name = "answers"
	paginate_by = 10
	
@method_decorator(delegate_required, name='dispatch')
class FAQAnswersListView(ListView):
	model = Answer
	template_name = "qanda/answers.html"
	context_object_name = "answers"
	paginate_by = 10

	def get_queryset(self):
		return Answer.objects.is_faq()

@method_decorator(delegate_required, name='dispatch')
class AskView(CreateView):
	template_name = "qanda/ask.html"
	success_url = reverse_lazy('qanda-ask-success')
	model = Question
	fields = ['question', 'by_anonymous']

	def form_valid(self, form):
		form.instance.by = self.request.user
		return super(AskView, self).form_valid(form)