# -*- coding: utf-8 -*-
from __future__ import division

from aero.__version__ import __version_info__
__author__ = 'nickl-'

from .base import CommandProcessor as CommandProcessor

class InfoCommand(CommandProcessor):

    from .base import coroutine

    @coroutine
    def res(self):
        while True:
            res = (yield)
            if res[0] and 'Aborted:' in res[0]:
                print res[0]
                continue
            from importlib import import_module
            (width, height) = import_module('aero.commands').getTerminalSize()
            factor = width / 100
            size = map(str, map(int , [(40 * factor)-3, 58 * factor, 60 * factor]))
            key = ''
            from StringIO import StringIO
            pager = StringIO()
            pager.write(u'─' * width)
            pager.write(('\n{:>' + size[0] + '}   {:<' + size[2] + '}\n').format(
                'INFORMATION:',
                ', '.join(map(
                    lambda x: x if ':' not in x else x.split(':')[1],
                    self.data.packages
                ))
            ))
            pager.write(('{:>' + size[0] + u'}─┬─{:<' + size[2] + '}\n').format(
                u'─' * int(size[0]), u'─' * int(size[2])
            ))
            import textwrap
            for line in res:
                if isinstance(line, tuple) or isinstance(line, list):
                    if len(line) >= 2:
                        key = line[0].title() + ':' if line[0] else ' '
                        line = line[1]
                    else:
                        line = line[0]
                    if len(key) > int(size[0]):
                        wrap = textwrap.wrap(key, int(size[0]))
                        key = wrap.pop()
                        for w in wrap:
                            pager.write(
                                ('{:>' + size[0] + u'} │\n').format(w)
                            )
                if line:
                    for l in line.splitlines():
                        if len(l) > int(size[1]):
                            for wrap in textwrap.wrap(l, int(size[1])):
                                pager.write(
                                    ('{:>' + size[0] + u'} │ {:' + size[1] + '}\n').format(
                                        key, wrap)
                                )
                                key = ''
                        else:
                            pager.write(('{:>' + size[0] + u'} │ {:' + size[1] + '}\n').format(
                                key,
                                l.lstrip())
                            )
                            key = ''
            pager.write(('{:>' + size[0] + u'}─┴─{:<' + size[2] + '}\n').format(
                u'─' * int(size[0]), u'─' * int(size[2])
            ))
            self.render(pager)


