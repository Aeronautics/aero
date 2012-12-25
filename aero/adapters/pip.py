# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from string import strip
from aero.__version__ import __version__, enc
from importlib import import_module
from .base import BaseAdapter


class Pip(BaseAdapter):
    """
    Pip adapter.
    """
    def search(self, query):
        m = import_module('pip.commands.search')
        lst = {}
        for r in m.transform_hits(m.SearchCommand().search(query, 'http://pypi.python.org/pypi')):
            summary = u' '.join(map(strip, r['summary'].split('\n') if r['summary'] else [''])).replace('  ', ' ')
            lst[self.package_name(r['name'])] = 'Version: {:<12} Score:{:>4}\n{}'.format(
                m.highest_version(r['versions']),
                r['score'],
                (summary.encode(*enc) if len(summary) < 200 else summary[:190] + '...').replace('  ', ' ')
            )
        return lst

    def install(self, query):
        import_module('pip').main([
            'install',
            '--force-reinstall',
            '--upgrade',
            '--timeout', '30',
            '--egg',
            '--log', '~/.aero/log/pip.log',
            '--download-cache', '~/.aero/cache/pip',
        ] + self.passthru + [query])
        return {}

    def info(self, query):
        try:
            import os
            finder = import_module('pip.index').PackageFinder([] , ['http://pypi.python.org/simple/'])
            m = import_module('pip.req')
            pi = m.InstallRequirement(query, '' )
            pr = m.RequirementSet(os.path.expanduser('~') + '/.aero/pkg_info/' , '' , None)
            pr.add_requirement(pi)
            pr.prepare_files(finder)
            return pi.pkg_info().items()
        except import_module('pip.exceptions').InstallationError:
            return ['Aborted: No info available']
