# django modules
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler403, handler404
# views
from contacts.views import LIVETeamListView
from notifications.views import mainView

urlpatterns = [
	path('', mainView, name='index'),
	path('account/', include('users.urls')),
	path('corporate/', include('corporate.urls')),
	path('rounds/', include('rounds.urls')),
	path('questions/', include('qanda.urls')),
	path('itinerary/', include('itenirary.urls')),
	path('live-team', LIVETeamListView.as_view(), name='contact'),
	path('credits',
		TemplateView.as_view(template_name="static/credits.html"),
		name='credits'),
	path('tos',
		TemplateView.as_view(template_name="static/terms_of_service.html"),
		name='terms_of_service'),
	path('privacy',
		TemplateView.as_view(template_name="static/privacy_policy.html"),
		name='privacy_policy'),
	path('executive/', admin.site.urls, name='admin'),
	path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
	handler403 = 'portal.views.forbidden'
	handler404 = 'portal.views.page_not_found'