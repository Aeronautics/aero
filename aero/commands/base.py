# -*- coding: utf-8 -*-
from __future__ import division
from aero.__version__ import __version_info__, enc
__author__ = 'nickl-'


from aero.adapters import AVAILABLE_ADAPTERS

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

class ProgressTicker():

    from aero.adapters import AVAILABLE_ADAPTERS

    ref = None
    result = None
    steps = len(AVAILABLE_ADAPTERS)
    taken = 0

    def routine(self, routine):
        self.ref = routine

    def done(self):
        return (self.taken * 100) // self.steps

    def terminate(self):
        self.taken = self.steps
        try:
            self.ref.send('terminate')
        except StopIteration:
            pass

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




class CommandProcessor(object):

    from aero.cache import CacheProviderFactory


    cache = CacheProviderFactory().whichProvider()
    data = None
    out = None

    ticker = ProgressTicker()
    clear = '\x1b[2J\x1b[0;0H'

    def __init__(self, data):
        self.data = data
        self.out = self.write()
        if self.data.invalidate:
            self.cache.invalidate(True)
        self.out.send(
            self.clear +
            'aero v{}.{}.{} {} {}\n\n'.format(*__version_info__)
        )

    def execute(self):
        try:
            next = self.wiring()
            self.do(self.data.packages, next)
        except BaseException as e:
            self.out.send(
                '\n\n[{}{}] Terminating...\n'.format(
                    type(e).__name__,
                    ': {}'.format(e) if len(str(e)) else ''
                ))
            self.ticker.terminate()

    # wire coroutines
    def wiring(self):
        self.ticker.routine(self.progress(self.res()))
        return self.each(self.call(self.ticker))

    @coroutine
    def res(self):
        while True: (yield)

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
            if not mngr or mngr in [a[0] for a in AVAILABLE_ADAPTERS]:
                adapters.send((pkg, mngr))
            else:
                self.ticker.send((len(AVAILABLE_ADAPTERS),
                    ['Aborted: No package manager named "{}" is available.'.format(mngr)]))

    @coroutine
    def write(self):
        from StringIO import StringIO
        out = StringIO()
        while True:
            text = (yield)
            out.write(str(text))
            print out.getvalue()

    def seen(self, command, adapter, package, result=False):
        cache_key = command + '+' + adapter + ':' + package
        return self.cache.seen(cache_key, result)

    @coroutine
    def each(self, target):
        while True:
            args = (yield)
            package = args[0]
            manager = args[1]
            for adapter in AVAILABLE_ADAPTERS:
                adapter_name = adapter[0]
                if adapter_name not in self.data.disabled:
                    if not manager or manager == adapter_name:
                        length = str(max([len(a[0]) for a in AVAILABLE_ADAPTERS]))
                        self.out.send(
                            ('Doing an aero {} of package: {} using {:<' + length + '} ').format(
                                self.cmd(), package, adapter_name
                            )
                        )
                        res = self.seen(self.cmd(), adapter_name, package)
                        if self.data.invalidate or res is False:
                            target.send((adapter, package))
                        else:
                            self.out.send('Found {:>4} options [CACHED]\n'.format(len(res)))
                            self.ticker.send((1, res))
                    else:
                        self.ticker.send(1)
                else:
                    self.ticker.send(1)

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
                if bar.isAlive():
                    bar.stop()
                bar.join()
                self.out.send('')
                if not isinstance(result, str): # terminate
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
                    self.out.send('Found {:>4} options\n'.format(len(aero)))
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
            except NotImplementedError:
                target.send((1,
                    ['Aborted: {} has no implementation for command: {}\n'.format(
                        adapter_name, self.cmd()
                    )]
                ))

    def render(self, pager):
        from pygments import highlight
        from pygments.lexers import CppLexer
        from pygments.formatters import Terminal256Formatter
        from importlib import import_module
        height = import_module('aero.commands').getTerminalSize()[1]
        out = pager.getvalue()
        pager.close()
        out = highlight(out, CppLexer(), Terminal256Formatter())
        out = out.encode(*enc)
        if len(out.splitlines()) > height:
            from subprocess import Popen, PIPE
            Popen(self.data.pager, shell=True, stdin=PIPE).communicate(input=out)
        else:
            if 'DebugCommandProcessor' not in self.__class__.__bases__[0].__name__:
                print self.clear
            print out



class DebugCommandProcessor(CommandProcessor):

    def seen(self, command, adapter, package, result=False):
        if not isinstance(result, bool):
            print '\n{:=^100}'.format('')
            print '{:=^100}'.format(' '+command+' '+adapter+' '+package+' ')
            print '{:=^100}'.format('')
            print 'Result type: ', type(result).__name__
            itr = result
            if isinstance(result, dict):
                itr = result.items()
            for r in itr:
                print '{} | {:^5} | {}'.format(type(r).__name__, len(r) if r else 0, r)
            print '\n'
        return result

    @coroutine
    def write(self):
        import sys
        out = sys.stdout
        while True:
            text = (yield)
            out.write(str(text))

    @coroutine
    def progress(self, target):
        while True:
            result = (yield)
            if self.ticker.done() == 100:
                target.send(result)

    def execute(self):
        next = self.wiring()
        self.do(self.data.packages, next)
