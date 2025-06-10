#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from repo.settings import TEMPLATES


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

# 修改模板查找路径
TEMPLATES[0]['DIRS'] = [
    resource_path('django/contrib/admin/templates'),
    resource_path('import_export/templates'),
    resource_path('templates')
]
if __name__ == '__main__':
    main()
