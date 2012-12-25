# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from aero.__version__ import __version__, enc
from .base import BaseAdapter


class Brew(BaseAdapter):
    """
    Homebrew adapter.
    """
    def search(self, query):
        response = self.command('search', query)[0].decode(*enc)
        if 'No formula found' not in response and 'Error:' not in response:
            return dict([(
                self.package_name(line),
                self.search_info(self.package_name(line))
            ) for line in response.splitlines() if line])
        return {}

    def search_info(self, query):
        response = self._execute_command('aero', ['info', query], False)[0].decode(*enc)
        from re import split
        lines = response.splitlines()
        idx = 0
        for x in lines:
            if x.find(u'─┬─') > -1:
                break
            idx += 1
        return '\n'.join([''.join(split('\x1b.*?m', l)).replace(u' │ ', '').strip() for l in lines[idx+1:idx+4]])

    def info(self, query):
        if '/' in query:
            self.command_no_passthru('tap', '/'.join(query.split('/')[:-1]))
        response = self.command('info', query)[0].decode(*enc)
        if 'Error:' not in response:
            response = response.replace(query + ': ', 'version: ')
            return [line.split(': ', 1) for line in response.splitlines() if 'homebrew' not in line]
        return [['No info available']]

    def install(self, query):
        self.shell('install', query)
        return {}
