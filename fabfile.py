### fabfile ###
from fabric.api import *
from project import ROOT_USER_NAME, ROOT_USER_PASSWORD, PROJECT_ID

## web host and root access user info ##
env.hosts = ['%s.webfactional.com' % ROOT_USER_NAME]
env.user = ROOT_USER_NAME
env.password = ROOT_USER_PASSWORD

## home, webapps, and python path tailored for webfaction ##
env.home_dir = '/home/%s' % ROOT_USER_NAME
env.webapps_dir = env.my_dir + '/webapps'
env.host_python_dir = env.my_dir + '/lib/python2.7'

## pyprojects and static directories ##
env.projects_dir = env.webapps_dir + '/pyproject'
env.static_dir = env.webapps_dir + '/static/%s' % PROJECT_ID

## apache2 bin and conf, virtualenv, and current project directories  ##
env.apache_bin_dir = env.projects_dir + '/apache2/bin'
env.apache_conf_dir = env.projects_dir + '/apache2/conf'
env.virtualenv_dir = env.project_dir + '/virtualenvs'
env.current_project_dir = env.projects_dir + '/%s' % PROJECT_ID

## projects virtualenv  ##
env.project_virtualenv_dir = env.virtualenv_dir + '/%s' % PROJECT_ID

## fab functions used to go from local development via command line :) ##
def run_server():
    """
    Runs django's manage.py runserver command
    """
    local('python manage.py runserver')

def run_server_plus():
    """
    Installs requiremetns via pip, syncs the local db, migrates any changes to db via south, and runs local server
    """
    local('pip install -r requirements.txt')
    local('python manage.py syncdb')
    local('python manage.py migrate')
    local('python manage.py runserver')

def run_local_smtp():
    """
    Runs a local smtp server
    """
    local('python -m smtpd -n -c DebuggingServer localhost:1025')
