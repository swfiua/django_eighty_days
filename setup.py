#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_eighty_days

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_eighty_days.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-eighty-days',
    version=version,
    description="""A django app for around the world in 80 days""",
    long_description=readme + '\n\n' + history,
    author='Johnny Gill',
    author_email='swfiua@gmail.com',
    url='https://github.com/swfiua/django_eighty_days',
    packages=[
        'django_eighty_days',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django_eighty_days',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
