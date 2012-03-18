## edjmicro - A simple boilerplate for using django as a micro framework ##

Inspiration comes from [here](http://softwaremaniacs.org/blog/2011/01/07/django-micro-framework/en/) and structure comes from my origin boilerplate [here](https://github.com/edhedges/eds-djangoplate).

Requirements to be able to start a project:

* [virtualenv](http://www.virtualenv.org/en/latest/index.html) 
* [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
* [git](http://git-scm.com/)
* [pip](http://www.pip-installer.org/en/latest/index.html) - Automatically installed with virtualenv

If the requirements have been met add a bash function to either your `.bash-profile` or `.bashrc`. I named my function `mkdjmicroproj` which runs all the commands necessary to start the project. Here it is:

	mkdjmicroproj () {
		mkproject --no-site-packages --promp=$1: $1 &&
		git init &&
		git pull git@github.com:edhedges/edjmicro.git master &&
		rm README.md &&
		pip install -r conf/requirements.txt &&
		chmod +x manage.py
		./manage.py runserver
	}

The goal of this project is to make a very functional django boilerplate while keeping it as lightweight as possible.