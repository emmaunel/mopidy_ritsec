# Simple Mopidy web Client for CSEC Labs
#
# Author: Emmanuel Adewale

from __future__ import unicode_literals
import re
from setuptools import find_packages, setup


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='RITSEC Music Server',
    version = get_version('mopidy_ritsec/__init__.py'),
    url = 'https://github.com/emmaunel/mopidy_ritsec',
    license='Apache License, Version 2.0', # Add license
    author = 'Emmanuel Adewale',
    author_email='aea8506@g.rit.edu',
    description = 'Mopidy music streaming server for the sec lab',
    long_description = open('README.rst').read(),
    packages = find_packages(exclude=['tests', 'tests.*']),
    zip_safe = False,
    include_package_data = True,
    install_requires = [
        'Mopidy >= 0.14',
        'setuptools'
    ],

    entry_points={
        'mopidy.ext' : [
            'mopidy_ritsec = mopidy_ritsec:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)