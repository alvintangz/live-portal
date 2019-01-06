# django modules
from django.db import models
# helpers
from rounds.helpers import video_upload_to, video_thumbnail_upload_to
from portal.functions import hashid_encode
# models
from users.models import Team
from rounds.models.rounds import Round

class PresentationVideo(models.Model):
	"""
	A video of a presentation by a team for a specific round.
	"""

	team = models.ForeignKey(Team,
		on_delete=models.CASCADE,
		verbose_name="team",
		related_name="videos")

	round = models.ForeignKey(Round,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="round",
		related_name="video")

	video = models.FileField(
		"video",
		upload_to=video_upload_to,
		help_text="Upload a video in H.264/MPEG-4 AVC."
	)

	thumbnail = models.ImageField(
		"thumbnail",
		blank=True,
		upload_to=video_thumbnail_upload_to,
		help_text="Optional. Thumbnail of the video."
	)

	slug = models.SlugField(max_length=8, null=True)

	class Meta:
		verbose_name = "Video"
		verbose_name_plural = "Videos"

	def __str__(self):
		# i.e. Video: Team 14 in Round 2
		return f"Video: Team {self.team.number} in Round {self.round.number}"

	def save(self):
		super().save()
		if not self.slug:
			self.slug = hashid_encode(self.pk, salt="event", min_length=8)
		super().save()