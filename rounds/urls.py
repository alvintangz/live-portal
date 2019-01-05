from django.urls import path, include
from django.views.generic.base import RedirectView
from .views.listed import RoundsListView, AssessmentsListView
from .views.upload import UploadRoundsView
from .views.judge import AssessmentUpdateView

urlpatterns = [
	path('', RedirectView.as_view(url='listed'), name='rounds-index'),
	# LISTED ROUNDS
	path('listed',
		RoundsListView.as_view(),
		name='rounds'),
	# UPLOAD
	path('upload/<str:encoded>',
		UploadRoundsView.as_view(),
		name='rounds-upload'),
	path('upload/<str:encoded>/success',
		UploadRoundsView.as_view(),
		name='rounds-upload-success'),
	# LISTED TEAMS
	path('<str:encoded>/judge/teams/listed',
		AssessmentsListView.as_view(),
		name='rounds-judge-listed'),
	# SUCCESS JUDGING -> LISTED TEAMS
	path('<str:encoded>/judge/teams/listed/success',
		AssessmentsListView.as_view(),
		name='rounds-judge-listed-success'),
	# JUDGE
	path('assessment/<slug>',
		AssessmentUpdateView.as_view(),
		name='rounds-judge'),
]