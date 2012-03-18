### settings ###
import socket, os
from conf.project import PROJECT_ID

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

## Global settings ###
ROOT_URLCONF = 'urls'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),   
)
SECRET_KEY = ''
INSTALLED_APPS = (
        'django.contrib.staticfiles',
        #'fabric',
        'apps.new_secret',   
)

## Settings used when running live on WebFaction ##
if LIVEHOST:
    DEBUG = False
    STATIC_ROOT = '/home/edhedges/webapps/static/PROJECT_ID/'
    STATIC_URL = 'http://www.edhedges.com/static/PROJECT_ID/'

## Settings used locally for development ##
if not LIVEHOST:
    DEBUG = True
    STATIC_ROOT = '/static/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static/'),
    )