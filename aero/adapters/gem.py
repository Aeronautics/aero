# -*- coding: utf-8 -*-
__author__ = 'nickl-'
from base import BaseAdapter
from subprocess import Popen
from subprocess import PIPE
from string import strip
class Gem(BaseAdapter):
    adapter_command = 'gem'

    def search(self, query):
        response = self._execute_command(self.adapter_command, ['search', '-qbd', query])[0]
        import re
        rlines = re.sub('\*\*\*.*\*\*\*\s+', '', response).splitlines()
        lst = {}
        for key, val in [line.split(' ', 1) for line in rlines if line and not line.startswith('  ')]:
            i = rlines.index(key+' '+val) + 1
            key = self.adapter_command+':'+key
            try: lst[key] += '\n\n'
            except KeyError: lst[key] = ''
            val = ['version: '+val]
            while (i < len(rlines) and rlines[i].startswith(' ')):
                val += [rlines[i].strip()]
                i += 1
            lst[key] += '\n'.join(val)
        return lst

    def install(self, query):
        print '\n'
        self._execute_shell(self.adapter_command, ['install', query]).wait()
        return {}
