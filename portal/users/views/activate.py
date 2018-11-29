from django.views.generic import View
from users.models import User, Delegate
from django.core.exceptions import ObjectDoesNotExist
from users.forms.activate import ConfirmDelegateForm
from django.shortcuts import redirect, render
from portal.functions import hashid_decode
import portal.variables as imp

class ActivateInformationView(View):
	invalid_template_name = "users/activate/invalid.html"
	delegate_template_name = "users/activate/information/delegate.html"
	partner_template_name = None

	def get(self, request, encoded):
		template = self.invalid_template_name
		context = dict()

		decoded = hashid_decode(encoded,
			salt=imp.user_activation_urls["salt"],
			min_length=imp.user_activation_urls["min_length"])

		if decoded:
			try:
				user = User.objects.get(pk=decoded)
				if not user.activated:
					template = self.delegate_template_name
					context["delegate"] = True
					context["first_name"] = user.first_name
					context["encoded"] = encoded
			except ObjectDoesNotExist:
				pass

		return render(request, template, context)

class ActivateConfirmView(View):
	invalid_template_name = "users/activate/invalid.html"
	delegate_template_name = "users/activate/confirm/delegate.html"
	partner_template_name = None

	def get(self, request, encoded):
		template = self.invalid_template_name
		context = dict()

		decoded = hashid_decode(encoded,
			salt=imp.user_activation_urls["salt"],
			min_length=imp.user_activation_urls["min_length"])

		if decoded:
			try:
				user = User.objects.get(pk=decoded)
				delegate = user.delegate
				if not user.activated:
					template = self.delegate_template_name
					context["delegate"] = user
					context["form"] = ConfirmDelegateForm(instance=delegate)
			except ObjectDoesNotExist:
				pass

		return render(request, template, context)

	def post(self, request, encoded):
		template = self.invalid_template_name
		context = dict()

		decoded = hashid_decode(encoded,
			salt=imp.user_activation_urls["salt"],
			min_length=imp.user_activation_urls["min_length"])

		if decoded:
			try:
				user = User.objects.get(pk=decoded)
				delegate = Delegate.objects.get(user=user)
				if not user.activated:
					template = self.delegate_template_name
					context["delegate"] = delegate
					context["form"] = ConfirmDelegateForm(request.POST,
						request.FILES, instance=delegate)
					if context["form"].is_valid():
						context["form"].save()
						return redirect('profile-confirm-success')
					context["error"] = True
			except ObjectDoesNotExist:
				pass

		return render(request, template, context)
