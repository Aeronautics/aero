# -*- coding: utf-8 -*-
from aero.__version__ import __version_info__
__author__ = 'nickl-'

from .base import CommandProcessor as CommandProcessor


class InstallCommand(CommandProcessor):

    from .base import coroutine
    package = ''
    adapter = ''

    def wiring(self):
        self.out = self.write()
        self.ticker.routine(self.progress(None))
        return self.each(self.spacing(self.call(self.res())))

    def seen(self, command, adapter, package, result=False):
        self.package = package
        self.adapter = adapter
        return result

    @coroutine
    def res(self):
        while True:
            res = (yield)
            if res[1] == 0:
                print 'Successfully installed package: {} with {}'.format(self.package, self.adapter)
            else:
                print 'Aborted: Error while installing package: {} {} returned exit code {}'.format(
                    self.package, self.adapter, res[1]
                )

    @coroutine
    def write(self):
        import sys
        out = sys.stdout
        while True:
            text = (yield)
            out.write(text)

    @coroutine
    def spacing(self, target):
        while True:
            payload = (yield)
            print u'\n'
            target.send(payload)

    @coroutine
    def progress(self, responder):
        while True: (yield)

