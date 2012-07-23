import os
import subprocess


class BaseAdapter(object):
    adapter_command = 'base'

    def _execute_command(self, command, args=None):
        command = [command]
        if args:
            assert isinstance(args, list)
            command += args

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return process


    def search(self, query):
        raise NotImplementedError

    def install(self, package):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def upgrade(self, query=None):
        raise NotImplementedError

    @property
    def is_present(self):
        for path in os.environ['PATH'].split(':'):
            if os.path.exists(os.path.join(path, self.adapter_command)):
                self.path = path
                return True

        return False
