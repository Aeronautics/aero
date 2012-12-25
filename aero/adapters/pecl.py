# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from aero.__version__ import __version__, enc
from .base import BaseAdapter


class Pecl(BaseAdapter):
    """
    Pecl adapter.
    """
    def search(self, query):
        response = self.command('-q search', query)[0].decode(*enc)
        if 'MATCHED PACKAGES' in response:
            from re import match
            from string import strip
            return dict([
                self.package_name('{0}|Version:{1}\nhttp://pecl.php.net/{0}\n{2}'.format(
                    *map(strip, match('(.* (?=\d))(.*\) +)(.*$)', line).groups())
                )).split('|')
                         for line in response.splitlines()
                         if line
                            and 'STABLE/(LATEST)' not in line
                            and match('(.* (?=\d))(.*\) +)(.*$)', line)
            ])
        return {}

    def info(self, query):
        response = self.command('remote-info', query)[0].decode(*enc)
        if response and 'Unknown package' not in response:
            from re import match
            from string import strip
            res = [(map(strip, match('(\w*)(.*$)',line.replace('\n','')).groups()))
                    for line in response.splitlines()
                    if line
                       and 'PACKAGE' not in line
                       and '====' not in line
                       and match('(\w*)(.*$)',line)]
            return self.munge_lines(res)
        return ['Aborted: No info available']

    def install(self, query):
        self.shell('install', query)
        return {}

    @property
    def is_present(self):
        if super(self.__class__, self).is_present and self.command('-V','')[0]:
            return True
        return False
