"""
WSGI config for Portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

Portfolio = os.path.expanduser('/Portfolio')  # adjust as appropriate
load_dotenv(os.path.join(Portfolio, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')

application = get_wsgi_application()
app = application


# """
# WSGI config for main project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
# """

# import os
# import sys

# from django.core.wsgi import get_wsgi_application
# sys.path.append('/var/www/public_html/')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')

# application = get_wsgi_application()
# app = application