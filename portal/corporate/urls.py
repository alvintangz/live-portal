from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import (
	PartnersListView,
	MentorsListView,
	JudgesListView,
	SpeakersListView,
	NetworkersListView
)

urlpatterns = [
	# Auto redirect to partners page
	path('', RedirectView.as_view(url='partners'), name='corporate'),
	path('partners', PartnersListView.as_view(), name='partners'),
	path('mentors', MentorsListView.as_view(), name='mentors'),
	path('judges', JudgesListView.as_view(), name='judges'),
	path('speakers', SpeakersListView.as_view(), name='speakers'),
	path('networkers', NetworkersListView.as_view(), name='networkers'),
]