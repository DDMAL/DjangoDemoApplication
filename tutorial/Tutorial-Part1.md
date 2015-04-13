# Introduction

This tutorial will provide you with a comprehensive overview on how to build a RESTful Django web application. Along the way you will learn the following tools and concepts:

 * How to create and work with Python virtual environments
 * How to create and work with the Django web application system
 * Model-View-Controller
 * Representation State Transfer (REST)
 * HTTP Headers, and Web API-based requests
 * Asynchronous JavaScript communication (AJAX)
 * How to set up and maintain a Solr installation
 * Notification centres, and Django Signals
 * Automatic indexing and searching with Solr and Django

By the end of this tutorial you should be able to understand how all of these components may fit together to form a complete, but simple, web application.

# Conventions and Assumptions

Commands to be typed in the terminal will be indicated by a monospaced font. Some commands may show the `$>` shell prompt. You should type everything that follows this prompt, but not the prompt itself.

Source code is given in `monospaced fonts`. 

# Getting Started

## Tools

### Python

For this tutorial we will be using Python 3.4. With the Homebrew package manager it's very easy to install this and run it alongside your Python 2.7 installations. To install Python 3.4 with Homebrew:

    $> brew install python3

After this has been installed you should be able to run `python3` and get a prompt:

    Python 3.4.2 (default, Oct 19 2014, 17:55:38)
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.54)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

A quick note about Python 3: There are quite a few changes in Python 3, but by the biggest one (that will probably bite you in older code) is that the `print` command has been changed from a statement (e.g., `print "Hello World"`) to a function (e.g., `print("Hello World")`).

### Browser tools

Google Chrome is a very good browser to develop websites with. It has a very easy-to-use debugger, and there are several useful extensions that we can install to make development easier. For ease of use, I would suggest working with Chrome, along with a couple valuable extensions:

`JSON View` is an extension that formats JavaScript Object Notation (JSON) responses in a nice, human-readable form.

`Dev HTTP Client` is an extension that provides a client for interacting with a web server.

You should install both of these in your Chrome installation.

## Create your project directory

Create a directory where you will keep your files for this project. I have called mine "DjangoDemoApplication" -- you can call yours whatever you like.

`cd` to this directory.

## Install your environment

We will be using `virtualenv` to manage our Python installation. `Virtualenv` keeps your main Python installation separate from installations for dedicated projects. This allows you to run and maintain separate modules for each project.

First, install virtualenv. Remember to call `pip3` instead of just `pip` to install the Python 3 version of virtualenv.

    $> pip3 install virtualenv

Now create a virtual environment:

    $> virtualenv-3.4 app_env

This will create a directory in your project directory called `app_env`. This directory will hold any Python modules you install. Every time you want to work on your project you will need to first activate this environment:

    $> source app_env/bin/activate

You will notice that your prompt now changes to include the name of your active environment:

    (app_env)$>

While you are in an active environment, any Python modules you install will be local to this project only.

> Note that because we're in a virtual environment, all of the "regular"
> Python commands are available to you as Python 3 modules: `pip3` is now
> just `pip`, and `python3` is now just `python`.

### Install required modules

We will start by installing some required modules (you must have your virtual environment active):

1. Django:  `$> pip install Django`
2. Django Rest Framework: `$> pip install djangorestframework`
3. Scorched (Solr library): `$> pip install scorched`
4. ipython: `$> pip install ipython`
5. Django Extensions `$> pip install django_extensions`

`ipython` is a replacement interpreter for Python that makes it easier to work with Python on the command line.

> A handy command to remember is `pip freeze`. This command will print
> all of the currently installed modules in your virtual environment. Later
> we will see how `pip freeze > requirements.txt` will produce a file that 
> can be used to automatically install your exact Python environment on another machine!

## Create your Django project

For the purposes of this example, we will be creating a simple code snippet web application. We'll call it "CodeKeeper".

We will start by creating the Django application:

`$> django-admin startproject codekeeper`

This will create a folder called 'codekeeper' with a number of files in it. I prefer a particular type of Django project layout to make it easier to keep track of the different files we'll need, so we will need to re-arrange the files that are created by default.

Start by opening up your project in your file manager. You should see a "codekeeper" folder, and within that folder another "codekeeper" folder with four files in it: `__init__.py`, `settings.py`, `urls.py` and `wsgi.py`. We will start by moving these files out of the sub-folder and into the first "codekeeper" folder. Delete the second "codekeeper" folder.

Now you should have just one "codekeeper" folder, with five files in it -- the four previously mentioned, and `manage.py`. Move `manage.py` up one folder in your hierarchy.

In `wsgi.py` you will need to change one line. Look for this line:

`os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codekeeper.settings")`

and change it to this:

`os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")`

In your `codekeeper` folder, create the following new sub-folders: views, models, static, templates, serializers, and renderers. In admin, views, models, serializers, and renderers, create an empty `__init__.py` file.

> The `__init__.py` file is a special file that allows Python to use a folder 
> as a module name. When writing your application you will typically start by 
> importing methods from other files, typically something like:
> `from codekeeper.views import someview`.
> This command will look in the folders `codekeeper/views` for a file, `someview.py`
> and import this file, making the classes and functions in it available.

You should now have something that looks like this:

![Figure 1](figures/figure1.png)

Finally, we'll need to add our project and modules to our `INSTALLED_APPS` section of `settings.py`. Open this file and add `codekeeper` to the end of the `INSTALLED_APPS` list. While you're there, also add `django_extensions` and `rest_framework` to the list, remembering to put a comma after each item of this list.

You should now be able to run `python manage.py` and have it execute without errors. You should now be ready to build your application.