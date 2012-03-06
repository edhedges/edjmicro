### settings ###
import os
from django.conf import settings

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

if not settings.configured:
    settings.configure(
        DEBUG = True,
        ROOT_URLCONF = 'urls',
        TEMPLATE_DIRS = (
            os.path.join(PROJECT_ROOT, 'templates/'),   
        ),
)