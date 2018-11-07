import uuid
from django.db import models
from users.models import Team

class Round(models.Model):
	
	uuid = models.UUIDField(
		'unique identifier',
		default=uuid.uuid4,
		editable=False,
		unique=True)

	active = models.BooleanField('active',
		default=False)

	title = models.CharField('title',
		max_length=200)

	description = models.TextField('description',
		blank=True)

	associated_file = models.FileField('associated file')

	expected_deadline = models.DateTimeField('expected deadline')

	show_deadline = models.BooleanField('show deadline publicly',
		default=False)

	deactive_deadline = models.BooleanField('deactive at deadline',
		default=False)

class Submission(models.Model):

	asc_team = models.ForeignKey(Team,
		on_delete=models.SET_NULL,
		null=True)

	asc_round = models.ForeignKey(Round,
		on_delete=models.SET_NULL,
		null=True)

	latest = models.BooleanField(default=True)

	next_sub = models.IntegerField('identification of the next submission',
		null=True)

	prev_sub = models.IntegerField('identification of the previous submission',
		null=True)

	expected_deadline = models.DateTimeField('date and time of submission')