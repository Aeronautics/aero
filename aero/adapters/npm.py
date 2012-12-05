# -*- coding: utf-8 -*-
__author__ = 'nickl-'
__all__ = ('Npm', )

from string import strip
from re import match, sub

from aero.__version__ import __version__
from .base import BaseAdapter


class Npm(BaseAdapter):
    """
    Node package manager adapter.
    """
    def search(self, query):
        response = self.command('search -q', query)[0]
        lst = list(
            self.__parse_search(line) for line in response.splitlines()
            if 'npm http' not in line and not bool(match(
                '^NAME\s+DESCRIPTION\s+AUTHOR\s+DATE\s+KEYWORDS', line
            ))
        )
        if lst:
            return dict([(k, v) for k, v in lst if k != 0])
        return {}

    def __parse_search(self, result):
        r = match(
            '^([A-Za-z0-9\-]*)\s+(\w.*)=(.+)\s+(\d\d\d\d[\d\-: ]*)\s*?(\w?.*?)$',
            result
        )
        if r and len(r.groups()) == 5:
            r = map(strip, list(r.groups()))
            pkg = self.package_name(r.pop(0))
            return pkg, r[2] + '\n' + r[0]
        return 0, 0

    def install(self, query):
        self.shell(['install', query])
        return {}

    def info(self, query):
        response = self.command('view', query)[0]
        try:
            import json
            r = json.loads(sub("'", '"', sub('\s(\w+):', r' "\1":', response.strip())))
            response = []
            for k in sorted(r):
                if isinstance(r[k], dict):
                    r[k] = '\n'.join([': '.join(list(l)) for l in r[k].items()])
                elif isinstance(r[k], list):
                    r[k] = ', '.join(r[k])
                if r[k]:
                    response.append((k, str(r[k])))
            return response
        except ValueError:
            return 'No info available'
