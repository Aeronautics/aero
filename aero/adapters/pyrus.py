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
                ''.join(split('\x1b.*?m', l)).replace('Summary:','').replace(' : ', '').strip()
                for l in response.splitlines()
                if 'Version:' in l or 'Summary:' in l
            ]
            if len(info) >= 1:
                info.insert(1, 'http://{}'.format(query.replace(self.package_name(''), '')))
            return (query, '\n'.join(info) if len(info) else 'No info available')
        return (query, 'No info available')

    def info(self, query):
        response = self.command('info', query)[0]
        if 'unknown channel' in response:
            self.command(['channel-discover', query.split('/')[0]])
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
                    hold = [line[0:-1], '']
                elif line.startswith('   ') and len(hold):
                    hold[1] += line.strip() + ' '
                else:
                    lst.append(line.split(': '))
            if len(hold):
                lst.append(hold)
            return lst
        return [['No info available']]

    def install(self, query):
        self.shell(['install', query])
        return {}
