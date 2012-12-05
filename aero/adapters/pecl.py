# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from aero.__version__ import __version__
from .base import BaseAdapter


class Pecl(BaseAdapter):
    """
    Pecl adapter.
    """
    def search(self, query):
        response = self.command('-q search', query)[0]
        if 'MATCHED PACKAGES' in response:
            from re import match
            from string import strip
            return dict([
                self.package_name(u'{0}|Version:{1}\nhttp://pecl.php.net/{0}\n{2}'.format(
                    *map(strip, match('(.* (?=\d))(.*\) +)(.*$)', line).groups())
                )).split('|')
                         for line in response.splitlines()
                         if line
                            and 'STABLE/(LATEST)' not in line
                            and match('(.* (?=\d))(.*\) +)(.*$)', line)
            ])
        return {}

    def info(self, query):
        response = self.command('remote-info', query)[0]
        if 'Unknown package' not in response:
            from re import match
            from string import strip
            return [(map(strip, match('(\w*)(.*$)',line).groups()))
                    for line in response.splitlines()
                    if line
                       and 'PACKAGE' not in line
                       and '====' not in line
                       and match('(\w*)(.*$)',line)]
        return [u'Aborted: No info available']

    def install(self, query):
        self.shell('install', query)
        return {}
