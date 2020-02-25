__all__ = (
    'ConfigValue',
    'VerifiedData',
)

from typing import Any, Dict, NewType, TypeVar, Union

ConfigValue = Union[str, bool, int]

TConfigValue = TypeVar('TConfigValue', bound=ConfigValue)

VerifiedData = NewType('VerifiedData', Dict[str, Any])
