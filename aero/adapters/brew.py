# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from aero.__version__ import __version__
from .base import BaseAdapter


class Brew(BaseAdapter):
    """
    Homebrew adapter.
    """
    def search(self, query):
        response = self.command(['search', query])[0]
        if 'No formula found' not in response and 'Error:' not in response:
            return dict([(
                self.package_name(line),
                '\n'.join(map(
                    lambda k: k[0] if len(k) < 2 else k[0] + ': ' + k[1],
                    self.search_info(line)
                ))
            ) for line in response.splitlines() if line])
        return {}

    def search_info(self, query):
        info = self.info(query)
        return filter(
            None,
            [
                info[0],
                info[1] if len(info) > 1 else None,
                info[2] if len(info) > 2 else None,
            ]
        )

    def info(self, query):
        if '/' in query:
            self.command(['tap', '/'.join(query.split('/')[:-1])])
        response = self.command(['info', query])[0]
        if 'Error:' not in response:
            response = response.replace(query + ': ', 'version: ')
            return [line.split(': ', 1) for line in response.splitlines() if 'homebrew' not in line]
        return [['No info available']]

    def install(self, query):
        self.shell(['install', query])
        return {}
