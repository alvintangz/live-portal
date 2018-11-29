from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from contacts import views
from django.conf.urls.static import static
from django.conf.urls import handler403, handler404
from .views import page_not_found, forbidden

# EDIT
#def error_404(request):
#	return render(request, '404.html')

urlpatterns = [
	path('', include('notifications.urls')),
	path('account/', include('users.urls')),
	path('corporate/', include('corporate.urls')),
	path('rounds/', include('rounds.urls')),
	path('questions/', include('qanda.urls')),
	path('live-team', views.contactUsView, name='contact'),
	path('credits', TemplateView.as_view(template_name="credits.html"), name='credits'),
	path('tos', TemplateView.as_view(template_name="terms_of_service.html"), name='terms_of_service'),
	path('privacy', TemplateView.as_view(template_name="privacy_policy.html"), name='privacy_policy'),
	path('executive/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
