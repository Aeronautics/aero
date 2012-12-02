# -*- coding: utf-8 -*-

__author__ = 'nickl-'

import sys
import textwrap

from .__version__ import __version_info__

from .cache import CacheProviderFactory
from .adapters import AVAILABLE_ADAPTERS

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

class ProgressTicker():

    ref = None
    result = None
    steps = len(AVAILABLE_ADAPTERS)
    taken = 0

    def routine(self, routine):
        self.ref = routine

    def done(self):
        return int(float(self.taken) / float(self.steps) * 100)

    def send(self, args):
        if isinstance(args, int):
            self.taken += args
        elif isinstance(args[0], str) and args[0] == 'step':
            self.steps += args[1]
        else:
            self.taken += args[0]
            if isinstance(args[1], dict):
                if not self.result:
                    self.result = {}
                self.result.update(args[1])
            elif isinstance(args[1], list):
                if not self.result:
                    self.result = []
                self.result.extend(args[1])
        self.ref.send(self.result)

class CommandProcessor():

    cache = CacheProviderFactory().whichProvider()
    data = None
    out = None
    ticker = ProgressTicker()
    clear = '\x1b[2J\x1b[0;0H'

    def __init__(self, data):
        self.data = data
        if self.data.invalidate:
            self.cache.invalidate(True)
        next = self.wiring()
        self.out.send(
            self.clear +
            'aero v{}.{}.{} {} {}\n\n'.format(*__version_info__)
        )
        self.do(data.packages, next)

    # wire coroutines
    def wiring(self):
        self.out = self.write()
        self.ticker.routine(self.progress(self.res()))
        return self.each(self.call(self.ticker))

    @coroutine
    def res(self):
        while True:
            result = (yield)

    def cmd(self):
        return self.__class__.__name__.replace('Command', '').lower()

    def do(self, packages, adapters):
        self.ticker.steps = len(packages) * len(AVAILABLE_ADAPTERS)
        for package in packages:
            if ':' in package:
                mngr = package.partition(':')
                pkg = mngr[2]
                mngr = mngr[0]
            else:
                mngr = None
                pkg = package
            adapters.send((pkg, mngr))

    @coroutine
    def write(self):
        from cStringIO import StringIO
        out = StringIO()
        while True:
            text = (yield)
            out.write(text)
            print out.getvalue()

    def seen(self, command, adapter, package, result=False):
        cache_key = command + "+" + adapter + ":" + package
        return self.cache.seen(cache_key, result)

    @coroutine
    def each(self, target):
        while True:
            args = (yield)
            package = args[0]
            manager = args[1]
            for adapter in AVAILABLE_ADAPTERS:
                adapter_name = adapter[0]
                if not manager or manager == adapter_name.lower():
                    self.out.send(
                        'Doing an aero {} of package: {} using {} '.format(
                            self.cmd(), package, adapter_name
                        )
                    )
                res = self.seen(self.cmd(), adapter_name, package)
                self.ticker.send(('step', 4))
                if self.data.invalidate or res is False:
                    if adapter_name not in self.data.disabled:
                        if not manager or manager == adapter_name.lower():
                            self.ticker.send(1)
                            target.send((adapter, package))
                            self.ticker.send(1)
                        else:
                            self.ticker.send(3)
                        self.ticker.send(1)
                    else:
                        self.ticker.send(4)
                    self.ticker.send(1)
                else:
                    if not manager or manager == adapter_name.lower():
                        self.out.send('Found ({}) options [CACHED]\n'.format(len(res)))
                    self.ticker.send((5, res))

    @coroutine
    def progress(self, target):
        from progbar import ProgBar
        bar = ProgBar('Progress: ', 30)
        bar.start()
        while True:
            result = (yield)
            self.out.send('')
            bar.percent = self.ticker.done()
            if self.ticker.done() == 100:
                bar.join()
                self.out.send('')
                target.send(result)

    @coroutine
    def call(self, target):
        while True:
            adapter_name = ''
            payload = (yield)
            adapter_name = payload[0][0]
            adapter = payload[0][1]
            package = payload[1]
            try:
                adapter.passthruArgs(self.data.passthru)
                aero = getattr(adapter, self.cmd())(package)
                if self.cmd() == 'search':
                    self.out.send('Found ({}) options\n'.format(len(aero)))
                else:
                    self.out.send('\n')
                target.send((1,
                    self.seen(
                        self.cmd(),
                        adapter_name,
                        package,
                        aero
                    ))
                )
            except Exception as e:
                target.send((1,
                    ['Aborted: {} has no implementation for command: {}\nWith message: {}\n'.format(
                        adapter_name, self.cmd(), e
                    )]
                ))


class SearchCommand(CommandProcessor):

    @coroutine
    def res(self):
        while True:
            res = (yield)
            if res:
                res = sorted(res.items())
                from cStringIO import StringIO
                pager = StringIO()
                pager.write(u"\n{:>48}   {:<52}\n".format("PACKAGE NAME", "DESCRIPTION"))
                pager.write(u"{:>48}   {:<52}\n".format("_" * 40, "_" * 50))
                for key, value in res:
                    try:
                        value = value.decode('utf-8')
                        if value.startswith(u'\ufeff'):
                            value = value[len(u'\ufeff'):]
                    except UnicodeDecodeError:
                        value = value.decode('latin1')
                    try:
                        key = key.decode('utf-8')
                        if key.startswith(u'\ufeff'):
                            key = key[len(u'\ufeff'):]
                    except UnicodeDecodeError:
                        key = key.decode('latin1')

                    key = key.encode('utf')
                    for line in value.splitlines():
                        line = line.encode('utf')
                        if key:
                            key += ' :'
                        if len(line) > 50:
                            for wrap in textwrap.wrap(line, 50):
                                pager.write("{:>50} {:<50}\n".format(key, wrap))
                                key = ''
                        else:
                            pager.write("{:>50} {:<50}\n".format(key, line))
                        key = ''
                pager.write('\n')
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

    def wiring(self):
        self.out = self.write()
        self.ticker.routine(self.progress(None))
        return self.each(self.call(self.res()))

    def seen(self, command, adapter, package, result=False):
        return result

    @coroutine
    def write(self):
        import sys
        out = sys.stdout
        while True:
            text = (yield)
            out.write(text)

    @coroutine
    def progress(self, responder):
        while True: (yield)


class InfoCommand(CommandProcessor):

    @coroutine
    def res(self):
        while True:
            res = (yield)
            if 'Aborted:' in res:
                print res
                continue
            key = ''
            print "\n{:>48}   {:<52}".format('', 'INFORMATION: ') # + self.package)
            print "{:>48}   {:<52}".format("_" * 40, "_" * 50)
            for line in res:
                if isinstance(line, tuple) or isinstance(line, list):
                    if len(line) >= 2:
                        key = line[0] + ' :'
                        line = line[1]
                    else:
                        line = line[0]
                if line:
                    for l in line.splitlines():
                        if len(l) > 50:
                            for wrap in textwrap.wrap(l, 50):
                                print "{:>50} {:50}".format(key, wrap)
                                key = ''
                        else:
                            print "{:>50} {:50}".format(key, l)
                            key = ''
