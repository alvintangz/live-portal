from django.db import models
from .constants.filetypes import FILETYPES, FILETYPES_LISTED
from users.models import Team, User
from portal.functions import hashid_encode, default_shortstrftime
from .helpers import submission_upload_to

class Round(models.Model):
	'''
	A model that represents a round. Before a round is released, there should be some associated accepted round files.
	'''

	active = models.BooleanField('active',
		default=False,
		help_text="Submissions for rounds allowed. Set True during round.")

	visible = models.BooleanField('visible',
		default=False,
		help_text="Round is visible. Set True during and after round.")

	number = models.SmallIntegerField('round number',
		help_text="Ensure sure there is no other round with thesame number.")

	title = models.CharField('title', max_length=80)

	description = models.TextField('description',
		blank=True,
		help_text=("Optional. Write a publicly displayed description, that " +
			"provides more details into the current round."))

	details_file = models.FileField('file with details',
		upload_to="rounds/round/details/",
		blank=True,
		help_text=("Optional. Upload a publicly displayed file, that " +
		"provides more details into the current round."))

	expected_deadline = models.DateTimeField('expected deadline',
		help_text=("Please note: the web application will not automatically " +
		"close the round, it needs to be done manually."))

	show_deadline = models.BooleanField('show deadline publicly',
		default=False,
		help_text="If True, then the deadline will be shared publicly.")

	survey_link = models.URLField("survey link",
		blank=True,
		help_text=("Optional. Add a link to a survey to be shown when visible" +
			" but not active (to delegates)."))

	def get_expected_deadline(self):
		return default_shortstrftime(self.expected_deadline)

	@property
	def encoded_url(self):
		return hashid_encode(self.pk)

	def __str__(self):
		desc = "Round %s: %s (%s)"
		if self.active:
			return desc % (str(self.number), self.title, "Active")
		return desc % (str(self.number), self.title, "Not Active")

class AcceptedRoundFile(models.Model):

	asc_round = models.ForeignKey(Round,
		on_delete=models.CASCADE)

	files_accepted = models.SmallIntegerField('file type(s) accepted',
		choices=FILETYPES)

	title = models.CharField('title',
		max_length=80)

	show_title = models.BooleanField('show title',
		default=True)

	class Meta:
		verbose_name = "acceptable file for round"

	def get_validators(self):
		for filetype in FILETYPES_LISTED:
			if filetype[0] == self.files_accepted:
				return filetype[1]

	def get_validators_str(self):
		filetypes = []
		for filetype in FILETYPES_LISTED:
			if filetype[0] == self.files_accepted:
				filetypes += filetype[1]
		if len(filetypes) == 0:
			# Which shouldn't happen
			string = "Upload anything."
		else:
			string = "Accepted file types: "
			for filetype in filetypes:
				string += filetype + ", "
			string = string[0:-2]
		return string

	def get_validators_accepted_html(self):
		filetypes = []
		string = ""
		for filetype in FILETYPES_LISTED:
			if filetype[0] == self.files_accepted:
				filetypes += filetype[1]
		
		for filetype in filetypes:
			string += "." + filetype + ", "
		return string

	def get_title_for_delegates(self):
		if self.show_title:
			return self.title
		else:
			return self.get_validators_str()

	def __str__(self):
		return "%s - %s" % (self.title, str(self.asc_round))

class Submission(models.Model):

	# Associated Team
	asc_team = models.ForeignKey(Team,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name='team')

	# Associated Round File
	asc_round_file = models.ForeignKey(AcceptedRoundFile,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name='round file')

	# Associated Round
	asc_round = models.ForeignKey(Round,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="round")

	# Keep track of the team member (their primary key) who submitted it
	submitted_by = models.IntegerField('submitted by (id of user)')

	submitted_file = models.FileField('submitted file',
		upload_to=submission_upload_to)

	submitted_at = models.DateTimeField('date and time of submission')

	latest = models.BooleanField('latest file')

	def get_submitted_by_name(self):
		return User.objects.get(pk=self.submitted_by).first_name
	get_submitted_by_name.short_description = "Submitted by"

	def get_formatted_submitted_at(self):
		return default_shortstrftime(self.submitted_at)
	get_formatted_submitted_at.short_description = "Time of submission"

	def __str__(self):
		return "Round " + str(self.asc_round_file.asc_round.number) + " submission by team " + str(self.asc_team.number)