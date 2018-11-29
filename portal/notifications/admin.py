from django.contrib import admin
from .models import PortalWidget, ImageWidget, TextWidget, TextNotification
import portal.variables as imp
from portal.functions import send_sms
from users.models import Delegate
import datetime

# IMAGE WIDGETS

class ImageWidgetInline(admin.StackedInline):
	"""Inline group for image widgets."""
	model = ImageWidget

class ImageWidgetProxy(PortalWidget):
	"""Proxy for portal widget, acting as a model of portal widget."""
	class Meta:
		proxy = True
		verbose_name = "image widget"

@admin.register(ImageWidgetProxy)
class ImageWidgetProxyAdmin(admin.ModelAdmin):
	"""Add the fields in ImageWidget on top of PortalWidget."""
	list_display = ('title', 'show_partner', 'show_delegate', 'pinned')
	inlines = [ImageWidgetInline]

	def get_queryset(self, request):
		"""Return queryset with an attribute of ImageWidget and order by if
		pinned, then by when widget was created.
		"""
		return PortalWidget.objects.filter(image_widget__pk__isnull=False
			).order_by('-pinned', '-pk')

# TEXT WIDGETS

class TextWidgetInline(admin.StackedInline):
	"""Inline group for text widgets."""
	model = TextWidget

class TextWidgetProxy(PortalWidget):
	"""Proxy for portal widget, acting as a model of portal widget."""
	class Meta:
		proxy = True
		verbose_name = "text widget"

@admin.register(TextWidgetProxy)
class TextWidgetProxyAdmin(admin.ModelAdmin):
	"""Add the fields in TextWidget on top of PortalWidget."""
	list_display = ('title', 'show_partner', 'show_delegate', 'pinned')
	inlines = [TextWidgetInline]

	def get_queryset(self, request):
		"""Return queryset with an attribute of TextWidget and order by
		if pinned, then by when widget was created.
		"""
		return PortalWidget.objects.filter(text_widget__pk__isnull=False
			).order_by('-pinned', '-pk')

# TBD: TEXT NOTIFICATIONS
@admin.register(TextNotification)
class TextNotificationAdmin(admin.ModelAdmin):
	list_display = ('title', 'sent')

	class Meta:
		verbose_name = "Text notifications to all delegates"

	def get_form(self, request, obj=None, **kwargs):
		if obj is None:
			self.exclude = ('sent', 'sent_time')
		else:
			if obj.sent:
				self.exclude = ('send',)
				self.readonly_fields = ["title", "message", "sent", "sent_time"]
			else:
				self.exclude = ('sent', 'sent_time')
		return super(TextNotificationAdmin, self).get_form(request, obj, **kwargs)

	def save_model(self, request, obj, form, change):
		super(TextNotificationAdmin, self).save_model(request, obj, form, change)
		if not obj.sent and obj.send:
			all_delegates = Delegate.objects.all()
			for delegate in all_delegates:
				if delegate.phone_number:
					number = "+1" + delegate.phone_number
					send_sms(number, obj.message)
			obj.sent = True
			obj.sent_time = datetime.datetime.now()
			obj.save()