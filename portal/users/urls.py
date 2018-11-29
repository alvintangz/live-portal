from django.urls import path
from .views.activate import ActivateInformationView, ActivateConfirmView
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
	delegate_create
)

urlpatterns = [
	path('sign-in', loginView, name='sign-in'),
	path('sign-out', logoutView, name='sign-out'),
	path('profile', profileView, name='profile'),
	path('profile/success', profileView, name='profile-success'),
	path('profile/confirmed', profileView, name='profile-confirm-success'),
	path('team', teamView, name='team'),
	path('password/reset', passwordResetView, name='reset-password'),
	path('password/reset/success', passwordResetView,
		name='reset-password-success'),
	path('recover', passwordForgottenView, name='forgot-password'),
	path('recover/done', passwordForgottenDoneView,
		name='forgot-password-done'),
	path('recover/reset/<uidb64>/<token>', passwordForgottenConfirmView,
		name='forgot-password-confirm'),
	path('recover/success', passwordForgottenCompleteView,
		name='forgot-password-complete'),
	path('activate/<str:encoded>', ActivateInformationView.as_view(),
		name="activate-information"),
	path('activate/confirm/<str:encoded>', ActivateConfirmView.as_view(),
		name="activate-confirm"),
	#path('creation', delegate_create, name="admin-ac"),
	#path('creation/success', delegate_create, name="admin-ac-success")
]