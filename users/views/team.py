from django.views.generic.list import ListView
from users.models import Delegate, Team

class DelegateTeamView(ListView):
	"""A specific view for delegates to view their team members."""
	model = Delegate
	template_name = 'users/delegate/team.html'

	def get_queryset(self, **kwargs):
		"""Returns a queryset that contains delegates in the same team as the
		current user excluding the current user.
		"""
		return Delegate.objects.filter(team=self.request.user.delegate.team
			).exclude(id=self.request.user.delegate.id)