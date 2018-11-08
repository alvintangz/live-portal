from django.http import HttpResponse
from django.shortcuts import redirect
from .models import User

def index(request):
	#if not request.user.is_authenticated():
	#	return redirect("delegate-sign-in")
	#return redirect("index")
	return HttpResponse(request, "Go to dashboard")

def delegate_sign_in(request):
    return HttpResponse("delegate sign in here")

def partner_sign_in(request):
    return HttpResponse("partner sign in here")