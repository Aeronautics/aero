# -*- coding: utf-8 -*-
import os
import subprocess

from abc import abstractmethod

from aero.__version__ import __version__
from . import MAdapterRegistration


class BaseAdapter(object):
    """
    Base adapter.
    """
    __metaclass__ = MAdapterRegistration
    adapter_command = 'base'
    passthru = []

    def _to_command(self, command, args=None, add_path=True):
        if add_path:
            command = os.path.join(self.path, command)
        command = [command]
        if args:
            assert isinstance(args, list)
            command += args
        return command

    def _execute_command(self, command, args=[], add_path=True):
        args += self.passthru
        return subprocess.Popen(self._to_command(command, args, add_path),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    def _execute_shell(self, command, args=[], add_path=True):
        args += self.passthru
        command = subprocess.list2cmdline(self._to_command(command, args, add_path))
        return subprocess.Popen(command, shell=True).wait()

    def passthruArgs(self, args):
        self.passthru = [] if not isinstance(args, str) else args.split(' ')

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
