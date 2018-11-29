from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import (
	AllAnswersListView,
	FAQAnswersListView,
	AskView
)

urlpatterns = [
	path('', RedirectView.as_view(pattern_name='qanda-answers-all'), name='qanda'),
	path('answers/all', AllAnswersListView.as_view(), name='qanda-answers-all'),
	path('answers/faq', FAQAnswersListView.as_view(), name='qanda-answers-faq'),
	path('ask', AskView.as_view(), name='qanda-ask'),
	path('ask/success', AskView.as_view(), name='qanda-ask-success'),
]