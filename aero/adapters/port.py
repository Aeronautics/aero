# -*- coding: utf-8 -*-
__author__ = 'nickl-'
from base import BaseAdapter
from subprocess import Popen
from subprocess import PIPE

class Port(BaseAdapter):
    adapter_command = 'port'

    def search(self, query):
        response = self._execute_command(self.adapter_command, ['search', query])[0]
        lst = list(line for line in response.splitlines() if line)
        if lst:
            return dict(map(self.__parse_search, zip(*[iter(lst)]*2)))
        return {}

    def __parse_search(self, result):
        key = result[0].split(' ', 1)
        return [self.adapter_command + ':' + key.pop(0), key.pop() +' '+ result[1]]

    def install(self, query):
        print '\n';
        self._execute_shell(self.adapter_command, ['install', query])
        return {}

    def info(self, query):
        return self._execute_command(self.adapter_command, ['info', query])[0]
