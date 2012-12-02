# -*- coding: utf-8 -*-
#noinspection PyPackageRequirements
import aero
from aero.__version__ import __version__


class MAdapterRegistration(type):
    """
    Registers an adapter which uses this metaclass.
    """
    adapters = {}

    def __new__(meta, name, bases, attrs):
        cls = type.__new__(meta, name, bases, attrs)

        if not name in meta.adapters:
            """
            Already stores an instance of adapter.
            """
            meta.adapters[name] = cls()

        return cls

# Importing so it will be registered
from .apt import Apt
from .brew import Brew
from .port import Port
from .pip import Pip
from .npm import Npm
from .gem import Gem
from .pear import Pear
from .pecl import Pecl

__all__ = ['AVAILABLE_ADAPTERS']

AVAILABLE_ADAPTERS = [(adapter_name, adapter) for (adapter_name, adapter) in MAdapterRegistration.adapters.items() if adapter.is_present]
