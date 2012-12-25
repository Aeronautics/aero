# -*- coding: utf-8 -*-
__author__ = 'nickl-'

import warnings
warnings.resetwarnings()

from .__version__ import __version_info__

def main():
    from .argument import ArgumentDelegate
    argp = ArgumentDelegate(
        prog='aero',
        version='v{}.{}.{} {} {}'.format(*__version_info__),
    )
    from argcomplete import autocomplete
    autocomplete(argp)
    argp.parse_args()
