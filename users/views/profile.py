from users.forms.profile import DelegateProfileUpdateForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from users.models import Judge

def delegateProfileView(request):
	"""View where delegates edit their profiles."""
	form = DelegateProfileUpdateForm(instance=request.user.delegate)
	context =  {'form': form}

	if request.method == 'POST':
		form = DelegateProfileUpdateForm(request.POST, request.FILES,
			instance=request.user.delegate)
		if form.is_valid():
			form.save()
			# Redirect to same page but with success get param to show success
			return redirect('profile-success')
		else:
			context["error"] = True

	return render(request, 'users/delegate/profile.html', context)