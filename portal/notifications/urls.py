from django.urls import path
from . import views

urlpatterns = [
	# Main page
	path('', views.mainView, name='index')
]