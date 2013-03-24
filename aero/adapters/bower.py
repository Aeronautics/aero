# -*- coding: utf-8 -*-
__author__ = 'oliveiraev'
__all__ = ['Bower']

from re import sub
from re import split
from aero.__version__ import enc
from .base import BaseAdapter


class Bower(BaseAdapter):
    """
    Twitter Bower - Browser package manager - Adapter
    """
    def search(self, query):
        response = self.command('search', query)[0].decode(*enc)
        lst = list(
            self.__parse_search(line) for line in response.splitlines()
            if line.startswith('  - ')
        )
        if lst:
            return dict([(k, v) for k, v in lst if k != 0])
        return {}

    def __parse_search(self, result):
        result = split('\[\d\dm', result, 2)
        if isinstance(result, (list, tuple)) and len(result) > 1:
            return self.package_name(result[1][:-1]), '\n'
        return 0, 0

    def install(self, query):
        return self.shell('install', query)

    def info(self, query):
        response = self.command('view', query)[0].decode(*enc)
        return response or ['Aborted: No info available']
