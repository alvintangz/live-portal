from django.db import models

class AnswerManager(models.Manager):
	def is_faq(self):
		return self.filter(faq=True)