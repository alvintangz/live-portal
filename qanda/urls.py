# django modules
from django.urls import path, include
from django.views.generic.base import RedirectView
# views
from .views import (
	AllAnswersListView,
	FAQAnswersListView,
	AskView
)

urlpatterns = [
	# Auto redirect to all answers page
	path('',
		RedirectView.as_view(pattern_name='qanda-ask'),
		name='qanda'),
	path('answers/all', AllAnswersListView.as_view(), name='qanda-answers-all'),
	path('answers/faq', FAQAnswersListView.as_view(), name='qanda-answers-faq'),
	path('ask', AskView.as_view(), name='qanda-ask'),
	path('ask/success', AskView.as_view(), name='qanda-ask-success'),
]