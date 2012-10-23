# -*- coding: utf-8 -*-
from aero.__version__ import __version__
from .base import BaseAdapter


class Apt(BaseAdapter):
    """
    apt-get adapter
    """
    adapter_command = 'apt-get'
    search_command = 'apt-cache'

    def search(self, query):
        process = self._execute_command(self.search_command, ['search', query])
        print '{:<40}{}'.format('Name', 'Description')
        for line in process[0].splitlines():
            if not line:
                continue
            print '{:<40}{}'.format(line.split()[0], ' '.join(line.split()[2:]))
