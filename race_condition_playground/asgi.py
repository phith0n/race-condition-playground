"""
ASGI config for race_condition_playground project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from dotenv import load_dotenv

from django.core.asgi import get_asgi_application

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
dotenv_path and load_dotenv(dotenv_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'race_condition_playground.settings')

application = get_asgi_application()
