import uuid
from django.db import models
from .constants.filetypes import FILETYPES, FILETYPES_LISTED
from users.models import Team

class Round(models.Model):
	'''
	A model that represents a round. Before a round is released, there should be some associated accepted round files.
	'''

	# To be used in the URL
	uuid = models.UUIDField(
		'unique identifier',
		default=uuid.uuid4,
		editable=False,
		unique=True)

	# True if delegates can submit files 
	active = models.BooleanField('active', default=False, help_text="Set True during round.")

	# True if it is visible to delegates, usually set True during and after round
	visible = models.BooleanField('visible', default=False, help_text="Set True during and after round.")

	number = models.SmallIntegerField('round number', help_text="Make sure there is not another round with the same number.")

	title = models.CharField('title', max_length=80)

	description = models.TextField('description',
		blank=True,
		help_text="Write a description that all delegates could see, which provides more details into the current round.")

	# Could add a file that delegates could see which provide details about the current round
	details_file = models.FileField('file with details',
		blank=True,
		help_text="Upload a file that all delegates could see, which provides more details into the current round.")

	expected_deadline = models.DateTimeField('expected deadline',
		help_text="The web application will not automatically close the round, it needs to be done manually.")

	show_deadline = models.BooleanField('show deadline publicly',
		default=False,
		help_text="If True, then the deadline will be shared to delegates.")

	def get_expected_deadline(self):
		return self.expected_deadline.strftime("%I:%M %p on %b %d, %Y")

	def __str__(self):
		if self.active:
			return str(self.number) + "(" +self.title + " - Active Round)"
		else:
			return str(self.number) + "(" +self.title + " - Unactive Round)"

class AcceptedRoundFile(models.Model):

	asc_round = models.ForeignKey(Round, on_delete=models.CASCADE)

	files_accepted = models.SmallIntegerField('file type(s) accepted', choices=FILETYPES)

	title = models.CharField('title', max_length=80)

	show_title = models.BooleanField('show title', default=False)

	class Meta:
		verbose_name = "acceptable file for round"

	def get_validators(self):
		for filetype in FILETYPES_LISTED:
			for key in filetype:
				if key == self.files_accepted:
					return self.filetype[key]

	def __str__(self):
		if self.asc_round.active:
			return self.title + " - " + self.asc_round.title + " (Active Round)"
		else:
			return self.title + " - " + self.asc_round.title + " (Unactive Round)"

class Submission(models.Model):

	# Associated Team
	asc_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

	# Associated Round File
	asc_round_file = models.ForeignKey(AcceptedRoundFile, on_delete=models.SET_NULL, null=True)

	# Keep track of the team member (their primary key) who submitted it
	submitted_by = models.IntegerField('submitted by (id of user)')

	submitted_file = models.FileField('submitted file')

	submitted_at = models.DateTimeField('date and time of submission')

	latest = models.BooleanField('latest file')

	def __str__(self):
		return "Round " + str(self.asc_round_file.asc_round.number) + " submission by team " + str(self.asc_team.number)