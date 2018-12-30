# django modules
from django.db import models
from django.utils.safestring import mark_safe
# models
from users.models import Team, User
from .rounds import Round, AcceptedRoundFile
# helpers
from rounds.helpers import submission_upload_to
from portal.functions import default_shortstrftime

class Submission(models.Model):
	"""
	A submission for a round, uploaded by a delegate for a team.
	"""

	asc_team = models.ForeignKey(Team,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="team")

	asc_round_file = models.ForeignKey(AcceptedRoundFile,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="round file")

	asc_round = models.ForeignKey(Round,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="round")

	submitted_by = models.IntegerField("submitted by (id of user)")

	submitted_file = models.FileField("submitted file",
		upload_to=submission_upload_to)

	submitted_at = models.DateTimeField("date and time of submission")

	latest = models.BooleanField("latest file",
        help_text="If True, this file is the latest file from a team. ")

	def get_submitted_by_name(self):
		return User.objects.get(pk=self.submitted_by).first_name
	get_submitted_by_name.short_description = "Submitted by"

	def get_formatted_submitted_at(self):
		return default_shortstrftime(self.submitted_at)
	get_formatted_submitted_at.short_description = "Time of submission"

	def get_view_html(self):
		"""
		A link to view the file in HTML format.
		"""
		return mark_safe(f"<a href=\"{self.submitted_file.url}\" " +
			"download>View File</a>")
	get_view_html.short_description = "View File"

	def __str__(self):
		return f"Round {str(self.asc_round.number)}; Team {str(self.asc_team.number)}"