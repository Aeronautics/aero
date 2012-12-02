# -*- coding: utf-8 -*-
__author__ = 'nickl-'
__all__ = ('Pip', )

from string import strip

from aero.__version__ import __version__
from .base import BaseAdapter


class Pip(BaseAdapter):
    """
    Pip adapter.
    """
    adapter_command = 'pip'

    def search(self, query):
        response = self._execute_command(
            self.adapter_command, ['search', query]
        )[0]
        lst = {}
        from re import match
        for key, line in [map(
            strip, (self.adapter_command + ':' + l).split(' - ', 1)
        ) for l in response.splitlines() if ' - ' in l]:
            parts = match('(.*)[ <\\(]?(http.*?)?[ >\\)]?(.*)', line).groups()
            lst[key] = parts[0] + ' ' + parts[2] + ('\n' + parts[1] if parts[1] else '')
        if lst:
            return lst
        return {}

    def install(self, query):
        self._execute_shell(self.adapter_command, [
            'install',
            '--force-reinstall',
            '--timeout', '30',
            '--egg',
            '--log', '~/.aero/log/pip.log',
            '--download-cache', '~/.aero/cache/pip',
            query
        ])
        return {}
