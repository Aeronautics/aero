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
            if u'Aborted:' in res[0]:
                print res[0]
                continue
            from importlib import import_module
            (width, height) = import_module('aero.commands').getTerminalSize()
            factor = width / 100
            size = map(str, map(int , [(40 * factor)-3, 55 * factor, 60 * factor]))
            key = u''
            from StringIO import StringIO
            pager = StringIO()
            pager.write(u'─' * width)
            pager.write((u'\n{:>' + size[0] + u'}   {:<' + size[2] + u'}\n').format(
                u'INFORMATION:',
                u', '.join(map(
                    lambda x: x if u':' not in x else x.split(u':')[1],
                    self.data.packages
                ))
            ))
            pager.write((u'{:>' + size[0] + u'}─┬─{:<' + size[2] + u'}\n').format(
                u'─' * int(size[0]), u'─' * int(size[2])
            ))
#            pager.write((u'{:>' + size[0] + u'}═╤═{:<' + size[2] + u'}\n').format(
#                u'═' * int(size[0]), u'═' * int(size[2])
#            ))
            #            pager.write(u'{:>47}    {:<52}\n'.format(u'_' * 40, u'_' * 50))
            for line in res:
                if isinstance(line, tuple) or isinstance(line, list):
                    if len(line) >= 2:
                        key = line[0].title() + u':' if line[0] else u' '
                        line = line[1]
                    else:
                        line = line[0]
                if line:
                    for l in line.splitlines():
                        if len(l) > int(size[1]):
                            import textwrap
                            for wrap in textwrap.wrap(l, int(size[1])):
                                pager.write(
                                    (u'{:>' + size[0] + u'} │ {:' + size[1] + u'}\n').format(
                                        key, wrap)
                                )
                                key = u''
                        else:
                            pager.write((u'{:>' + size[0] + u'} │ {:' + size[1] + u'}\n').format(
                                key,
                                l.lstrip())
                            )
                            key = u''
            pager.write((u'{:>' + size[0] + u'}─┴─{:<' + size[2] + u'}\n').format(
                u'─' * int(size[0]), u'─' * int(size[2])
            ))
            self.render(pager)


