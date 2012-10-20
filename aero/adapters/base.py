# -*- coding: utf-8 -*-
from aero.__version__ import __version__
from abc import abstractmethod
import os
import subprocess



class BaseAdapter(object):
    adapter_command = 'base'

    def _to_command(self, command, args=None, add_path=True):
        if add_path:
            command = os.path.join(self.path, command)
        command = [command]
        if args:
            assert isinstance(args, list)
            command += args
        return command

    def _execute_command(self, command, args=None, add_path=True):
        return subprocess.Popen(self._to_command(command, args, add_path),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    def _execute_shell(self, command, args=None, add_path=True):
        command = subprocess.list2cmdline(self._to_command(command, args, add_path))
        return subprocess.Popen(command, shell=True).wait()

    @abstractmethod
    def search(self, query):
        raise NotImplementedError

    @abstractmethod
    def install(self, package):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def upgrade(self, query=None):
        raise NotImplementedError

    @property
    def is_present(self):
        for path in os.environ['PATH'].split(':'):
            if os.path.exists(os.path.join(path, self.adapter_command)):
                self.path = path
                return True
        return False
