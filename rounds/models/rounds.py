# django modules
from django.db import models
# constants
from rounds.constants.filetypes import FILETYPES, FILETYPES_LISTED
# helpers
from portal.functions import hashid_encode, default_shortstrftime
from rounds.helpers import round_details_upload_to

class Round(models.Model):
	"""
	A round in the competition. For delegates to submit a file for a round,
    an AcceptedRoundFile that has a relationship with a Round must exist.
    """

	active = models.BooleanField("active",
		default=False,
		help_text="If True, delegates can submit files.")

	visible = models.BooleanField("visible",
		default=False,
		help_text="If True, delegates can view the details of the round.")

    # ASIDE: Can be switched to PositiveIntegerField for next implementation
	number = models.SmallIntegerField("round number",
        unique=True)

	title = models.CharField("title",
        max_length=80)

	description = models.TextField("description",
		blank=True,
		help_text=("Optional. Write a public description, that provides more " +
            "information about the current round."))

	details_file = models.FileField("file with details",
		upload_to=round_details_upload_to,
		blank=True,
		help_text=("Optional. Upload a public file, that provides more " +
            "information about the current round."))

	expected_deadline = models.DateTimeField("expected deadline",
		help_text="NOTE: The round will not automatically close.")

	show_deadline = models.BooleanField("show deadline publicly",
		default=False,
		help_text="If True, then the deadline will be shared publicly.")

	survey_link = models.URLField("survey link",
		blank=True,
		help_text=("Optional. Add a link to a survey to be shown when the " +
			" round is visible but not active (to delegates)."))

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
	"""
	An acceptable file for a round. Needed as a round may allow multiple
	file submissions of different types.
	"""

	asc_round = models.ForeignKey(Round,
		on_delete=models.CASCADE)

	files_accepted = models.SmallIntegerField("file type(s) accepted",
		choices=FILETYPES)

	title = models.CharField("title",
		max_length=80)

	show_title = models.BooleanField("show title",
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