# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from aero.__version__ import __version__
from .base import BaseAdapter


class Pecl(BaseAdapter):
    """
    Pecl adapter.
    """
    adapter_command = 'pecl'

    def search(self, query):
        print query
        response = self._execute_command(self.adapter_command, ['-q', 'search', query])[0]
        if 'MATCHED PACKAGES' in response:
            from re import match
            from string import strip
            return dict([(
                (self.adapter_command+':{0}|Version:{1}\nhttp://pecl.php.net/{0}\n{2}').format(
                    *map(strip, match('(.* (?=\d))(.*\) +)(.*$)',line).groups())
                ).split('|'))
                         for line in response.splitlines()
                         if line
                            and 'STABLE/(LATEST)' not in line
                            and match('(.* (?=\d))(.*\) +)(.*$)',line)
            ])
        return {}

    def info(self, query):
        response = self._execute_command(self.adapter_command, ['remote-info', query])[0]
        if 'Unknown package' not in response:
            from re import match
            from string import strip
            return [(map(strip, match('(\w*)(.*$)',line).groups()))
                    for line in response.splitlines()
                    if line
                       and 'PACKAGE' not in line
                       and '====' not in line
                       and match('(\w*)(.*$)',line)]
        return [['No info available']]

    def install(self, query):
        print '\n'
        self._execute_shell(self.adapter_command, ['install', query])
        return {}
