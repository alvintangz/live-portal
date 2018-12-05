# django modules
from django.db import models
# constants
from .constants.corporate_individual_types import CORPORTATE_INDIVIDUAL_TYPES

class CorporateIndividualManager(models.Manager):
	def is_mentor(self):
		return self.filter(type_of='Mentor')

	def is_judge(self):
		return self.filter(type_of='Judge')

	def is_speaker(self):
		return self.filter(type_of='Speaker')

	def is_networker(self):
		return self.filter(type_of='Networker')

class MentorManager(models.Manager):
	def get_queryset(self):
		return super(MentorManager, self).get_queryset().filter(
			type_of='Mentor')

class JudgeManager(models.Manager):
	def get_queryset(self):
		return super(JudgeManager, self).get_queryset().filter(
			type_of='Judge')

class SpeakerManager(models.Manager):
	def get_queryset(self):
		return super(SpeakerManager, self).get_queryset().filter(
			type_of='Speaker')

class NetworkerManager(models.Manager):
	def get_queryset(self):
		return super(NetworkerManager, self).get_queryset().filter(
			type_of='Networker')