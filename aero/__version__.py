# -*- coding: utf-8 -*-
"""
Package manager recycler, aero

For support please visit Aeronautics on github.
Project page: https://github.com/Aeronautics/aero
"""
import sys
from distutils import version

from collections import namedtuple
v = namedtuple('version_info', 'major minor micro releaselevel serial')


class V(v):
    def __init__(self, *args, **kwargs):
        try:
            val = args[3]
        except IndexError:
            val = kwargs['releaselevel']
        if val not in ('', 'a', 'alpha', 'b', 'beta'):
            raise ValueError("Release-level must be one of 'a', 'alpha', 'b' or 'beta' but '{}' given".format(val))
        # other values must be numbers
        map(int, [a for a in args if a != args[3]])
        map(int, [a for a in kwargs.values() if a != kwargs['releaselevel']])

__version_info__ = V(0, 0, 1, 'alpha', 0)
__version__ = '{}.{}.{}{:1.1}{}'.format(*tuple(__version_info__))
__build__ = __version_info__.serial
__authors__ = ('Nick Lombard - nickl-', 'Jayson Reis')
__email__ = ("github@jigsoft.co.za", '')
__title__ = 'aero'
__license__ = 'BSD 3-Clause'
__url__ = "https://github.com/Aeronautics/aero",
__download_url__ = "https://github.com/Aeronautics/aero/tarball/master",
__copyright__ = ('Copyright (c) 2012, Nick Lombard et al.', 'Copyright (c) 2012, Jayson Rei')
__docformat__ = 'restructuredtext'
__ascii_by__ = ['Si Deane', 'Chad Vice', 'Scott Davey', 'Wil Dixon', 'Brad Leftwich',
                'Thor Aage Eldby', 'Ennis Trimble', 'Joan Stark', 'Jochem Berends']
