__author__ = 'nickl-'
from base import BaseAdapter
from subprocess import Popen
from subprocess import PIPE

class Port(BaseAdapter):
    adapter_command = 'port'

    def search(self, query):
        response = Popen(self.adapter_command + ' search ' + query, shell=True, stdout=PIPE).communicate()[0]
        lst = list(line for line in response.splitlines() if line)
        if lst:
            return dict(map(self.__parse_search, zip(*[iter(lst)]*2)))
        return {}

    def __parse_search(self, result):
        key = result[0].split(' ', 1)
        return [self.adapter_command + ':' + key.pop(0), key.pop() +' '+ result[1]]

    def install(self, query):
        print '\n';
        Popen(self.adapter_command + ' install ' + query, shell=True).wait()
        return {}
