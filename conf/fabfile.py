### fabfile ###
from fabric.api import *
from project import *

## web host and root access user info ##
env.hosts = ['%s.webfactional.com' % ROOT_USER_NAME]
env.user = ROOT_USER_NAME
env.password = ROOT_USER_PASSWORD

## home, webapps, and python path tailored for webfaction ##
env.home_dir = '/home/%s' % ROOT_USER_NAME
env.webapps_dir = env.home_dir + '/webapps'
env.host_python_dir = env.home_dir + '/lib/python2.7'

## pyprojects and static directories ##
env.projects_dir = env.webapps_dir + '/pyproject'
env.static_dir = env.webapps_dir + '/static/%s' % PROJECT_ID

## apache2 bin and conf, virtualenv, and current project directories  ##
env.apache_bin_dir = env.projects_dir + '/apache2/bin'
env.apache_conf_dir = env.projects_dir + '/apache2/conf'
env.virtualenv_dir = env.projects_dir + '/virtualenvs'
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
    Installs requirements via pip, syncs the local db, migrates any changes to db via south, and runs local server
    """
    local('pip install -r conf/requirements.txt')
    ## The following two commands are optional if using database which, is not assumed with edjmicro ##
    #local('python manage.py syncdb')
    #local('python manage.py migrate')
    local('python manage.py runserver')

def run_local_smtp():
    """
    Runs a local smtp server
    """
    local('python -m smtpd -n -c DebuggingServer localhost:1025')

def replace_httpdconf():
    """
    Replaces httpd.conf file given by webfaction.
    """
    with cd(env.apache_conf_dir):
        run('rm httpd.conf')
    with cd(env.current_project_dir + '/conf'):
        run('cp httpd.conf %s' % env.apache_conf_dir)
    with cd(env.apache_bin_dir):
        run('./restart')

def initial_setup():
    """
    Sets up webfaction host with python 2.7 and other dependencies
    """
    run('mkdir -p %s' % env.host_python_dir)
    run('easy_install-2.7 pip')
    run('pip-2.7 install virtualenv')
    run('pip-2.7 install virtualenvwrapper')
    run('mkdir -p %s' % env.virtualenv_dir)
    run('mkdir -p %s' % env.static_dir)

def deploy():
    """
    Deploys the project to webfaction
    """
    run('mkproject %s' % PROJECT_ID)
    run('mkdir %s' % env.static_dir)
    with cd(env.current_project_dir):
        run('git init')
        run('git pull https://edhedges@github.com/edhedges/%s.git master' % PROJECT_ID)
        run('pip-2.7 install -r conf/requirements.txt')
        run('python2.7 manage.py new_secret')
        run('python2.7 manage.py syncdb')
        run('python2.7 manage.py migrate')
        run('mv static/* %s' % env.static_dir)
        run('rm -rf static')
        run('python2.7 manage.py collectstatic')
    replace_httpdconf()

def destroy_all():
    """
    Destroys what is made in initial_setup() as well as the django project     
    """
    run('rm -rf %s' % env.host_python_dir)
    run('rm -rf %s' % env.virtualenv_dir)
    destroy_project()

def destroy_project():
    """
    Destroys the project
    """
    run('rm -rf %s' % env.current_project_dir)
    run('rm -rf %s' % env.specific_virtualenv_dir)
    run('rm -rf %s' % env.static_dir)

def rebuild_all():
    """
    Runs destroy_all(), set_up(), and deploy()
    """
    destroy_all()
    set_up()
    deployt()

def rebuild_project():
    """
    Runs destroy_project() and deploy()
    """
    destroy_project()
    deploy()

def restart_apache():
   """
   Restarts the apache2 isntance
   """
   run(env.apache_bin_dir + '/restart')
