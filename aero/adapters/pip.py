# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from string import strip
from aero.__version__ import __version__
from importlib import import_module
from .base import BaseAdapter


class Pip(BaseAdapter):
    """
    Pip adapter.
    """
    def search(self, query):
        m = import_module('pip.commands.search')
        lst = {}
        for r in m.transform_hits(m.SearchCommand().search(query, 'http://pypi.python.org/pypi')):
            summary = ' '.join(map(strip, r['summary'].split('\n'))).replace('  ', ' ')
            lst[self.package_name(r['name'])] = 'Version: {:<14} Score:{:>4}\n{}'.format(
                max(r['versions']),
                r['score'],
                (summary if len(summary) < 200 else summary[:190] + '...').replace('  ', ' ')
            )
        return lst

    def install(self, query):
        self.shell([
            'install',
            '--force-reinstall',
            '--timeout', '30',
            '--egg',
            '--log', '~/.aero/log/pip.log',
            '--download-cache', '~/.aero/cache/pip',
            query
        ])
        return {}
