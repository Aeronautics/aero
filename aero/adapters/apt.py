# -*- coding: utf-8 -*-
from aero.__version__ import __version__, enc
from .base import BaseAdapter


class Apt(BaseAdapter):
    """
    apt-get adapter
    """
    search_command = 'apt-cache'

    def adapter_command(self):
        return 'apt-get'

    def search(self, query):
        response = self._execute_command(self.search_command, ['search', query])[0].decode(*enc)
        lst = {}
        from re import match
        lst.update([
            match('^([^ ]*) - (.*)', 'apt:'+line).groups()
            for line in response.splitlines()
            if match('^([^ ]*) - (.*)', line)
        ])
        return lst

    def info(self, query):
        response = self._execute_command(self.search_command, ['show', query])[0].decode(*enc)
        lst = [
            line.split(': ') if line.find(': ') > 0 else ('',line)
            for line in response.splitlines()
        ]
        return self.munge_lines(lst)

    def install(self, query):
        self.shell('install', query)
        return {}
