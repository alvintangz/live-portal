from .constants.universities import CANADIAN_UNIS
from .constants.student_types import STUDENT_TYPES
from .constants.seeking_statuses import SEEKING_STATUSES
from .constants.partner_types import PARTNER_TYPES
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):

	uuid = models.UUIDField(
		'unique identifier',
		default=uuid.uuid4,
		editable=False,
		unique=True)

	number = models.IntegerField(
		'team number')

	def __str__(self):
		return 'Team {}'.format(self.number)

class User(AbstractUser):

	is_delegate = models.BooleanField('delegate status', default=False)
	
	is_partner = models.BooleanField('partner status', default=False)

	uuid = models.UUIDField(
		'unique identifier',
		default=uuid.uuid4,
		editable=False,
		unique=True)

	activated = models.BooleanField(
		'user has activated account',
		default=False)

	def set_delegate(self):
		self.is_delegate = True

	def set_partner(self):
		self.is_partner = True

	def set_email(self, email):
		self.set_email = email

class Delegate(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.SET_NULL,
		null=True,
		related_name='delegate')

	profile_picture = models.ImageField('profile picture',
		height_field=500,
		width_field=500,
		blank=True)

	year_of_study = models.CharField('year in school', max_length=40,
		choices=STUDENT_TYPES)

	school = models.CharField('currently attending',
		max_length=150,
		choices=CANADIAN_UNIS,
		help_text='If the school is not listed, please contact the admin')

	program = models.CharField('program', max_length=150)

	linkedin = models.URLField('link to linkedin profile',
		max_length=100,
		blank=True)

	resume = models.FileField('resume')

	phone_number = models.CharField('phone number',
		max_length=10)

	team = models.ForeignKey(Team,
		on_delete=models.SET_NULL,
		null=True)

	seeking_status = models.CharField('seeking status',
		max_length=80,
		choices=SEEKING_STATUSES)

	last_updated = models.DateTimeField('last updated profile',
		blank=True,
		null=True)

	def __str__(self):
		'''
		Returns a string that represents the current Delegate.
		e.g. Delegate: Alvin Tang (Team 5)
		'''
		if self.team is None:
			team_status = "Not in a team"
		else: 
			team_status = 'Team {}'.format(self.team.number)

		return 'Delegate: {} {} ({})'.format(self.user.first_name, self.user.last_name, team_status)

class Partner(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.SET_NULL,
		null=True,
		related_name='partner')

	company_name = models.CharField(
		'company name',
		max_length=130)

	partner_package = models.CharField(
		'package',
		max_length=60,
		choices=PARTNER_TYPES)

	def __str__(self):
		'''
		Returns a string that represents the current Partner object.
		e.g. Partner: Microsoft (Gold Package)
		'''
		if self.partner_package is None:
			package = "package not defined"
		else:
			package = '{} Package'.format(self.partner_package)

		return 'Partner: {} ({})'.format(self.company_name, package)