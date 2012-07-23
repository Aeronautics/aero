from .base import BaseAdapter


class Apt(BaseAdapter):
    adapter_command = 'apt-get'
    search_command = 'apt-cache'

    def search(self, query):
        process = self._execute_command(self.search_command, ['search', 'python'])
        packages = []
        for line in process.stdout.read().split('\n'):
            if not line:
                continue
            packages.append({
                'name': line.split()[0],
                'description': ' '.join(line.split()[1:])
            })

