# django modules
from django.db import models
# helpers
from rounds.helpers import video_upload_to

class PresentationVideo(models.Model):
	"""
	A video of a presentation by a team for a specific round.
	"""

	team = models.ForeignKey(Team,
		on_delete=models.CASCADE,
		verbose_name="team")

	round = models.ForeignKey(Round,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="round")

	video = models.FileField(
		"video",
		upload_to=video_upload_to,
		help_text="Upload a video in H.264/MPEG-4 AVC."
	)

	thumbnail = models.ImageField(
		"thumbnail",
		blank=True,
		upload_to=video_thumbnail_upload_to,
		"Optional. Thumbnail of the video."
	)

	def __str__(self):
		# i.e. Video: Team 14 in Round 2
		return f"Video: Team {self.team.number} in Round {self.round.number}"