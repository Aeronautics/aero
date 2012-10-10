from .base import BaseAdapter
from subprocess import Popen
from subprocess import PIPE


class Brew(BaseAdapter):
    adapter_command = 'brew'

    def search(self, query):
        response = Popen(self.adapter_command + ' search ' + query, shell=True, stdout=PIPE).communicate()[0]
        if 'No formula found' not in response:
            return dict(list((self.adapter_command + ':' + line, self.__parse_search(line)) for line in response.splitlines() if line))
        return {}

    def __parse_search(self, query):
        response = Popen(self.adapter_command + ' info ' + query, shell=True, stdout=PIPE).communicate()[0]
        return ' '.join(list(line for line in response.splitlines() if 'homebrew' not in line))

    def install(self, query):
        print '\n'
        Popen(self.adapter_command + ' install ' + query, shell=True).wait()
        return {}