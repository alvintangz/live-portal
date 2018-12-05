# django modules
from django.db import models
# helpers
from portal.functions import resize_and_convert
# constants
from .constants.live_positions import LIVE_POSITIONS

class Contact(models.Model):

	position_title = models.IntegerField('position',
		choices=LIVE_POSITIONS)
	
	show_delegates = models.BooleanField('viewable to delegates',
		default=True)

	show_partners = models.BooleanField('viewable to partners',
		default=True,
		help_text="Recommended. Displays in a section about the LIVE team.")

	full_name = models.CharField('full name',
		max_length=150)

	profile_picture = models.ImageField('profile picture',
		help_text="Please upload a 500x500 square ratio image.")

	description = models.TextField('description',
		max_length=100,
		help_text=("i.e. Responsible for overseeing all logistical " +
			"operations on the day of. " +
			"To be seen by both delegates and partners."))

	email_address = models.EmailField('email address')

	linkedin = models.URLField('linkedin account',
		help_text="i.e. https://www.linkedin.com/in/alvintangz/")

	resume = models.FileField('resume',
		help_text="visible only to partners")

	class Meta:
		ordering = ['position_title']

	def get_position_title(self):
		for number, position in LIVE_POSITIONS:
			if number == self.position_title:
				return position

	def __str__(self):
		return '{}'.format(self.full_name)

	def save(self):
		"""Resize profile picture before being saved."""
		super(Contact, self).save()
		if self.profile_picture:
			resize_and_convert(self.profile_picture).save(
				self.profile_picture.path)