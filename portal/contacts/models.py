from django.db import models

POSITIONS = [
		(1, 'President'),
		(2, 'VP of Corporate Relations'),
		(3, 'Corporate Relations Manager'),
		(4, 'VP of Operations'),
		(5, 'Delegate Experience Manager'),
		(6, 'VP of Curriculum'),
		(7, 'Curriculum Manager'),
		(8, 'VP of Business Intelligence'),
		(9, 'Business Analyst'),
		(10, 'VP of Marketing'),
		(11, 'Marketing Manager'),
		(12, 'External Relations Manager'),
		(13, 'IT Solutions Manager'),
		(14, 'Board Member')
]

class Contact(models.Model):

	position_title = models.IntegerField('position',
		choices=POSITIONS)
	
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

	def get_position_title(self):
		for number, position in POSITIONS:
			if number == self.position_title:
				return position

	def __str__(self):
		return '{}'.format(self.full_name)

	class Meta:
		ordering = ['position_title']