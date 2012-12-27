# -*- coding: utf-8 -*-
__author__ = 'nickl-'
__all__ = ('Port', )

from string import strip

from aero.__version__ import __version__, enc
from .base import BaseAdapter


class Port(BaseAdapter):
    """
    Macports adapter.
    """
    def search(self, query):
        response = self._execute_command('search', query)[0].decode(*enc)
        lst = list(line for line in response.splitlines() if line)
        if lst:
            return dict(map(
                self.__parse_search, zip(*[iter(lst)] * 2)
            ))
        return {}

    def __parse_search(self, result):
        key = result[0].split(' ', 1)
        return [
            self.package_name(key.pop(0)),
            key.pop() + ' ' + result[1]
        ]

    def install(self, query):
        return self.shell('install', query)

    def info(self, query):
        result = self.command('info', query)[0].decode(*enc)
        result = result.replace('{} '.format(query), 'Version: ')
        return [map(
            strip, line.split(': ', 1)
        ) for line in result.splitlines()]
