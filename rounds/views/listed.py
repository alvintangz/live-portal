from django.views.generic import ListView
from django.utils.decorators import method_decorator
from rounds.models.rounds import Round

# Generalized view for both delegates and partners
class ListedRoundsView(ListView):
	"""View that lists all rounds."""
	model = Round
	template_name = "rounds/listed.html"

	def get_queryset(self):
		return Round.objects.filter(visible=True).order_by("number")
