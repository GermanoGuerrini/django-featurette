===============
Getting Started
===============

Installation
=============

Use your favorite Python package manager to install the app from PyPI, e.g.

Example::

    pip install django_featurette


Configuration
=============

Add ``django_featurette`` to the ``INSTALLED_APPS`` within your settings file
(usually ``settings.py``).

Example::

    INSTALLED_APPS = [
        [...]
        'django_featurette',
    ]

After that, run the ``syncdb`` command, or ``migrate`` if you are using Django 1.7::

    ./manage.py syncdb

As Featurette rely on built-in Django authentication system, you will need to add
all the needed applications and middleware.
Head to the `official documentation <https://docs.djangoproject.com/en/1.7/topics/auth/>`_ if you need help.
