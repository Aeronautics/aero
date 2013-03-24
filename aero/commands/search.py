# -*- coding: utf-8 -*-
from __future__ import division
from aero.__version__ import __version_info__

__author__ = 'nickl-'

from .base import CommandProcessor as CommandProcessor

class SearchCommand(CommandProcessor):

    from .base import coroutine

    @coroutine
    def res(self):
        while True:
            res = (yield)
            if res:
                if isinstance(res, list):
                    print '\n' + res[0]
                    continue
                from importlib import import_module
                (width, height) = import_module('aero.commands').getTerminalSize()
                factor = width / 100
                size = map(str, map(int , [(40 * factor)-3, 58 * factor, 60 * factor]))
                res = sorted(res.items())
                from StringIO import StringIO
                pager = StringIO()
                pager.write(u'─' * width)
                pager.write(('\n{:>' + size[0] + '}   {:<' + size[2] + '}\n').format(
                    'PACKAGE NAME', 'DESCRIPTION'
                ))
                pager.write(('{:>' + size[0] + u'}─┬─{:<' + size[2] + '}\n').format(
                    u'─' * int(size[0]), u'─' * int(size[2])
                ))
                for key, value in res:
                    for line in value.splitlines():
                        if len(line) > int(size[1]):
                            for wrap in import_module('textwrap').wrap(line, int(size[1])):
                                pager.write(
                                    ('{:>' + size[0] + u'} │ {:<' + size[1] + '}\n').format(
                                        key.strip(), wrap.lstrip()
                                    )
                                )
                                key = ''
                        else:
                            pager.write(
                                ('{:>' + size[0] + u'} │ {:<' + size[1] + '}\n').format(
                                    key.strip(), line.lstrip()
                                )
                            )
                        key = ''
                pager.write(('{:>' + size[0] + u'}─┴─{:<' + size[2] + '}\n').format(
                    u'─' * int(size[0]), u'─' * int(size[2])
                ))
                self.render(pager)

