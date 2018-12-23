# django modules
from django.urls import path, include
# views
from .views.all import (
	loginView,
	logoutView,
	profileView,
	teamView,
	passwordResetView,
	passwordForgottenView,
	passwordForgottenDoneView,
	passwordForgottenConfirmView,
	passwordForgottenCompleteView,
)
from .views.activate import (
	activateInformationView,
	activateConfirmView,
)

urlpatterns = [
	path('sign-in', loginView, name='sign-in'),
	path('sign-in/confirmed', loginView, name='sign-in-confirmed'),
	path('sign-out', logoutView, name='sign-out'),
	path('profile', profileView, name='profile'),
	path('profile/success', profileView, name='profile-success'),
	path('profile/confirmed', profileView, name='profile-confirmed'),
	path('team', teamView, name='team'),
	# PASSWORD RESET
	path('password/reset', passwordResetView, name='reset-password'),
	path('password/reset/success', passwordResetView,
		name='reset-password-success'),
	# RECOVER PASSWORD
	path('recover', passwordForgottenView, name='forgot-password'),
	path('recover/done', passwordForgottenDoneView,
		name='forgot-password-done'),
	path('recover/reset/<uidb64>/<token>', passwordForgottenConfirmView,
		name='forgot-password-confirm'),
	path('recover/success', passwordForgottenCompleteView,
		name='forgot-password-complete'),
	# CONFIRM
	path('activate/confirm/<str:encoded>',
		activateConfirmView,
		name="activate-confirm"),
	path('activate/<str:encoded>',
		activateInformationView,
		name="activate-information"),
]