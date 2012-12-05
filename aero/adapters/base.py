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
    passthru = []

    def adapter_command(self):
        return self.__class__.__name__.lower()

    def _to_command(self, command, args=None, add_path=True):
        if add_path:
            command = os.path.join(self.path, command)
        command = [command]
        if args:
            assert isinstance(args, list)
            command += args
        return command

    def _execute_command(self, command, args=[], add_path=True):
        return subprocess.Popen(
            self._to_command(command, args, add_path),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ).communicate()

    def command(self, pm_command, query, args=[], add_path=True):
        args = pm_command.split(' ') + self.passthru + args + query.split(' ')
        return self._execute_command(self.adapter_command(), args, add_path)

    def _execute_shell(self, command, args=[], add_path=True):
        command = subprocess.list2cmdline(self._to_command(command, args, add_path))
        return subprocess.Popen(command, shell=True).wait()

    def shell(self, pm_command, query, args=[], add_path=True):
        args = pm_command.split(' ') + self.passthru + args + query.split(' ')
        self._execute_shell(self.adapter_command(), args, add_path)

    def package_name(self, package):
        return self.adapter_command()+':'+package

    def passthruArgs(self, args):
        self.passthru = [] if not isinstance(args, str) else args.split(' ')

    @abstractmethod
    def search(self, query):
        raise NotImplementedError

    @abstractmethod
    def install(self, package):
        raise NotImplementedError

    @abstractmethod
    def info(self, package):
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
            if os.path.exists(os.path.join(path, self.adapter_command())):
                self.path = path
                return True
        return False
