from django.views.generic import ListView
from users.views import viewByUser
from .models import PortalWidget

# MAIN (aka What's New, Dashbaord), view with all the widgets

# Uses viewByUser to provide a view based off which type of user is using the application
def mainView(request):
	return viewByUser(request, DelegateMainView.as_view()(request), PartnerMainView.as_view()(request))

class DelegateMainView(ListView):
	model = PortalWidget
	template_name = "notifications/main.html"

	def get_queryset(self):
		# Only get queryset if shown to delegates is True and order by if pinned, then by when widget was created
		return PortalWidget.objects.filter(show_delegate=True).order_by('-pinned', '-pk')

class PartnerMainView(ListView):
	model = PortalWidget
	template_name = "notifications/main.html"
	
	def get_queryset(self):
		# Only get queryset if shown to partners is True and order by if pinned, then by when widget was created
		return PortalWidget.objects.filter(show_partner=True).order_by('-pinned', '-pk')