from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from .forms import DelegateUserForm, DelegateProfileForm
from .models import Delegate

@login_required
def viewByUser(request, delgateView, partnerView):
	'''
	Return a delegate view or a partner view depending on who is logged in.
	'''
	if hasattr(request.user, 'delegate'):
		if delegateView is None:
			return django.views.defaults.page_not_found()
		else:
			return delgateView
	elif hasattr(request.user, 'partner'):
		if partnerView is None:
			return django.views.defaults.page_not_found()
		else:
			return partnerView
	else:
		# Undefined user views a error page
		return TemplateView.as_view(template_name="errors/undefined_user.html")(request)

class TeamView(ListView):
	'''
	A specific view for delegates to view their team members.
	'''
	model = Delegate

	def get_queryset(self, **kwargs):
		'''
		QuerySet used will only contain delegates in the same team as the current user excluding the current user.
		'''
		return Delegate.objects.filter(team=self.request.user.delegate.team).exclude(id=self.request.user.delegate.id)

def profileView(request):
	return viewByUser(request, delegateProfileView(request), TemplateView.as_view(template_name='privacy_policy.html')(request))

def delegateProfileView(request):
	user_form = DelegateUserForm(instance=request.user)
	profile_form = DelegateProfileForm(instance=request.user.delegate)
	context =  {'user_form': user_form, 'profile_form': profile_form}

	if request.method == 'POST':
		user_form = DelegateUserForm(request.POST)
		profile_form = DelegateProfileForm(request.POST, request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			context['success'] = 'Your profile was successfully updated!'
			redirect('profile')
		else:
			context['error'] = 'Please fill in your form correctly.'
	return render(request, 'users/delegate/edit_profile.html', context)

class PartnerProfileView(UpdateView):
	'''
	A specific view for partners to edit their profile.
	'''
	pass