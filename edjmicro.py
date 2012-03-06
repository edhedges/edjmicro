### settings ###
import os
from django.conf import settings

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

if not settings.configured:
    settings.configure(
        DEBUG = True,
        ROOT_URLCONF = 'edjmicro',
        TEMPLATE_DIRS = (
            os.path.join(PROJECT_ROOT, 'templates/'),   
        ),
)

### views ###
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

### urls ###
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^$', 'views.index'),
)

### Running ###
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line()