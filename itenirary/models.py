from django.db import models
from portal.functions import default_strfonlydate, default_strfonlytime
from datetime import datetime

class Day(models.Model):
	"""A day contains multiple events.
	"""

	number = models.SmallIntegerField('number')

	title = models.CharField('title',
		max_length=100,
		help_text='i.e. Finals Day')

	date = models.DateField('date')

	release = models.BooleanField('release the itenirary of the day',
		default=False)

	def get_status(self):
		"""Status of day.
		0 -> Day has not started
		1 -> Day is active
		2 -> Day is finished
		"""
		if self.date > datetime.today().date():
			return 0
		elif self.date == datetime.today().date():
			return 1
		return 2

	def get_formatted_date(self):
		return default_strfonlydate(self.date)

	def __str__(self):
		return f'{self.title} on {default_strfonlydate(self.date)}'

class Event(models.Model):
	"""An event is part of one day.
	"""

	day = models.ForeignKey(Day,
		on_delete=models.CASCADE,
		related_name='day')

	time = models.TimeField('start time',
		help_text="When the event starts.")

	end_time = models.TimeField('end time',
		help_text="When the event ends. Not displayed.")

	title = models.CharField('title',
		max_length=100,
		help_text="i.e. Registration")

	description = models.TextField('description',
		blank=True,
		help_text='Optional.')

	venue_name = models.CharField('venue name',
		max_length=100,
		help_text="i.e. Hyatt Regency Toronto")

	venue_address = models.CharField('venue address',
		max_length=200,
		help_text="i.e. 370 King St W, Toronto, ON M5V 1J9")

	venue_long = models.DecimalField('venue longitude',
		max_digits=9,
		decimal_places=6,
		help_text=("The coordinates of the venue (longitude). Useful in maps." +
		" Can find coordinates using a tool: https://gps-coordinates.org/."))

	venue_lat = models.DecimalField('venue latitude',
		max_digits=9,
		decimal_places=6,
		help_text=("The coordinates of the venue (latitude). Useful in maps. " +
		"Can find coordinates using a tool: https://gps-coordinates.org/."))

	def get_status(self):
		"""Status of event.
		0 -> Event has not started
		1 -> Event is active
		2 -> Event is finished
		"""
		date = self.day.date
		if date > datetime.today().date():
			return 0
		elif date == datetime.today().date():
			if self.time > datetime.today().time():
				return 0
			elif self.end_time < datetime.today().time():
				return 2
			else:
				return 1
		return 2

	def get_formatted_time(self):
		return default_strfonlytime(self.time)
	get_formatted_time.short_description = "Time"

	def __str__(self):
		return f'{self.title} at {self.venue_name} - {default_strfonlytime(self.time)}'