from django.db import models

class CorporateOrganization(models.Model):

	name = models.CharField('name',
		max_length=150)

	description = models.TextField('description',
		null=True,
		blank=True)

	logo = models.ImageField('logo',
		null=True,
		blank=True,
		help_text="<strong>It is highly recommended that a logo should be uploaded if they are a partner.</strong>")

	partner = models.BooleanField('is a partner',
		default=False,
		help_text="If true, this organization will be viewable to delegates.")

	partner_type = models.CharField('partner type',
		blank=True,
		max_length=50,
		help_text="Leave blank if organization is not a partner. This is viewable to delegates if organization is a partner. <br/>i.e. Title Partner")

	class Meta:
		verbose_name = "corporate organization"

	def __str__(self):
		return self.name

class CorporateIndividual(models.Model):

	organization = models.ForeignKey(CorporateOrganization,
		on_delete=models.SET_NULL,
		null=True)

	full_name = models.CharField('full name',
		max_length=150)

	profile_picture = models.ImageField('picture',
		help_text="Please upload a 50x50 square ratio image.",
		null=True,
		blank=True)

	biography = models.TextField('biography',
		help_text="Recommended to keep it short",
		blank=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.full_name + " of " + self.organization.name

class Mentor(CorporateIndividual):
	pass

class Judge(CorporateIndividual):
	pass

class Speaker(CorporateIndividual):
	pass

class Networker(CorporateIndividual):
	pass