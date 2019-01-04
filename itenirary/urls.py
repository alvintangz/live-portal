# django modules
from django.urls import path, include
from django.views.generic.base import RedirectView
# views
from .views import (
	DayListView,
	DayDetailView,
	EventDetailView,
)

urlpatterns = [
	path('', RedirectView.as_view(url='days'), name="itenirary"),
	path('days', DayListView.as_view(), name='day-listed'),
	path('day/<number>', DayDetailView.as_view(), name='day-detail'),
	path('event/<int:pk>-<encoded>',
		EventDetailView.as_view(),
		name='event-detail'
	),
]