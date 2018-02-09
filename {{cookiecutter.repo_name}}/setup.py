#!/usr/bin/env python
import os
from setuptools import setup, find_packages

import {{cookiecutter.repo_name}}

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()
with open(os.path.join(here, 'requirements.pip')) as f:
    requires = f.readlines()

setup(
    name='{{cookiecutter.repo_name}}',
    version={{cookiecutter.repo_name}}.__version__,
    description='{{cookiecutter.short_description}}',
    long_description=README + '\n\n' + CHANGES,
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'dev': {
            'ipython': '<6'
        },
        'production': {
            'uwsgi': '2.0.15',
        }
    },
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development',
    ],
)
