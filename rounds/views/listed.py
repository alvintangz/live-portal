# django modules
from django.views.generic import ListView
# models
from rounds.models.rounds import Round
from rounds.models.assessments import Rubric, Assessment
from users.models import Team
# helpers
from users.auth.mixins import TypesRequiredMixin, JudgeRequiredMixin
from portal.functions import hashid_decode

class ListedRoundsView(TypesRequiredMixin, ListView):
	"""
	View that lists all rounds.
	"""
	model = Round
	template_name = "rounds/rounds_listed.html"
	context_object_name = "rounds"
	delegate_allowed = True
	partner_allowed = True
	judge_allowed = True

	def get_queryset(self):
		rounds = Round.objects.order_by("number")
		if self.is_judge():
			return rounds.filter(rubric__release=True)
		return rounds.filter(visible=True)

class TeamsListedView(JudgeRequiredMixin, ListView):
	"""
	View that lists all teams that can be judged for a specific round for the
	current judge.
	"""
	model = Team
	context_object_name = "teams"
	template_name = "rounds/teams_listed.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		decoded_round = hashid_decode(self.kwargs['encoded'])
		try:
			context["round"] = Round.objects.get(pk=decoded_round)
		except:
			context["round"] = False
		return context

	def get_queryset(self):
		decoded_round = hashid_decode(self.kwargs['encoded'])
		try:
			rubric = (Round.objects.get(pk=decoded_round)).rubric
			if not rubric.release:
				return list()
			assessments_with_rubric = Assessment.objects.filter(
				judge=self.request.user.judge).filter(rubric=rubric)
			teams = [ass.team for ass in assessments_with_rubric]
			return teams
		except:
			return list()