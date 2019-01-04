from django.urls import path, include
from django.views.generic.base import RedirectView
from .views.listed import ListedRoundsView, TeamsListedView
from .views.upload import UploadRoundsView
from .views.judge import AssessmentUpdateView

urlpatterns = [
	path('', RedirectView.as_view(url='listed'), name='rounds-index'),
	# LISTED ROUNDS
	path('listed',
		ListedRoundsView.as_view(),
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
		TeamsListedView.as_view(),
		name='rounds-judge-listed'),
	# SUCCESS JUDGING -> LISTED TEAMS
	path('<str:encoded>/judge/teams/listed/success',
		TeamsListedView.as_view(),
		name='rounds-judge-listed-success'),
	# JUDGE
	path('judge/<pk>',
		AssessmentUpdateView.as_view(),
		name='rounds-judge'),
]