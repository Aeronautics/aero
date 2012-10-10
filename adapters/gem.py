__author__ = 'nickl-'
from base import BaseAdapter
from subprocess import Popen
from subprocess import PIPE
from string import strip
class Gem(BaseAdapter):
    adapter_command = 'gem'

    def search(self, query):
        response = Popen(self.adapter_command + ' search -qbd ' + query + '| awk \'NF{if(!index($0,"***")&&!index($0,"Rubyforge")) {print}}\'', shell=True, stdout=PIPE).communicate()[0]
        rlines = response.splitlines()
        lst = {}
        for key in list(line for line in rlines if line and not line.startswith('  ')):
            val = ''
            i = rlines.index(key) + 1
            while (i < len(rlines) and rlines[i].startswith('  ')):
                val += ' '+rlines[i].strip()
                i += 1
            key = (self.adapter_command+':'+key).split(' ')
            lst[key.pop(0)] = key.pop() + val

        if lst:
            return dict(lst)
        return {}

    def install(self, query):
        print '\n'
        Popen(self.adapter_command + ' install ' + query, shell=True).wait()
        return {}
