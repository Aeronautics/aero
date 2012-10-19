# -*- coding: utf-8 -*-
__author__ = 'nickl-'
from cache import CacheProviderFactory
from adapters import AVAILABLE_ADAPTERS
import sys, textwrap

class CommandProcessor():
    cache = CacheProviderFactory().whichProvider()

    def __init__(self, data):
        if (data.invalidate):
            self.cache.invalidate(True)

    def cmd(self):
        return self.__class__.__name__.replace('Command','').lower()

    def do(self, pkg, data, mngr=None):
        for adapter in AVAILABLE_ADAPTERS:
            dptr = type(adapter).__name__
            if dptr not in data.disabled:
                if not mngr or mngr == dptr.lower():
                    sys.stdout.write('Doing an aero {} of package: {} using {} '.format(self.cmd(), pkg, type(adapter).__name__))
                    self.call(adapter, pkg)

    def call(self, adapter, args):
        try:
            return getattr(adapter, self.cmd())(args)
        except AttributeError as e:
            print e
            return '{} has no implementation for command: {}'.format(adapter.__class__.__name__, self.cmd())

class SearchCommand(CommandProcessor):
    def do(self, pkg, data, mngr=None):
        res = self.cache.seen(pkg)
        if data.invalidate or res == False:
            res = {}
            for adapter in AVAILABLE_ADAPTERS:
                dptr = type(adapter).__name__
                if dptr not in data.disabled:
                    if not mngr or mngr == dptr.lower():
                        sys.stdout.write('Doing an aero {} of package: {} using {} '.format(self.cmd(), pkg, type(adapter).__name__))
                        aero = self.call(adapter, pkg)
                        res.update(aero)
                        print 'Found ({}) options'.format(len(aero))


        if res:
            res = sorted(self.cache.seen(pkg, res).items())
#            pager = sys.stdout
#            use_pager = len(res) > 30 #TODO find real screen height
            from prettytable import PrettyTable, FRAME
            t = PrettyTable()
            t.add_column("PACKAGE NAME", [r[0] for r in res], 'r')
            t.add_column("DESCRIPTION", [r[1] for r in res], 'l')
            t.max_width = 79
            t.border = False
            t.header = True
            t.hrules = FRAME
            t.padding_width = 0
            t.left_padding_width = 1
            t.right_padding_width = 1
#            t.vertical_char = ":"
            t.junction_char = ':'
#            print t.rowcount
            if t.rowcount > 30:
                from subprocess import Popen
                pager = open('/tmp/aero.out', 'w')
                pager.write(str(t))
                pager.close()
                Popen(data.pager+' /tmp/aero.out', shell=True).wait()
            else:
                print t

#            t.
            #pager.write("\n\n%50s   %-50s\n" % ("PACKAGE NAME", "DESCRIPTION"))
#            for k,v in sorted(self.cache.seen(pkg, res).items()):
#                t.add_row([k,v])
#                for wrap in textwrap.wrap(v, 50):#p.sub('',v)
#                    pager.write("%50s : %-50s\n" % (k, wrap))
#                    k = ''
#            if use_pager:
#                from subprocess import Popen
#                pager = open('/tmp/aero.out', 'w')
#                pager.write(t)
#                pager.close()
#                Popen(data.pager+' /tmp/aero.out', shell=True).wait()
#            else:
#            print t.get_string(max_width = 79,
#                border = False,
#                theader = True,
#                junction_char = ':',
#                padding_width = 0,
#                left_padding_width = 0,
#                right_padding_width = 0,
#            )

class InstallCommand(CommandProcessor):
    pass

class InfoCommand(CommandProcessor):
    def do(self, pkg, data, mngr=None):
        res = self.cache.seen(pkg)
        if data.invalidate or res == False:
            res = []
            for adapter in AVAILABLE_ADAPTERS:
                dptr = type(adapter).__name__
                if dptr not in data.disabled:
                    if not mngr or mngr == dptr.lower():
                        print 'Doing an aero %s of package: %r using %s \n' % (self.cmd(), pkg, type(adapter).__name__)
                        lines = self.call(adapter, pkg)
                        try:
                            lines = lines.splitlines()
                        except AttributeError:
                            pass
                        for longline in lines:
                            if longline:
                                for line in textwrap.wrap(longline, 70):
                                    print "%30s %-70s" % ('', line)
                            else:
                                print
