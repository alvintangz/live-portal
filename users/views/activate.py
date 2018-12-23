# django modules
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test
# models
from users.models import Delegate, User
# forms
from users.forms.activate import ConfirmDelegateForm, EmailForm
# helpers
from portal.functions import hashid_decode
# constants
import portal.variables as imp

def activateInformationView(request, encoded):
	invalid_template_name = "users/activate/invalid.html"
	delegate_template_name = "users/activate/information/delegate.html"
	template_name = invalid_template_name
	context = dict()

	decoded = hashid_decode(encoded,
		salt=imp.user_activation_urls["salt"],
		min_length=imp.user_activation_urls["min_length"])

	if decoded:
		try:
			temp = User.objects.get(pk=decoded)
			if not temp.activated:
				template_name = delegate_template_name
				context["delegate"] = True
				context["first_name"] = temp.first_name
				context["encoded"] = encoded
		except ObjectDoesNotExist:
			pass

	return render(request, template_name, context)

def activateConfirmView(request, encoded):
	invalid_template_name = "users/activate/invalid.html"
	delegate_template_name = "users/activate/confirm/delegate.html"
	template_name = invalid_template_name
	context = dict()

	decoded = hashid_decode(encoded,
		salt=imp.user_activation_urls["salt"],
		min_length=imp.user_activation_urls["min_length"])

	if decoded:
		try:
			temp = User.objects.get(pk=decoded)
			delegate = Delegate.objects.get(user=temp)
			if not temp.activated:
				template_name = delegate_template_name
				context["delegate"] = temp
				context["encoded"] = encoded
				context["form"] = ConfirmDelegateForm(instance=delegate)
				if request.method == "POST":
					context["form"] = ConfirmDelegateForm(request.POST,
						request.FILES, instance=delegate)
					if context["form"].is_valid():
						context["form"].save()
						return redirect('sign-in-confirmed')
					context["error"] = True
		except ObjectDoesNotExist:
			pass

	return render(request, template_name, context)