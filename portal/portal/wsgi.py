"""
WSGI config for portal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='/Users/Alvin/Development/Web/live-portal/portal/static')
application.add_files('/Users/Alvin/Development/Web/live-portal/portal/static', prefix='static/')