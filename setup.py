#!/usr/bin/env python
#coding: utf-8
from distribute_setup import use_setuptools
use_setuptools()

from aero import __version__ as v
from setuptools import setup

setup(
	name = v.__title__,
	author = v.__authors__,
	author_email = v.__email__,
	version = v.__version__,
	license = v.__license__,
	url = v.__url__,
	download_url = v.__download_url__,
#	description = "Software discovery and installation through colaborative package management.",
#	py_modules = "",
	packages = ['aero', 'aero.adapters'],
    package_data={'aero': ['assets/*.ascii']},
    description = [descr for descr in open('README.txt').read().splitlines() if descr.strip() and '===' not in descr][1],
#    data_files=[('aero', 'assets/ascii-planes assets/crash.ascii assets/descrip.ascii assets/epilog.ascii assets/title.ascii'.split())],
    long_description=open('README.txt').read(),
#	install_requires = "",
	scripts = ["aero/aero"],
#    entry_points={'console_scripts':['aero = aero:main'] },

)
