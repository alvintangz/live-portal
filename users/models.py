from .constants.universities import CANADIAN_UNIS
from .constants.student_types import STUDENT_TYPES
from .constants.seeking_statuses import SEEKING_STATUSES
from .constants.partner_types import PARTNER_TYPES
from django.db import models
from django.contrib.auth.models import AbstractUser
from .helpers import resume_upload_to, profile_picture_upload_to
from portal.functions import resize_and_convert, hashid_encode
from portal.functions import send_sms
import portal.variables as imp

class Team(models.Model):
	
	number = models.IntegerField('team number',
		unique=True)

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

	def set_delegate(self):
		"""Sets user as a delegate."""
		self.is_delegate = True

	def set_partner(self):
		"""Sets user as a partner."""
		self.is_partner = True

	def activation_link(self):
		return imp.urls["portal"] + "/account/activate/" + hashid_encode(self.pk, 
			salt=imp.user_activation_urls["salt"],
			min_length=imp.user_activation_urls["min_length"])

class Delegate(models.Model):

	user = models.OneToOneField(User,
		on_delete=models.CASCADE,
		related_name='delegate')

	team = models.ForeignKey(Team,
		on_delete=models.SET_NULL,
		null=True)

	profile_picture = models.ImageField('profile picture',
		upload_to=profile_picture_upload_to,
		blank=True,
		max_length=500)

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

	company_name = models.CharField('company name',
		max_length=130)

	partner_package = models.CharField('package',
		max_length=60,
		choices=PARTNER_TYPES)

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

	def __str__(self):
		return f"Judge {str(self.number)}"