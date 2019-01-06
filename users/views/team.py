from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from users.models import Delegate, Team
from users.auth.mixins import DelegateRequiredMixin, PartnerRequiredMixin

class DelegateTeamView(DelegateRequiredMixin, ListView):
	"""
	A specific view for delegates to view their team members.
	"""
	model = Delegate
	template_name = 'users/delegate/team.html'

	def get_queryset(self, **kwargs):
		"""
		Returns a queryset that contains delegates in the same team as the
		current user excluding the current user.
		"""
		return Delegate.objects.filter(team=self.request.user.delegate.team
			).exclude(id=self.request.user.delegate.id)

class PartnerTeamListView(PartnerRequiredMixin, ListView):
	"""
	A specific view for partners to view all teams.
	"""
	model = Team
	template_name = 'users/teams/listed.html'
	context_object_name = "teams"
	ordering = ('place',)
	
	def get_queryset(self, **kwargs):
		"""
		Returns a queryset that excludes team 0.
		"""
		# ASIDE: Maybe also include excluding any teams with 0 delegates.
		# ASIDE: Fix ordering when blank not just null
		return super().get_queryset(**kwargs).exclude(number=0).extra(
			select={'number_null': 'number is null'}).extra(
				order_by=['number_null'])

class PartnerTeamDetailView(PartnerRequiredMixin, DetailView):
	"""
	A specific view for partners to view specific teams.
	"""
	model = Team
	template_name = 'users/teams/detail.html'
	slug_field = "number"
	context_object_name = "team"
	# ASIDE: Exclude team 0 in get_context_object