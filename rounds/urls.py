from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import (
	RoundsListView,
	AssessmentsListView,
	UploadRoundsView,
	AssessmentUpdateView,
	TeamSubmissionsDetailView,
	VideoDetailView,
)

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
	# VIEW ROUND SUBMISSIONS FOR PARTNERS
	path('submissions/<int:slug>',
		TeamSubmissionsDetailView.as_view(),
		name='rounds-submissions'),
	# VIDEOS
	path('video/<slug>', VideoDetailView.as_view(), 
		name='rounds-videos'),
]