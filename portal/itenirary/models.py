from django.db import models

class Day(models.Model):

	title = modes.CharField('day title',
		max_length=150,
		help_text='i.e. Finals Day, Stage Two')

	date = models.DateField('date')

	released = models.BooleanField('release the itenirary of the entire day')

	def __str__(self):
		return self.title + " on " + str(self.date.month) + "/" + str(self.date.day) + "/" + str(self.date.year)

class Event(models.Model):

	title = models.CharField('event title',
		max_length=200)

	description = models.TextField('description',
		blank=True)

	day = models.ForeignKey(Day,
		on_delete=models.CASCADE)

	time = models.TimeField('time of event')

	venue = models.CharField('venue')

	coordinates = models.EasyMap

	def get_time(self):
		'''
		Formated in HH:MM AM/PM.
		'''

		am_pm = "AM"
		hour = str(self.time.hour)

		if(self.time.hour > 12) {
			hour = str(self.time.hour-12)
			am_pm = "PM"
		}

		return hour + ":" + str(self.time.minute) + am_pm

	def __str__(self):

		am_pm = "AM"
		hour = str(self.time.hour)

		if(self.time.hour > 12) {
			hour = str(self.time.hour-12)
			am_pm = "PM"
		}

		return self.title + " at " + self.day + " " + self.get_time()