"""
WSGI config for Newwor1d project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
import traceback
from django.core.wsgi import get_wsgi_application


   # Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Newwor1d.settings')

# Get the WSGI application for the Django project.
application = get_wsgi_application()
#app = application
#handler = application