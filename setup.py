from __future__ import unicode_literals
import re
from setuptools import find_packages, setup

def get_version(filename):
    content = open(filename).read()
    meta = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return meta['version']


setup(
    name='RITSEC Music Server',
    version = get_version('MusicServer/__init__.py'),  # come back for this
    author = 'Ayobami Emmanuel Adewale',
    author_email='aea8506@g.rit.edu',
    description = 'Mopidy music streaming server for the sec lab',
    packages = find_packages(),
    zip_safe = False,
    include_package_data = True,
    install_requires = [
        'Mopidy >= 1.1.0',
        'setuptools'
    ],

    entry_points={
        'mopidy.ext' : [
            'RITSEC_SECLAB = app:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)