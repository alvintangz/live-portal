from django.views.generic import ListView
from django.shortcuts import redirect
from users.functions import viewByUser
from .models import PortalWidget

def mainView(request):
	"""A view for the main page."""
	if request.user.is_authenticated:
		if request.user.is_superuser:
			return redirect('/executive/')
		else:
			# What's New, view with all the widgets
			return viewByUser(request, DelegateMainView.as_view()(request),
				PartnerMainView.as_view()(request))
	else:
		return redirect('sign-in')

class DelegateMainView(ListView):
	"""A view for delegates for what's new."""
	model = PortalWidget
	template_name = "notifications/whats_new.html"

	def get_queryset(self):
		"""Return a queryset of widgets where showing to delegates is True
		and order if pinned, then when created.
		"""
		return PortalWidget.objects.filter(show_delegate=True
			).order_by('-pinned', '-pk')

class PartnerMainView(ListView):
	"""A view for partners for what's new."""
	model = PortalWidget
	template_name = "notifications/whats_new.html"
	
	def get_queryset(self):
		"""Return a queryset of widgets where showing to partners is True
		and order if pinned, then when created.
		"""
		return PortalWidget.objects.filter(show_partner=True
			).order_by('-pinned', '-pk')