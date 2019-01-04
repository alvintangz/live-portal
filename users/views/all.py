# django modules
from django.contrib.auth.decorators import login_required
from users.auth.decorators import delegate_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# helpers
from users.auth.functions import is_delegate, is_judge, is_partner
# views
from .profile import delegateProfileView
from .team import DelegateTeamView

@delegate_required
def teamView(request):
	"""A view for teams."""
	return DelegateTeamView.as_view()(request)

@login_required
def profileView(request):
	"""
	A view for viewing your profile.
	"""
	if is_delegate(request):
		return delegateProfileView(request)
	elif is_judge(request):
		return TemplateView.as_view(
			template_name="users/judge/profile.html")(request)
	elif is_partner(request):
		return TemplateView.as_view(
			template_name="users/partner/profile.html")(request)

@login_required
def passwordResetView(request):
	"""
	A view for resetting passwords.
	"""
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