# django modules
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import (
	LoginView,
	LogoutView,
	PasswordResetView,
	PasswordResetDoneView,
	PasswordResetConfirmView,
	PasswordResetCompleteView,
)
# views
from .views.all import (
	profileView,
	teamView,
	passwordResetView,
)
from .views.activate import (
	activateInformationView,
	activateConfirmView,
)

urlpatterns = [
	# SIGN IN
	path('sign-in',
		LoginView.as_view(template_name='users/sign_in.html'),
		name='sign-in'),
	path('sign-in/confirmed',
		LoginView.as_view(template_name='users/sign_in.html'),
		name='sign-in-confirmed'),
	# SIGN OUT
	path('sign-out',
		LogoutView.as_view(template_name='users/sign_out.html'),
		name='sign-out'),
	# PROFILE VIEWING
	path('profile', profileView, name='profile'),
	path('profile/success', profileView, name='profile-success'),
	path('profile/confirmed', profileView, name='profile-confirmed'),
	path('team', teamView, name='team'),
	# PASSWORD RESET
	path('password/reset', passwordResetView, name='reset-password'),
	path('password/reset/success', passwordResetView,
		name='reset-password-success'),
	# RECOVER PASSWORD
	path('recover',
		PasswordResetView.as_view(
			template_name='users/password/recover.html',
			subject_template_name = 'users/password/reset_email_subject.txt',
			email_template_name = 'users/password/reset_email_body.html',
			success_url = reverse_lazy('forgot-password-done')),
		name='forgot-password'),
	path('recover/done',
		PasswordResetDoneView.as_view(template_name='users/password/done.html'),
		name='forgot-password-done'),
	path('recover/reset/<uidb64>/<token>',
		PasswordResetConfirmView.as_view(
			template_name='users/password/reset.html',
			success_url = reverse_lazy('forgot-password-complete')),
		name='forgot-password-confirm'),
	path('recover/success',
		PasswordResetCompleteView.as_view(
			template_name='users/password/complete.html'),
		name='forgot-password-complete'),
	# CONFIRM
	path('activate/confirm/<str:encoded>',
		activateConfirmView,
		name="activate-confirm"),
	path('activate/<str:encoded>',
		activateInformationView,
		name="activate-information"),
]