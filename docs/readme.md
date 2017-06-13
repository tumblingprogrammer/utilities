To learn more about this project, please visit its page on [tumblingprogrammer.com](http://www.tumblingprogrammer.com/setting-up-a-django-project-boilerplate/).

While there, make sure to visit the [conventions page](http://www.tumblingprogrammer.com/conventions-used-on-tumbling-programmer-dot-com/), some of which apply to the instructions below.

Let's dive in.

#### Creating a virtual environment
_____
Let's create a virtual environment, preferably using [virtual environment wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) (you could use a different virtual environment option too); for illustration purposes, let's call it `djangoboilerplate`.  Make sure that it is based on python 3.5 or later.

#### Cloning the repository

Open a terminal session at the location where you intend to clone the repository. There, execute `git clone https://github.com/tumblingprogrammer/djangoboilerplate.git`.

You will get the following output:

	Cloning into 'djangoboilerplate'...
	remote: Counting objects: 174, done.
	remote: Compressing objects: 100% (104/104), done.
	remote: Total 174 (delta 55), reused 167 (delta 48), pack-reused 0
	Receiving objects: 100% (174/174), 22.83 KiB | 0 bytes/s, done.
	Resolving deltas: 100% (55/55), done.

A folder named `djangoboilerplate` will pop up on your chosen location.  Below are its contents.  Note that `git` related files have been omitted for brevity and clarity.

	|____djangoboilerplate
	| |____apps
	| | |____config
	| | | |______init__.py
	| | | |____settings
	| | | | |______init__.py
	| | | | |____base.py
	| | | | |____local.py
	| | | | |____production.py
	| | | |____urls.py
	| | | |____wsgi.py
	| | |____main
	| | | |______init__.py
	| | | |____admin.py
	| | | |____apps.py
	| | | |____migrations
	| | | | |______init__.py
	| | | |____models.py
	| | | |____tests.py
	| | | |____urls.py
	| | | |____views.py
	| | |____manage.py
	| | |____media
	| | | |____twitter48.png
	| | |____static
	| | | |____css
	| | | | |____global.css
	| | | |____img
	| | | | |____twitter48.png
	| | | |____js
	| | | | |____global.js
	| | |____templates
	| | | |____403_csrf.html
	| | | |____404.html
	| | | |____500.html
	| | | |____base.html
	| | | |____main
	| | | | |____home.html
	| |____docs
	| | |____readme.md
	| |____requirements
	| | |____base.txt
	| | |____local.txt
	| | |____production.txt
	| | |____requirements.txt

#### Installing requirements
_____
On the terminal, navigate to `djangoboilerplate/requirements/`.  Make sure that your `djangoboilerplate` virtual environment is active, and run `pip install -r local.txt`. It should go without hiccup.

#### Setting required environment variables
_____
Because of the reasons explained [here](http://www.tumblingprogrammer.com/setting-up-a-django-project-boilerplate/ "tumbling programmer - setting up a django project boilerplate"), you will need to set two environment variables before you can run the application: `DJANGO_EXECUTION_ENVIRONMENT` and `DJANGO_SECRET_KEY`.  [This article](http://www.tumblingprogrammer.com/setting-environment-variables/ "tumbling programmer - setting environment variables") will point you in the right direction as to how to do that.

As laid out [here](http://www.tumblingprogrammer.com/setting-up-a-django-project-boilerplate/ "tumbling programmer - setting up a django project boilerplate"), it is recommended that `DJANGO_EXECUTION_ENVIRONMENT` be set system-wide, and `DJANGO_SECRET_KEY` be limited to the `djangoboilerplate` virtual environment.

The value for the `DJANGO_EXECUTION_ENVIRONMENT` should be `LOCAL`.  To generate a value for your `DJANGO_SECRET_KEY` you can use [this site](http://www.miniwebtool.com/django-secret-key-generator/) or, better yet, program your own python script to do it. 

To verify that setting the environment variables worked, make sure to run `echo $DJANGO_EXECUTION_ENVIRONMENT` and `echo $DJANGO_SECRET_KEY` on the terminal.  You should get `LOCAL` and the secret key that you generated above.  Remember to source your bash profile (e.g. `source ~/.bash_profile`) and deactivate and reactivate your virtual environment before testing your variables. 

#### Testing the boilerplate
_____
Once your variables are set, on your terminal navigate to `djangoboilerplate/apps/` and once there, run `manage.py runserver`. You should be able to see the below screen if you point your browser to `http://127.0.0.1:8000/`.   

From this point on, the sky is the limit :)

![tumbling programmer's django project boilerplate home page](https://www.tumblingprogrammer.com/media/2017/06/django_project_boilerplate.png "tumbling programmer's django project boilerplate home page")