# django modules
from django.db import models
# helpers
import datetime

class PortalWidget(models.Model):
	"""A portal widget is a group of information that is shown to
	either delegate or partners when they first enter the portal. The order of
	the widget will be displayed based off when the widget was created.
	"""

	title = models.CharField("title", max_length=100)

	show_title = models.BooleanField(default=True,
		help_text="Let the widget title be seen publicly.")

	show_delegate = models.BooleanField(default=False)

	show_partner = models.BooleanField(default=False)

	pinned = models.BooleanField(default=False,
		help_text="Pin this at the top of the portal.")

	external_link = models.URLField("external link",
		blank=True,
		help_text="Add a link to an external source. Entire widget will be " +
		"clickable.")

	class Meta:
		verbose_name = "portal widget"

	def __str__(self):
		"""Returns just the title."""
		return self.title

class ImageWidget(models.Model):
	"""Holds an image in a portal widget."""

	widget = models.OneToOneField(PortalWidget,
		on_delete=models.CASCADE,
		related_name="image_widget")

	image = models.ImageField("image",
		upload_to="notifications/widget/",
		help_text="Display an image in the widget.<br/><strong>Recommended " +
		"that you have an image with large dimensions so it can be " +
		"stretched based off user's screen.</strong>")
	
	class Meta:
		verbose_name = "portal image widget"

	def __str__(self):
		return self.widget.title

class TextWidget(models.Model):
	"""Holds a piece of text in a portal widget."""

	widget = models.OneToOneField(PortalWidget,
		on_delete=models.CASCADE,
		related_name="text_widget")

	text = models.TextField("text",
		help_text="Display a piece of text in the widget.")
	
	class Meta:
		verbose_name = "portal text widget"

	def __str__(self):
		"""Returns just the widget title"""
		return self.widget.title

class TextNotification(models.Model):
	"""Holds texts sent to delegates."""

	default = "Text at {}".format(datetime.datetime.now())

	title = models.CharField("title", max_length=100, default=default)

	message = models.TextField("message",
		help_text="Display a piece of text in the widget.")

	send = models.BooleanField("send now",
		default=False,
		help_text="If True, message will be sent after submitting this form.")

	sent = models.BooleanField("sent",
		default=False,
		help_text="If True, message has been sent to all delegates.")

	sent_time = models.DateTimeField("time message sent",
		null=True,
		blank=True)

	def __str__(self):
		return self.title