#!/usr/bin/env python
#coding: utf-8
from distribute_setup import use_setuptools
use_setuptools()

from aero.__version__ import __version__, __title__, __authors__, __email__, __license__, __url__, __download_url__
from setuptools import setup

setup(
    name=__title__,
    author=__authors__,
    author_email=__email__,
    version=__version__,
    license=__license__,
    url=__url__,
    download_url=__download_url__,
    packages=['aero', 'aero.adapters'],
    package_data={'aero': ['assets/*.ascii']},
    description=[
        descr.strip() for descr in open('README.txt').read().splitlines()[:6]
        if descr and '===' not in descr
    ][1],
    long_description=open('README.txt').read(),
    install_requires=["beaker", "PyYAML", "pygments", "progbar"],
    platforms=['Linux', 'Mac OSX'],
    classifiers=[  # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities',
        ],
    scripts=["aero/aero"],
)
