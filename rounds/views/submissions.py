from django.views.generic import DetailView
from users.auth.mixins import PartnerRequiredMixin
from users.models import Team
from rounds.models import Round

class TeamSubmissionsDetailView(PartnerRequiredMixin, DetailView):
	"""
	View for partners that lists all team submissions of a specific round.
	"""
	model = Round
	context_object_name = "round"
	template_name = "rounds/submissions_listed.html"
	slug_field = "number"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# Also exclude teams that haven't submitted anything in the current round
		context["teams"] = Team.objects.exclude(number=0).order_by("number")
		return context