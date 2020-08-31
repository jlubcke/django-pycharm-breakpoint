===============================
django-pycharm-breakpoint
===============================

.. image:: https://badge.fury.io/py/django-pycharm-breakpoint.png
    :target: http://badge.fury.io/py/django-pycharm-breakpoint

App for ``Django`` to enter PyCharm debugger on uncaught exceptions

* Free software: BSD license

Features
--------

* Uncaught exceptions in django view implementations (and middlewares) will trigger the PyCharm
  debugger


Installation
------------

You can install the plugin by running

    pip install django-pycharm-breakpoint

In ``settings.py`` add  ``django-pycharm-breakpoint`` to your ``INSTALLED_APPS``

    INTALLED_APPS += ['django_pycharm_breakpoint']


Usage
-----

When running in the PyCharm debugger and the package is installed and added to the ``INSTALLED_APPS``
django setting, any uncaught exception will trigger a breakpoint in PyCharm.
