# django modules
from django.views.generic import ListView
from django.shortcuts import redirect
# helpers
from users.auth.mixins import DelegateRequiredMixin, PartnerRequiredMixin
from users.auth.functions import is_delegate, is_judge, is_partner
# models
from .models import PortalWidget

def mainView(request):
	"""
	A view for the main page.
	"""
	if not request.user.is_authenticated:
		return redirect('sign-in')
	if request.user.is_superuser:
		return redirect('/executive/')
	elif is_delegate(request):
		return DelegateMainView.as_view()(request)
	elif is_partner(request):
		return PartnerMainView.as_view()(request)
	elif is_judge(request):
		return redirect('rounds')
	return redirect('sign-in')

class DelegateMainView(DelegateRequiredMixin, ListView):
	"""
	A view for delegates for what's new.
	"""
	model = PortalWidget
	template_name = "notifications/whats_new.html"

	def get_queryset(self):
		"""Return a queryset of widgets where showing to delegates is True
		and order if pinned, then when created.
		"""
		return PortalWidget.objects.filter(show_delegate=True
			).order_by('-pinned', '-pk')

class PartnerMainView(PartnerRequiredMixin, ListView):
	"""
	A view for partners for what's new.
	"""
	model = PortalWidget
	template_name = "notifications/whats_new.html"
	
	def get_queryset(self):
		"""Return a queryset of widgets where showing to partners is True
		and order if pinned, then when created.
		"""
		return PortalWidget.objects.filter(show_partner=True
			).order_by('-pinned', '-pk')