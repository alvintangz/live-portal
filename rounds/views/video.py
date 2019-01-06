from django.views.generic import DetailView
from users.auth.mixins import PartnerRequiredMixin
from rounds.models import PresentationVideo

class VideoDetailView(PartnerRequiredMixin, DetailView):
	"""
	View for partners that lists all team submissions of a specific round.
	"""
	model = PresentationVideo
	context_object_name = "video"
	template_name = "rounds/video.html"