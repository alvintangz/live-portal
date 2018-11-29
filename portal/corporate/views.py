from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from users.decorators import delegate_required
from .models import (
	CorporateOrganization,
	Mentor,
	Judge,
	Speaker,
	Networker
)

@method_decorator(delegate_required, name='dispatch')
class PartnersListView(ListView):
	template_name = "corporate/partners_listed.html"
	context_object_name = "partners"

	def get_queryset(self):
		return CorporateOrganization.objects.filter(partner=True).order_by(
			'partner_type')

@method_decorator(delegate_required, name='dispatch')
class CorporateIndividualsListView(ListView):
	template_name = "corporate/individuals_listed.html"
	context_object_name = "individuals"
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['type_of'] = self.model._meta.verbose_name
		context['type_of_plural'] = self.model._meta.verbose_name_plural
		context['type_of_title'] = self.model._meta.verbose_name.title()
		context['type_of_plural_title'] = (
			self.model._meta.verbose_name_plural.title())
		return context

class MentorsListView(CorporateIndividualsListView):
	model = Mentor

class JudgesListView(CorporateIndividualsListView):
	model = Judge

class SpeakersListView(CorporateIndividualsListView):
	model = Speaker

class NetworkersListView(CorporateIndividualsListView):
	model = Networker