from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TeamView, profileView

urlpatterns = [
	path('sign-in', auth_views.LoginView.as_view(template_name='users/sign_in.html'), name='sign-in'),
	path('sign-out', auth_views.LogoutView.as_view(template_name='users/sign_out.html'), name='sign-out'),
	path('profile', profileView, name='profile'),
	path('team', TeamView.as_view(template_name='users/delegate/team.html'), name='team'),
	#RE-EDIT
	path('reset', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='forgot-password'),
]