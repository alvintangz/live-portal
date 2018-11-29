from django.contrib.auth.decorators import login_required
from users.decorators import delegate_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views as auth_views
from users.functions import viewByUser
from .profile import delegateProfileView
from .team import DelegateTeamView
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
# from users.forms.accountcreation import DelegateCreateForm

def loginView(request):
	"""A view for logging in."""
	return auth_views.LoginView.as_view(template_name='users/sign_in.html')(request)

def logoutView(request):
	"""A view for logging out."""
	return auth_views.LogoutView.as_view(template_name='users/sign_out.html')(request)

def passwordForgottenView(request):
	"""A view for forgetting passwords."""
	return auth_views.PasswordResetView.as_view(
		template_name='users/password/recover.html',
		subject_template_name = 'users/password/reset_email_subject.txt',
		email_template_name = 'users/password/reset_email_body.html',
		success_url = reverse_lazy('forgot-password-done'))(request)

def passwordForgottenDoneView(request):
	"""A view for forgetting passwords."""
	return auth_views.PasswordResetDoneView.as_view(
		template_name='users/password/done.html')(request)

def passwordForgottenConfirmView(request, *args, **kwargs):
	"""A view for forgetting passwords."""
	return auth_views.PasswordResetConfirmView.as_view(
		template_name='users/password/reset.html',
		success_url = reverse_lazy('forgot-password-complete'))(request, *args, **kwargs)

def passwordForgottenCompleteView(request):
	"""A view for forgetting passwords."""
	return auth_views.PasswordResetCompleteView.as_view(
		template_name='users/password/complete.html')(request)

@delegate_required
def teamView(request):
	"""A view for teams."""
	return DelegateTeamView.as_view()(request)

@delegate_required
def profileView(request):
	"""A view for profiles."""
	return delegateProfileView(request)

@delegate_required
def passwordResetView(request):
	"""A view for profiles."""
	form = PasswordChangeForm(user=request.user)
	context = {'form': form}

	if request.method == 'POST':
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('reset-password-success')
		else:
			context["errors"] = True

	return render(request, 'users/password/signed_in_reset.html', context)

@user_passes_test(lambda u: u.is_superuser)
def delegate_create(request):
	pass
	#form = DelegateCreateForm()
	#context = {'form': form}

	#if request.method == 'POST':
	#	form = DelegateCreateForm(request.POST, request.FILES)
	#	if form.is_valid():
	#		form.save()
	#		return redirect('/accounts/creation/success')
	#	else:
	#		context["errors"] = True

	#return render(request, 'users/creation/delegate.html', context)