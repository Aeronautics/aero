# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from aero.__version__ import __version__
from .base import BaseAdapter


class Brew(BaseAdapter):
    """
    Homebrew adapter.
    """
    adapter_command = 'brew'

    def search(self, query):
        response = self._execute_command(self.adapter_command, ['search', query])[0]
        if 'No formula found' not in response and 'Error:' not in response:
            return dict([(
                self.adapter_command + ':' + line,
                '\n'.join(map(
                    lambda k: k[0] if len(k) < 2 else k[0] + ': ' + k[1],
                    self.info(line)
                ))
            ) for line in response.splitlines() if line])
        return {}

    def info(self, query):
        if '/' in query:
            self._execute_command(self.adapter_command, ['tap', '/'.join(query.split('/')[:-1])])
        response = self._execute_command(self.adapter_command, ['info', query])[0]
        if 'Error:' not in response:
            response = response.replace(query + ': ', 'version: ')
            return [line.split(': ', 1) for line in response.splitlines() if 'homebrew' not in line]
        return [['No info available']]

    def install(self, query):
        print
        self._execute_shell(self.adapter_command, ['install', query])
        return {}
