from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from contacts import views
from django.conf.urls.static import static

# EDIT
#def error_404(request):
#	return render(request, '404.html')

urlpatterns = [
	path('', include('users.urls')),
	path('', include('notifications.urls')),
	path('', include('rounds.urls')),
	path('live-team', views.contactUsView, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
	path('credits', TemplateView.as_view(template_name="credits.html"), name='credits'),
	path('tos', TemplateView.as_view(template_name="terms_of_service.html"), name='terms_of_service'),
	path('privacy', TemplateView.as_view(template_name="privacy_policy.html"), name='privacy_policy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)