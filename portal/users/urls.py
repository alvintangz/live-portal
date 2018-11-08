from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='accounts-index'),
	path('delegate', views.delegate_sign_in, name='delegate-sign-in'),
	path('partner', views.partner_sign_in, name='partner-sign-in'),
]