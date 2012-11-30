# -*- coding: utf-8 -*-
__author__ = 'nickl-'

import sys
import textwrap

from .__version__ import __version__

from .cache import CacheProviderFactory
from .adapters import AVAILABLE_ADAPTERS


class CommandProcessor():

    cache = CacheProviderFactory().whichProvider()

    def __init__(self, data):
        if data.invalidate:
            self.cache.invalidate(True)

    def cmd(self):
        return self.__class__.__name__.replace('Command', '').lower()

    def do(self, pkg, data, mngr=None):
        for adapter in AVAILABLE_ADAPTERS:
            if dptr not in data.disabled:
                if not mngr or mngr == dptr.lower():
                    sys.stdout.write(
                        'Doing an aero {} of package: {} using {} '.format(
                            self.cmd(), pkg, type(adapter).__name__
                        )
                    )
                    self.call(adapter, pkg)

    def call(self, adapter, args):
        try:
            return getattr(adapter, self.cmd())(args)
        except AttributeError:  # as e: # Trust me you're going to want to use that e when duck duck misses
            # print e
            return 'Aborted: {} has no implementation for command: {}'.format(
                adapter.__class__.__name__, self.cmd()
            )


class SearchCommand(CommandProcessor):

    def do(self, pkg, data, mngr=None):
        res = self.cache.seen(pkg)
        if data.invalidate or res is False:
            res = {}
            for adapter in AVAILABLE_ADAPTERS:
                if dptr not in data.disabled:
                    if not mngr or mngr == dptr.lower():
                        sys.stdout.write('Doing an aero {} of package: {} using {} '.format(
                            self.cmd(), pkg, type(adapter).__name__)
                        )
                        aero = self.call(adapter, pkg)
                        print 'Found ({}) options'.format(len(aero))
                        if aero:
                            res.update(aero)

        if res:
            res = sorted(self.cache.seen(pkg, res).items())
            pager = sys.stdout
            use_pager = len(res) > 30  # TODO find real screen height
            if use_pager:
                pager = open('/tmp/aero.out', 'w')
            pager.write("\n{:>48}   {:<52}\n".format("PACKAGE NAME", "DESCRIPTION"))
            pager.write("{:>48}   {:<52}\n".format("_" * 40, "_" * 50))
            for k, v in res:
                for line in v.splitlines():
                    if k:
                        k += ' :'
                    if len(line) > 50:
                        for wrap in textwrap.wrap(line, 50):
                            pager.write("{:>50} {:<50}\n".format(k, wrap))
                            k = ''
                    else:
                        pager.write("{:>50} {:<50}\n".format(k, line))
                    k = ''
            pager.write('\n')
            if use_pager:
                from subprocess import Popen
                pager.close()
                Popen(data.pager + ' /tmp/aero.out', shell=True).wait()


class InstallCommand(CommandProcessor):

    pass


class InfoCommand(CommandProcessor):

    def do(self, pkg, data, mngr=None):
        res = self.cache.seen(pkg)
        if data.invalidate or res is False:
            res = []
            for adapter in AVAILABLE_ADAPTERS:
                if dptr not in data.disabled:
                    if not mngr or mngr == dptr.lower():
                        print 'Doing an aero {} of package: {} using {} \n'.format(
                            self.cmd(), pkg, type(adapter).__name__
                        )
                        res = self.cache.seen(pkg, self.call(adapter, pkg))

        if 'Aborted:' in res:
            print res
            return
        k = ''
        print "\n{:>48}   {:<52}".format('', 'INFORMATION: ' + pkg)
        print "{:>48}   {:<52}".format("_" * 40, "_" * 50)
        for line in res:
            if isinstance(line, tuple) or isinstance(line, list):
                if len(line) >= 2:
                    k = line[0] + ' :'
                    line = line[1]
                else:
                    line = line[0]
            if line:
                for l in line.splitlines():
                    if len(l) > 50:
                        for wrap in textwrap.wrap(l, 50):
                            print "{:>50} {:50}".format(k, wrap)
                            k = ''
                    else:
                        print "{:>50} {:50}".format(k, l)
                        k = ''
