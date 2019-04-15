#!/usr/bin/env python
'''manage.py это утилита для запуска различных команд внутри проекта.
На самом деле это просто оболочка вокруг того же django-admin, но которая уже знает всё про ваш проект'''
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
