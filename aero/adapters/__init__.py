# -*- coding: utf-8 -*-
#noinspection PyPackageRequirements
import aero
from aero.__version__ import __version__

from .apt import Apt
from .brew import Brew
from .port import Port
from .pip import Pip
from .npm import Npm
from .gem import Gem
__all__ = ['AVAILABLE_ADAPTERS']

POSSIBLE_ADAPTERS = (Apt(), Brew(), Port(), Pip(), Npm(), Gem())
AVAILABLE_ADAPTERS = [adapter for adapter in POSSIBLE_ADAPTERS if adapter.is_present]
