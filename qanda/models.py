# django modules
from django.db import models
from django.urls import reverse_lazy
# models
from users.models import User
# managers
from .managers import AnswerManager
# helpers
from portal.functions import default_shortstrftime, send_email
import datetime
# constants
import portal.variables as imp

# Create your models here.
class Question(models.Model):

	question = models.CharField('question',
		max_length=200,
		help_text="Required. Maximum question length of 200 characters.")

	by = models.ForeignKey(
		User,
		models.SET_NULL,
		null=True,
		related_name="by")

	by_anonymous = models.BooleanField('asker is anonymous to others',
		default=False,
		help_text=("Optional. Be anonymous to your peers when the answer " +
			"to your question is posted publicly."))

	created = models.DateTimeField('created on',
		editable=False)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		if hasattr(self, 'answer'):
			return "%s Question: %s" % ("Answered", 
				self.shorten_question())
		return "%s Question: %s" % ("Unanswered", 
			self.shorten_question())

	def shorten_question(self, shorten=37):
		if len(self.question) > shorten+3:
			return self.question[:shorten] + "..."
		return self.question

	def by_name(self):
		if self.by:
			return self.by.get_full_name()
		return "N/A"

	def formatted_created(self):
		return default_shortstrftime(self.created)

	def save(self):
		if not self.id:
			self.created = datetime.datetime.now()
		return super(Question, self).save()

	shorten_question.short_description = "Question"
	by_name.short_description = "Raised by"
	formatted_created.short_description = "Asked on"

class Answer(models.Model):

	question = models.OneToOneField(
		Question,
		models.CASCADE,
		related_name="answer")

	answer = models.TextField('answer',
		help_text=(
			"Feel free to correct the related question for any mistakes " +
			"such as spelling mistakes.<br/>After submitting an answer " +
			"to the question for the first time, an email will automatically " +
			"be sent to the person who raised the question."))

	faq = models.BooleanField('is frequently asked',
		default=False,
		help_text=("If True, the answer and its associated question " +
			"will be appended to a special FAQ section."))

	updated = models.DateTimeField('last updated',
		editable=False)

	objects = AnswerManager()

	class Meta:
		verbose_name = "public answer"
		verbose_name_plural = "public answers"
		ordering = ['-updated', '-question__created']

	def formatted_updated(self):
		return default_shortstrftime(self.updated)

	def shorten_answer(self, shorten=37):
		if len(self.answer) > shorten+3:
			return self.answer[:shorten] + "..."
		return self.answer

	def asc_question(self):
		return self.question.shorten_question()

	def viewable_meta(self):
		metastr = "Asked by %s at %s | Last updated at %s"
		if not self.question.by_anonymous:
			if self.question.by.is_superuser:
				return metastr % ("a LIVE Executive",
					self.question.formatted_created(),
					self.formatted_updated())
			else:
				return metastr % (self.question.by.get_full_name(),
					self.question.formatted_created(),
					self.formatted_updated())
		return metastr % ("an Anonymous User",
			self.question.formatted_created(),
			self.formatted_updated())

	def save(self):
		self.updated = datetime.datetime.now()
		if ((not self.id) and self.question.by.email
			and not self.question.by.is_superuser):
			send_email(
				subject="Your Question Answered: %s" % (
					self.question.shorten_question()),
				receiver=self.question.by.email,
				html_message=(("<p>Hello <strong>%s</strong>,</p>" +
					"<p>At %s, you asked us this question: <em>%s</em></p>" +
					"<p>We have recently answered! The answer to your " +
					"question is:<br/><em>%s</em></p><p>This question and " +
					"its answer was posted on the <a href=\"%s\">"+
					"Questions and Answers</a> section of Portal as of %s.</p>")
					% (self.question.by.get_full_name(),
						self.question.formatted_created(),
						self.question.question,
						self.answer,
						imp.urls["portal"],
						self.formatted_updated())),
				message=(("Hello %s! " +
					"At %s, you asked us this question: %s " +
					"We have recently answered and the answer is: %s "
					"This question and its answer was posted on the Questions" +
					" and Answers section of Portal as of %s.")
					% (self.question.by.get_full_name(),
						self.question.formatted_created(),
						self.question.question,
						self.answer,
						self.formatted_updated())),
			)
		return super(Answer, self).save()

	shorten_answer.short_description = "Answer"
	asc_question.short_description = "Question"
	formatted_updated.short_description = "Last Updated"