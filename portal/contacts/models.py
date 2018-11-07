from django.db import models

POSITIONS = [
		(1, 'President'),
		(2, 'Vice President of Corporate Relations'),
		(3, 'Corporate Relations Manager'),
		(4, 'Vice President of Operations'),
		(5, 'Delegate Experience Manager'),
		(6, 'Vice President of Curriculum'),
		(7, 'Curriculum Manager'),
		(8, 'Vice President of Business Intelligence'),
		(9, 'Business Analyst'),
		(10, 'Vice President of Marketing'),
		(11, 'Marketing Manager'),
		(12, 'External Relations Manager'),
		(13, 'Information Technology Solutions Manager'),
		(14, 'Board Member')
]

class Contact(models.Model):

	position_title = models.IntegerField('position',
		choices=POSITIONS)
	
	show_delegates = models.BooleanField('viewable to delegates',
		default=False)

	show_partners = models.BooleanField('viewable to partners',
		default=False)

	full_name = models.CharField('full name',
		max_length=150)

	profile_picture = models.ImageField('profile picture',
		help_text="Please upload a 50x50 square ratio image.")

	description = models.TextField('description',
		help_text="i.e. Responsible for overseeing all logistical operations on the day of.",
		blank=True)

	email_address = models.EmailField('email address')

	linkedin = models.URLField('linkedin account',
		help_text="i.e. https://www.linkedin.com/in/alvintangz/")

	def __str__(self):
		return '{}'.format(self.full_name)