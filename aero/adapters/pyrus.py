# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from aero.__version__ import __version__
from .base import BaseAdapter


class Pyrus(BaseAdapter):
    """
    Homebrew adapter.
    """
    def search(self, query):
        response = self.command('search', query)[0]
        if 'No formula found' not in response \
            and 'Error:' not in response\
            and 'No info available' not in response\
            and 'No results found' not in response:
            return dict([
                self.search_info(self.package_name(line))
                for line in response.splitlines()[4:-2] if line and 'pearhub.org' not in line
            ])
        return {}

    def search_info(self, query):
        response = self._execute_command('aero', ['info', query], False)[0]
        if 'No info available' not in response:
            from re import split
            info = [
                u''.join(split('\x1b.*?m', l)).replace(u'Summary:',u'').replace(u' : ', u'').strip()
                for l in response.splitlines()
                if 'Version:' in l or 'Summary:' in l
            ]
            if len(info) >= 1:
                info.insert(1, u'http://{}'.format(query.replace(self.package_name(u''), u'')))
            return [u'\n'.join(info) if len(info) else u'Aborted: No info available']
        return [u'Aborted No info available']

    def info(self, query):
        response = self.command('info', query)[0]
        if 'unknown channel' in response:
            self.command_no_passthru('channel-discover', '/'.join(query.split('/')[:-1]))
        response = self.command('info', query)[0]
        if 'does not exist' not in response and 'No results found' not in response:
            response = response.replace(
                'Package type: ', ''
            ).replace(
                'Package ', ''
            ).replace(
                ' Excerpt', ''
            )
            lst = []
            hold = []
            from string import strip
            for line in [l for l in response.splitlines()[4:] if l.strip() and not l.startswith('(`')]:
                if 'Version:' in line:
                    lst.extend(map(lambda x: map(strip, x.split(':')), line.split(',')))
                elif line.endswith(':'):
                    if len(hold):
                        lst.append(hold)
                    hold = [line[0:-1], u'']
                elif line.startswith('   ') and len(hold):
                    hold[1] += line.strip() + u' '
                else:
                    lst.append(line.split(u': '))
            if len(hold):
                lst.append(hold)
            return lst
        return [u'Aborted: No info available']

    def install(self, query):
        self.shell('install', query)
        return {}
