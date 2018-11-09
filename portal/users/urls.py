from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('sign-in', auth_views.LoginView.as_view(template_name='users/sign_in.html'), name='sign-in'),
	#RE-EDIT
	path('reset', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='forgot-password'),
]