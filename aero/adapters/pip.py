# -*- coding: utf-8 -*-
__author__ = 'nickl-'
from base import BaseAdapter
from subprocess import Popen
from subprocess import PIPE
from string import strip
class Pip(BaseAdapter):
    adapter_command = 'pip'

    def search(self, query):
        response = self._execute_command(self.adapter_command, ['search', query])[0]
        lst = [map(strip, (self.adapter_command + ':' + line).split(' - ', 1))
                for line in response.splitlines() if ' - ' in line]
        if lst:
            return dict(lst)
        return {}

    def install(self, query):
        print '\n'
        self._execute_shell(self.adapter_command, ['install', query])
        return {}