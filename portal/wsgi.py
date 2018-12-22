"""
WSGI config for portal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')

os.environ['LP_AZURE_STORAGE_KEY'] = 'PA4c7t/0sCEdPElAyz6TkyDXqOGWaCZnXd9kPu7GJ65leJXNZRuSZ2nM3zwN9UPcfs0aZbFpEJzAGwrDfEz99w=='
os.environ['LP_DB_HOST'] = 'live-portal.database.windows.net'
os.environ['LP_DB_NAME'] = 'live-portal'
os.environ['LP_DB_PASSWORD'] = 'arELee59x9'
os.environ['LP_DB_PORT'] = '1433'
os.environ['LP_DB_USER'] = 'alvintang@live-portal'
os.environ['LP_EMAIL_HOST'] = 'smtp.sendgrid.net'
os.environ['LP_EMAIL_PASSWORD'] = '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'
os.environ['LP_EMAIL_PORT'] = '587'
os.environ['LP_TWILIO_NUMBER'] = '+16479515718'
os.environ['LP_TWILIO_SID'] = 'AC1f3ababace34b895c68707c32ac74315'
os.environ['LP_TWILIO_TOKEN'] = '714e479cde7ff140367e7a857082845b'

application = get_wsgi_application()
