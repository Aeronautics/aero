# -*- coding: utf-8 -*-

__author__ = 'nickl-'

import sys
import textwrap

from .__version__ import __version__

from .cache import CacheProviderFactory
from .adapters import AVAILABLE_ADAPTERS

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

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
            use_pager = len(res) > 30  # TODO find real screen height
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
                from cStringIO import StringIO
                pager = StringIO()
                from pygments import highlight
                from pygments.lexers import CppLexer
                from pygments.formatters import Terminal256Formatter
                out = pager.getvalue()
                out = highlight(out, CppLexer(), Terminal256Formatter())
                out = out.encode('utf')
                if len(out.splitlines()) > 30:
                    from subprocess import Popen, PIPE
                    Popen(self.data.pager, shell=True, stdin=PIPE).communicate(input=out)
                else:
                    print out


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
