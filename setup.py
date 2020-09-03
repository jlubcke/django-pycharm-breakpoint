#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

readme = open('README.rst').read()

requirements = [
    'Django' 
]

setup(
    name='django-pycharm-breakpoint',
    version='0.2.0',
    description='App for Django to during development enter PyCharm debugger on uncaught exceptions',
    long_description=readme + '\n',
    author='Johan Lübcke',
    author_email='johan@lubcke.se',
    url='https://github.com/jlubcke/django-pycharm-breakpoint',
    packages=['django_pycharm_breakpoint'],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='Django,pycharm',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
