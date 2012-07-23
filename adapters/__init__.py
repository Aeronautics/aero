from .apt import Apt
from .brew import Brew

__all__ = ['AVAILABLE_ADAPTERS']

POSSIBLE_ADAPTERS = (Apt(), Brew())
AVAILABLE_ADAPTERS = [adapter for adapter in POSSIBLE_ADAPTERS if adapter.is_present]
