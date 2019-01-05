# django modules
from django.db import models
from django.core.exceptions import ValidationError
# models
from users.models import Team, Judge
from .rounds import Round
# helpers
from portal.functions import hashid_encode
from rounds.helpers import rubric_upload_to

class Rubric(models.Model):
	"""
	A rubric for a round. A Rubric should be related to multiple instances of
	RubricMark, in which each instance holds how much each mark should be out
	of. It is noted that a judge will have a physical copy of a rubric in front
 	of them.
	"""

	round = models.OneToOneField(Round,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="round")

	rubric_document = models.FileField("rubric as a document",
		upload_to=rubric_upload_to,
        blank=True,
		help_text="Optional.")

	release = models.BooleanField("release rubric",
		default=False,
		help_text="If this is True, then the round is visible to judge.")

	def __str__(self):
		return f"Rubric: Round {self.round.number}"

class RubricMark(models.Model):
	"""
	Rubric mark is a specific marking entry in a Rubric.
	"""

	rubric = models.ForeignKey(Rubric,
		on_delete=models.CASCADE,
		verbose_name="rubric",
		related_name="marks")

	title = models.CharField("title",
		max_length=100,
		help_text="i.e. Presentation Skills")

	max_mark = models.PositiveSmallIntegerField("maximum possible mark",
		help_text="What the mark is out of.")

	class Meta:
		verbose_name = "rubric mark"
    
	def __str__(self):
		return f"{self.title} (out of {str(self.max_mark)}) - {self.rubric}"

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
		help_text=("Optional. Will NOT be counted in the " +
			"team's score."),
		blank=True)

	last_updated = models.DateTimeField("last updated",
		auto_now=True,
		blank=True)

	submitted = models.BooleanField("submitted",
		help_text=("Whether or not the assessment has been submitted by judge."),
		default=False)

	slug = models.SlugField(max_length=8, null=True)

	def get_round_and_team(self):
		return f"Round {self.rubric.round.number} - {self.team}"

	def save(self):
		if not self.pk:
			rmarks = self.rubric.marks.all()
			super().save()
			for rmark in rmarks:
				AssessmentMark.objects.create(rubric_mark=rmark, 
					assessment=self)
		super().save()
		if not self.slug:
			self.slug = hashid_encode(self.pk, salt="assessment", min_length=8)
		super().save()

	def __str__(self):
		return f"{self.judge.user.get_full_name()} - {self.rubric} - {self.team}"

class AssessmentMark(models.Model):
	"""
	An assessment mark by a judge which is a mark out of a related rubric mark.
	"""
	
	assessment = models.ForeignKey(Assessment,
		on_delete=models.CASCADE,
		verbose_name="assessment",
		related_name="marks")

	rubric_mark = models.ForeignKey(RubricMark,
		on_delete=models.CASCADE,
		null=True)
	
	mark = models.PositiveSmallIntegerField("assessment mark",
		help_text="The assessment mark cannot be greater than the rubric mark.",
		null=True)
	
	def clean(self):
		# Ensure mark is lower or equal to rubric_mark before saving
		if self.rubric_mark and self.mark:
			if self.mark > self.rubric_mark.max_mark:
				raise ValidationError("The assessment mark cannot be greater " +
                	"than the rubric mark.")
	
	def __str__(self):
		return str(self.rubric_mark)