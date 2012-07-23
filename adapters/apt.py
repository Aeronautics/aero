from .base import BaseAdapter


class Apt(BaseAdapter):
    adapter_command = 'apt-get'
    search_command = 'apt-cache'

    def search(self, query):
        process = self._execute_command(self.search_command, ['search', query])
        packages = []
        print '%-40s%s' % ('Name', 'Description')
        for line in process.stdout.read().split('\n'):
            if not line:
                continue
            print '%-40s%s' % (line.split()[0], ' '.join(line.split()[2:]))
