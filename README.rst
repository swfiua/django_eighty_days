=============================
django-eighty-days
=============================

.. image:: https://badge.fury.io/py/django_eighty_days.png
    :target: https://badge.fury.io/py/django_eighty_days

.. image:: https://travis-ci.org/swfiua/django_eighty_days.png?branch=master
    :target: https://travis-ci.org/swfiua/django_eighty_days

.. image:: https://coveralls.io/repos/swfiua/django_eighty_days/badge.png?branch=master
    :target: https://coveralls.io/r/swfiua/django_eighty_days?branch=master

A django app for around the world in 80 days

Documentation
-------------

The full documentation is at https://django_eighty_days.readthedocs.org.

Quickstart
----------

Install django-eighty-days::

    pip install django_eighty_days

Then use it in a project::

    import django_eighty_days

Features
--------

* TODO

Auto-generating API code
------------------------

django_eighty_days/codegen.py is used to auto-generate api.py,
serializer.py and urls.py.

If new models are added to models.py you just need to re-run::

   python django_eighty_days/codgen.py

All goes well it will update the api/serializer and url code with new
boiler plate for the new models.

