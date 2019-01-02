# django modules
from django.views.generic import ListView
# models
from contacts.models import Contact
# helpers
from users.auth.mixins import TypesRequiredMixin

class LIVETeamListView(TypesRequiredMixin, ListView):
	model = Contact
	template_name = "contacts/contact_us.html"
	context_object_name = "contacts"
	delegate_allowed = True
	partner_allowed = True
	judge_allowed = True

	def get_queryset(self):
		if self.is_partner():
			return Contact.objects.filter(show_partners=True)
		elif self.is_judge():
			return Contact.objects.filter(show_judges=True)
		elif self.is_delegate():
			return Contact.objects.filter(show_delegates=True)