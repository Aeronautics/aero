# -*- coding: utf-8 -*-
from .base import BaseAdapter
import textwrap

class Brew(BaseAdapter):
    adapter_command = 'brew'

    def search(self, query):
        response = self._execute_command(self.adapter_command, ['search', query])[0]
        if 'No formula found' not in response and 'Error:' not in response:
            return dict([(self.adapter_command + ':' + line, self.info(line))
                         for line in response.splitlines() if line])
        return {}

    def info(self, query):
        response = self._execute_command(self.adapter_command, ['info', query])[0]
        if 'Error:' not in response:
            return '\n'.join([line for line in response.splitlines() if 'homebrew' not in line])
        return 'No info available'

    def install(self, query):
        print '\n'
        self._execute_command(self.adapter_command, ['search', query])
        return {}
