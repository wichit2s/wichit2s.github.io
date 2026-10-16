import os
import sys

path = '/home/yourusername/health_cdss_portal'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'cdss_portal.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
