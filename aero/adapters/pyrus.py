# -*- coding: utf-8 -*-
__author__ = 'nickl-'

from aero.__version__ import __version__, enc
from .base import BaseAdapter


class Pyrus(BaseAdapter):
    """
    Pyrus adapter.
    """
    def search(self, query):
        response = self.command('search', query)[0].decode(*enc)
        if 'No results found' not in response:
            return dict([
                self.search_info(self.package_name(line))
                for line in response.splitlines()[4:-2] if line and 'pearhub.org' not in line
            ])
        return {}

    def search_info(self, query):
        response = self._execute_command('aero', ['info', query], False)[0].decode(*enc)
        if 'Aborted:' not in response:
            from re import split
            info = [
                ''.join(split('\x1b.*?m', l)).replace('Summary:','').replace(u' │ ', '').strip()
                for l in response.splitlines()
                if 'Version:' in l or 'Summary:' in l
            ]
            if len(info) >= 1:
                info.insert(1, 'http://{}'.format(query.replace(self.package_name(''), '')))
            return [query, '\n'.join(info) if len(info) else 'Aborted: No info available']
        return [query, 'Aborted: No info available']

    def info(self, package):
        query = package + '-alpha'
        response = self.command('info', query)[0].decode(*enc)
        if 'unknown channel' in response[0]:
            self.command_no_passthru('channel-discover', '/'.join(query.split('/')[:-1]))
            response = self.command('info', query)[0].decode(*enc)
        response = response[response.index('Package type:'):-1]
        if 'does not exist' not in response and 'No results found' not in response:
            response = response.replace(
                'Package type: ', ''
            ).replace(
                'Package ', ''
            ).replace(
                ' Excerpt', ''
            )
            lines = [l for l in response.splitlines()
                     if l
                        and not l.startswith('PHP ')
                        and 'Notice:' not in l
                        and 'Call Stack:' not in l
            and 'pyrus.phar:' not in l]
            lst = []
            hold = []
            from string import strip
            for line in [l for l in lines if l.strip() and not l.startswith('(`')]:
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
        return ['Aborted: No info available for ' + package]

    def install(self, query):
        self.shell('install', query)
        return {}
