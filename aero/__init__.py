# -*- coding: utf-8 -*-
__author__ = 'nickl-'

import warnings
import os
warnings.resetwarnings()

from .__version__ import __version_info__
from . import cache, command
from .argument import ArgumentDelegate
from .adapters import AVAILABLE_ADAPTERS


def autocomplete(commands, argp):  # TODO complete packages found
    if 'AERO_AUTO_COMPLETE' not in os.environ:
        return
    else:
        cwords = os.environ['COMP_WORDS']
        cword = int(os.environ['COMP_CWORD'])
        cwords = cwords.split(' ')
        adapters = [type(n).__name__.lower() for n in AVAILABLE_ADAPTERS]
        if '-p' in cwords[cword - 1]:
            print ' '.join(
                [p for p in 'less more most cat'.split(' ') if not cwords[cword] or p.startswith(cwords[cword])]
            )
            exit()
        if '-d' in cwords[cword - 1]:
            print ' '.join(
                [n for n in adapters if n not in cwords and (not cwords[cword] or n.startswith(cwords[cword]))]
            )
            exit()
        if cwords[cword - 1] in commands:
            if not cwords[cword]:
                print ': '.join(adapters) + ': --help'
            else:
                adapters = ': '.join([a for a in adapters if a.startswith(cwords[2])])
                print adapters + ':' if adapters else ''
            exit(0)
        if not cwords[cword].startswith('-') and not [c for c in cwords[1:] if c in commands]:
            print ' '.join([c for c in commands if not cwords[cword] or c.startswith(cwords[cword])])
            exit(0)
        options = ','.join([','.join(a.option_strings) for a in argp._actions])
        options = [o for o in options.split(',')
                   if '-d' in o or (o not in cwords and o[1:3] not in cwords
                                    and o not in [c[1:3] for c in cwords])]
        print ' '.join([o for o in options if o.startswith(cwords[cword])])
        exit()


def main():
    commands = {
        'search': [
            'Do an aero search for a package',
            'The package name to aero search',
        ],
        'install': [
            'Do an aero install package',
            'The package name to aero install',
        ],
        'info': [
            'Do an aero info for a package',
            'The package name to aero info',
        ],
    }
    argp = ArgumentDelegate(
        prog='aero',
        version='v{}.{}.{} {} {}'.format(*__version_info__),
    )
    autocomplete(commands.keys(), argp)
    argp.add_package_commands(commands)

    argp.parse_args()
