#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


def prepare_data_directory():
    base = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(os.path.join(base, 'cache'), exist_ok=True)
    os.makedirs(os.path.join(base, 'logs'), exist_ok=True)
    os.makedirs(os.path.join(base, 'media'), exist_ok=True)
    os.makedirs(os.path.join(base, 'sqlite3'), exist_ok=True)
    os.makedirs(os.path.join(base, 'static'), exist_ok=True)
    os.makedirs(os.path.join(base, 'postgres'), exist_ok=True)


def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    dotenv_path and load_dotenv(dotenv_path)
    prepare_data_directory()

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'race_condition_playground.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
