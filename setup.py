#!/usr/bin/env python
#coding: utf-8
from distribute_setup import use_setuptools
use_setuptools()

from aero.__version__ import __version__, __title__, __authors__, __email__, __license__, __url__, __download_url__
from setuptools import setup

setup(
	name         = __title__,
	author       = __authors__,
	author_email = __email__,
	version      = __version__,
	license      = __license__,
	url          = __url__,
	download_url = __download_url__,
#	description = "Software discovery and installation through colaborative package management.",
#	py_modules = "",
	packages     = ['aero', 'aero.adapters'],
    package_data ={'aero': ['assets/*.ascii']},
    description  = [descr for descr in open('README.txt').read().splitlines() if descr.strip() and '===' not in descr][1],
#    data_files=[('aero', 'assets/ascii-planes assets/crash.ascii assets/descrip.ascii assets/epilog.ascii assets/title.ascii'.split())],
    long_description=open('README.txt').read(),
#	install_requires = "",
	scripts      = ["aero/aero"],
#    entry_points={'console_scripts':['aero = aero:main'] },

)
