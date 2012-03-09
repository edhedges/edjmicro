### settings ###
import socket, os
from django.conf import settings

def contains(str, substr):
    if str.find(substr) != -1:
        return True
    else:
        return False

if contains(socket.gethostname(), 'webfaction'):
    LIVEHOST = True
else:
    LIVEHOST = False

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

if not settings.configured:
    if LIVEHOST:
        settings.configure(
            DEBUG = True,
            
            ROOT_URLCONF = 'urls',
            TEMPLATE_DIRS = (
                os.path.join(PROJECT_ROOT, 'templates/'),   
            ),
            STATIC_ROOT = '/home/edhedges/webapps/static/PROJECT_ID/',
            STATIC_URL = 'http://www.edhedges.com/static/PROJECT_ID/',
            INSTALLED_APPS = (
                'django.contrib.staticfiles',
                #uncomment to use fabric
                #'fabric',        	
            ),
        )
    if not LIVEHOST:
        settings.configure(
            DEBUG = True,
            
            ROOT_URLCONF = 'urls',
            TEMPLATE_DIRS = (
                os.path.join(PROJECT_ROOT, 'templates/'),   
            ),
            STATIC_ROOT = '/static/',
            STATIC_URL = '/static/',
            STATICFILES_DIRS = (
                os.path.join(PROJECT_ROOT, 'static/'),
            ),
            INSTALLED_APPS = (
                'django.contrib.staticfiles',
                #uncomment to use fabric
                #'fabric',          
            ),
        )
