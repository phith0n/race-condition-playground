"""
WSGI config for race_condition_playground project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
dotenv_path and load_dotenv(dotenv_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'race_condition_playground.settings')

application = get_wsgi_application()
