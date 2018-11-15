from django.views.generic import ListView
from contacts.models import Contact
from users.models import Delegate, Partner
from users.views import viewByUser

def contactUsView(request):
	return viewByUser(request, DelegateContactUsView.as_view()(request), PartnerContactUsView.as_view()(request))

class DelegateContactUsView(ListView):
	model = Contact
	template_name = "contacts/contact_us.html"

	def get_queryset(self):
		return Contact.objects.filter(show_delegates=True)

class PartnerContactUsView(ListView):
	model = Contact
	template_name = "contacts/contact_us.html"
	
	def get_queryset(self):
		return Contact.objects.filter(show_partners=True)