# -*- coding: utf-8 -*-
from aero.__version__ import __version__
from .base import BaseAdapter


class Apt(BaseAdapter):
    """
    apt-get adapter
    """
    search_command = 'apt-cache'

    def adapter_command(self):
        return 'apt-get'

    def search(self, query):
        process = self._execute_command(self.search_command, ['search', query])
        print '{:<40}{}'.format('Name', 'Description')
        for line in process[0].splitlines():
            if not line:
                continue
            print '{:<40}{}'.format(line.split()[0], ' '.join(line.split()[2:]))
