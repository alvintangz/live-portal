from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User

def index(request):
	#if not request.user.is_authenticated():
	#	return redirect('/accounts/')
	#return HttpResponse(request, "Go to dashboard")
	return HttpResponse(request, "Go to dashboard")

def credits(request):
	return render(request, 'credits.html')

# EDIT
def terms_of_service(request):
	return render(request, 'terms_of_service.html')

# EDIT
def privacy_policy(request):
	return render(request, 'privacy_policy.html')

# EDIT
#def error_404(request):
#	return render(request, '404.html')

urlpatterns = [
	path('', include('users.urls')),
	path('', include('notifications.urls')),
    path('admin/', admin.site.urls),
	path('credits', credits, name='credits'),
	path('tos', terms_of_service, name='terms_of_service'),
	path('privacy', privacy_policy, name='privacy_policy'),
]