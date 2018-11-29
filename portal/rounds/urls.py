from django.urls import path, include
from .views.all import roundsListedView, roundsUploadView

urlpatterns = [
	path('listed', roundsListedView, name='rounds'),
	path('upload/<str:encoded>', roundsUploadView, name='rounds-upload'),
	path('upload/<str:encoded>/success', roundsUploadView, name='rounds-upload-success'),
]