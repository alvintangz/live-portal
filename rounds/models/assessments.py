# django modules
from django.db import models
from django.core.exceptions import ValidationError
# models
from users.models import Team, Judge
from .rounds import Round
# helpers
from rounds.helpers import rubric_upload_to

class Rubric(models.Model):
	"""
	A rubric for a round. A Rubric should be related to multiple instances of
	RubricMark, in which each instance holds how much each mark should be out
	of. It is noted that a judge will have a physical copy of a rubric in front
 	of them.
	"""

	round = models.ForeignKey(Round,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="round")

	rubric_document = models.FileField("rubric as a document",
		upload_to=rubric_upload_to,
        blank=True,
		help_text="Optional.")

	release = models.BooleanField("release rubric",
		default=False)

	def __str__(self):
		return f"Rubric: Round {self.round.number}"

class RubricMark(models.Model):
	"""
	Rubric mark is a specific marking entry in a Rubric.
	"""

	rubric = models.ForeignKey(Rubric,
		on_delete=models.CASCADE,
		verbose_name="rubric")

	title = models.CharField("title",
		max_length=100,
		help_text="i.e. Presentation Skills")

	max_mark = models.PositiveSmallIntegerField("maximum possible mark",
		help_text="What the mark is out of.")

	class Meta:
		verbose_name = "rubric mark"
    
	def __str__(self):
		return f"{self.title} - {self.rubric}"

class Assessment(models.Model):
	"""
	An assessment by a judge based off a rubric for a specific team.
	An Assessment should be related to multiple instances of AssessmentMark
	which contain the actual marks.
	"""

	rubric = models.ForeignKey(Rubric,
		on_delete=models.CASCADE,
		verbose_name="rubric")

	judge = models.ForeignKey(Judge,
		on_delete=models.CASCADE,
		verbose_name="judge")
	
	team = models.ForeignKey(Team,
		on_delete=models.CASCADE,
		verbose_name="team")

	rough_notes = models.TextField("rough notes",
		help_text=("Add any rough notes here. Will NOT be counted in the " +
			"team's score."),
		blank=True)

	last_updated = models.DateTimeField("last updated",
		auto_now=True)

	def __str__(self):
		return f"{self.judge.user.get_full_name()} - {self.rubric} - {self.team}"

class AssessmentMark(models.Model):
	"""
	An assessment mark by a judge which is a mark out of a related rubric mark.
	"""
	
	assessment = models.ForeignKey(Assessment,
		on_delete=models.CASCADE,
		verbose_name="assessment")

	rubric_mark = models.ForeignKey(RubricMark,
		on_delete=models.CASCADE)
	
	mark = models.PositiveSmallIntegerField("assessment mark",
		help_text="The assessment mark cannot be greater than the rubric mark.")
	
	def clean(self):
		# Ensure mark is lower or equal to rubric_mark before saving
		if self.mark > self.rubric_mark.max_mark:
			raise ValidationError("The assessment mark cannot be greater " +
                "than the rubric mark.")