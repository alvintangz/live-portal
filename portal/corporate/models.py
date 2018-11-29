# django modules
from django.db import models
from django.db.models.query import QuerySet
# constants
from .constants.corporate_individual_types import CORPORTATE_INDIVIDUAL_TYPES
from .constants.partner_types import PARTNER_TYPES
# helpers
from portal.functions import resize_and_convert
import math
# managers
from .managers import (
	CorporateIndividualManager,
	MentorManager,
	JudgeManager,
	SpeakerManager,
	NetworkerManager
)

class CorporateOrganization(models.Model):

	name = models.CharField('name',
		max_length=40)

	description = models.TextField('description',
		blank=True,
		help_text="Optional.")

	logo = models.ImageField('logo',
		null=True,
		blank=True,
		help_text=("<strong>It is highly recommended that a logo should be " +
			"uploaded if they are a partner.</strong>"))

	partner = models.BooleanField('is a partner',
		default=False,
		help_text="If true, this organization will be viewable to delegates.")

	partner_type = models.SmallIntegerField('partner type',
		blank=True,
		max_length=60,
		choices=PARTNER_TYPES,
		help_text=("Leave blank if organization is not a partner. " +
			"This is viewable to delegates if organization is a partner. " +
			"As well, this will determine the ordering when partners listed." +
			"<br/>i.e. Title Partner"))

	class Meta:
		verbose_name = "corporate organization"
		ordering = ['partner_type']

	def get_partner_type(self):
		for number, partner_type in PARTNER_TYPES:
			if number == self.partner_type:
				return partner_type

	def __str__(self):
		return self.name

class CorporateIndividual(models.Model):

	type_of = models.CharField('type of individual',
		choices=CORPORTATE_INDIVIDUAL_TYPES,
		max_length=10)

	organization = models.ForeignKey(CorporateOrganization,
		on_delete=models.CASCADE,
		related_name="individuals")

	position_org = models.CharField('position in their organization',
		max_length=100)

	full_name = models.CharField('full name',
		max_length=70)

	profile_picture = models.ImageField('picture',
		null=True,
		blank=True,
		help_text=("For best results, upload a 500px by 500px RGB picture. " +
			"It will be resized and formatted automatically to that anyway."))

	biography = models.TextField('biography',
		blank=True,
		help_text="Recommended to keep this short.")

	email = models.EmailField('Email',
		blank=True,
		help_text="Optional.")

	linkedin = models.URLField('linkedin',
		blank=True,
		help_text="Optional.")

	order = models.PositiveSmallIntegerField('order for listing',
		help_text=("Order an individual for when they are listed. " +
			"i.e. If Bob has 1 for order of listing and Alice has 2 for order" +
			" of listing, then Bob will be shown before Alice when listed."))

	objects = CorporateIndividualManager()

	class Meta:
		ordering = ['order']

	def get_page(self, pagination=10):
		counter = 1
		for each in CorporateIndividual.objects.filter(type_of=self.type_of):
			if each == self:
				return str(math.trunc(counter / pagination) + 1)
			counter += 1
		return str(1)

	def html_id(self):
		return "%spk%s" % (
			self.organization.name.lower().replace(" ", ""),
			str(self.id))

	def save(self):
		super(CorporateIndividual, self).save()
		if self.profile_picture:
			resize_and_convert(self.profile_picture).save(
				self.profile_picture.path)

	def __str__(self):
		return "%s of %s" % (
			self.full_name,
			self.organization.name)

class Mentor(CorporateIndividual):
	objects = MentorManager()

	class Meta:
		proxy = True

class Judge(CorporateIndividual):
	objects = JudgeManager()

	class Meta:
		proxy = True

class Speaker(CorporateIndividual):
	objects = SpeakerManager()

	class Meta:
		proxy = True

class Networker(CorporateIndividual):
	objects = NetworkerManager()

	class Meta:
		proxy = True