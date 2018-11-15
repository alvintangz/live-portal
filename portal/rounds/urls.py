from django.urls import path, include
from .views import roundsListedView, roundsUploadView

urlpatterns = [
	path('rounds', roundsListedView, name='rounds'),
	path('round/<int:pk>', roundsSpecificView, name='rounds-upload')
]