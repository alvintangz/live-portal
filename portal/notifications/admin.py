from django.contrib import admin
from .models import PortalWidget, ImageWidget, TextWidget

# IMAGE WIDGETS

# The inline group for image widgets
class ImageWidgetInline(admin.StackedInline):
	model = ImageWidget

# The proxy for portal widget, acting as a model of portal widget
class ImageWidgetProxy(PortalWidget):
	class Meta:
		proxy = True
		verbose_name = "image widget"

# Where the magic begins, add the fields in ImageWidget on top of PortalWidget
@admin.register(ImageWidgetProxy)
class ImageWidgetProxyAdmin(admin.ModelAdmin):
	list_display = ('title', 'show_partner', 'show_delegate', 'pinned')
	inlines = [ImageWidgetInline]

	def get_queryset(self, request):
		# Only get queryset with an attribute of ImageWidget and order by if pinned, then by when widget was created
		return PortalWidget.objects.filter(image_widget__pk__isnull=False).order_by('-pinned', '-pk')

# TEXT WIDGETS

# The inline group for text widgets
class TextWidgetInline(admin.StackedInline):
	model = TextWidget

# The proxy for portal widget, acting as a model of portal widget
class TextWidgetProxy(PortalWidget):
	class Meta:
		proxy = True
		verbose_name = "text widget"

# Where the magic begins, add the fields in TextWidget on top of PortalWidget
@admin.register(TextWidgetProxy)
class TextWidgetProxyAdmin(admin.ModelAdmin):
	list_display = ('title', 'show_partner', 'show_delegate', 'pinned')
	inlines = [TextWidgetInline]

	def get_queryset(self, request):
		# Only get queryset with an attribute of TextWidget and order by if pinned, then by when widget was created
		return PortalWidget.objects.filter(text_widget__pk__isnull=False).order_by('-pinned', '-pk')

# TBD: TEXT NOTIFICATIONS