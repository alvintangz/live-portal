# constants
from .constants.universities import CANADIAN_UNIS
from .constants.student_types import STUDENT_TYPES
from .constants.seeking_statuses import SEEKING_STATUSES
from .constants.partner_types import PARTNER_TYPES
import portal.variables as imp
from django.urls import reverse
# django modules
from django.db import models
from django.contrib.auth.models import AbstractUser
# helpers
from .helpers import resume_upload_to, profile_picture_upload_to
from portal.functions import resize_and_convert, hashid_encode
from portal.functions import send_sms

class Team(models.Model):
	
	number = models.IntegerField('team number',
		unique=True)

	place = models.PositiveSmallIntegerField('ranking',
		blank=True,
		null=True,
		help_text="The team's place (ranking) in the competition.")

	def get_members_listed(self):
		delegates = Delegate.objects.filter(team=self.pk)
		ret_val = ""
		ret_val = ", ".join(
			[delegate.user.get_full_name() for delegate in delegates])
		if ret_val == "":
			ret_val = "No members in this team."
		return ret_val

	def get_members_listed_html(self):
		delegates = Delegate.objects.filter(team=self.pk)
		ret_val = ""
		ret_val = ", ".join(
			[("<a class=\"text-secondary\" href=\"" + reverse("delegates-detail", 
				kwargs={"pk": delegate.pk }) + "\">" + 
				delegate.user.get_full_name() + "</a>") 
				for delegate in delegates])
		if ret_val == "":
			ret_val = "No members in this team."
		return ret_val

	def __str__(self):
		return 'Team {}'.format(self.number)

class User(AbstractUser):

	is_delegate = models.BooleanField('delegate status', default=False)

	is_partner = models.BooleanField('partner status', default=False)

	is_judge = models.BooleanField('judge status', default=False)

	first_name = models.CharField('first name', max_length=30, blank=False)

	last_name = models.CharField('last name', max_length=30, blank=False)

	email = models.EmailField('email address', blank=True)

	activated = models.BooleanField('activated account',
		default=False)

	agreed_terms = models.DateTimeField('agreed to all terms on',
		blank=True,
		null=True)

	def activation_link(self):
		return imp.urls["portal"] + "/account/activate/" + hashid_encode(self.pk, 
			salt=imp.user_activation_urls["salt"],
			min_length=imp.user_activation_urls["min_length"])

	def __str__(self):
		return f"{self.get_full_name()} ({self.username})"

class Delegate(models.Model):

	user = models.OneToOneField(User,
		on_delete=models.CASCADE,
		related_name='delegate')

	team = models.ForeignKey(Team,
		on_delete=models.SET_NULL,
		null=True,
		related_name="delegates")

	profile_picture = models.ImageField('profile picture',
		upload_to=profile_picture_upload_to,
		blank=True,
		max_length=500)

	profile_picture_block = models.BooleanField('block profile picture',
		default=False,
		blank=True,
		help_text="Only block the user's profile picture for partners.")

	school = models.CharField('currently attending',
		max_length=150,
		choices=CANADIAN_UNIS,
		help_text='If the school is not listed, please contact the admin',
		blank=True)

	year_of_study = models.CharField('year in school', max_length=40,
		choices=STUDENT_TYPES,
		blank=True)

	program = models.CharField('program',
		max_length=150,
		blank=True)

	linkedin = models.URLField('link to linkedin profile',
		max_length=100,
		blank=True)

	resume = models.FileField('resume',
		upload_to=resume_upload_to,
		blank=True,
		null=True)

	phone_number = models.CharField('phone number',
		max_length=10,
		blank=True)

	seeking_status = models.CharField('seeking status',
		max_length=80,
		choices=SEEKING_STATUSES,
		blank=True)

	is_invisible = models.BooleanField('invisible to partners',
		default=False,
		help_text="Set this as True if you want to make this delegate " + 
		"invisible to partners. This option is used for testing purposes.")

	@property
	def encoded_url(self):
		return hashid_encode(self.pk)

	def __init__(self, *args, **kwargs):
		super(Delegate, self).__init__(*args, **kwargs)
		self.initial_number = self.phone_number

	def save(self):
		number = self.initial_number
		super(Delegate, self).save()
		if self.profile_picture:
			resize_and_convert(self.profile_picture)
		if self.phone_number != "" and self.phone_number != number:
			send_sms("+1"+self.phone_number, 
				imp.sms_messages["added_number"] % self.user.first_name)

	def __str__(self):
		"""Returns a string that represents the current Delegate.
		e.g. Delegate: Alvin Tang (Team 5)
		"""
		if self.team is None:
			team_status = "Not in a team"
		else: 
			team_status = 'Team {}'.format(self.team.number)

		return 'Delegate: {} {} ({})'.format(self.user.first_name,
			self.user.last_name, team_status)

class Partner(models.Model):

	user = models.OneToOneField(User,
		on_delete=models.CASCADE,
		related_name='partner')

	# ASIDE: Can be removed, and replaced with a ForeignKey to a corporate
	# organization for next implementation
	company_name = models.CharField('organization name',
		max_length=130,
		help_text="Will be displayed to the partner.")

	# ASIDE: Look at ASIDE above.
	partner_package = models.CharField('package',
		max_length=60,
		choices=PARTNER_TYPES,
		help_text="Will be displayed to the partner.")

	def __str__(self):
		"""Returns a string that represents the current Partner object.
		e.g. Partner: Microsoft (Gold Package)
		"""
		if self.partner_package is None:
			package = "package not defined"
		else:
			package = '%s Package' % (self.partner_package)

		return 'Partner: %s (%s)' % (self.company_name, package)

class Judge(models.Model):
	
	user = models.OneToOneField(User,
		on_delete=models.CASCADE,
		related_name='judge')

	number = models.PositiveSmallIntegerField("number",
		unique=True)

	room = models.CharField("room",
		max_length=60,
		blank=True,
		help_text="Optional. Room in which this judge is in.")

	def get_assessments(self):
		from rounds.models.assessments import Assessment
		assessments = Assessment.objects.filter(judge=self.pk)
		ret_val = ", ".join(
			[assessment.get_round_and_team() for assessment in assessments]
		)
		if ret_val == "":
			ret_val = "None chosen."
		return ret_val
	get_assessments.short_description = "Assigned Assessments"

	def __str__(self):
		return f"Judge {str(self.number)} - {self.user.get_full_name()}"