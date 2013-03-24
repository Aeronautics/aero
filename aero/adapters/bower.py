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
        lst = list(
            if line.startswith('  - ')
        )
        if lst:
            return dict([(k, v) for k, v in lst if k != 0])
        return {}

        response = self.command('search', query, ['--no-color'])[0].decode(*enc)
            line.lstrip(' -').split(' ') for line in response.splitlines()

    def install(self, query):
        return self.shell('install', query)

    def info(self, query):
        response = self.command('view', query, ['--no-color'])[0].decode(*enc)
        return response or ['Aborted: No info available']
