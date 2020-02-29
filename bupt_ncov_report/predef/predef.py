__all__ = (
    'ConfigValue',
    'VerifiedData',
)

from typing import Any, Dict, NewType, Union

ConfigValue = Union[str, bool, int]

VerifiedData = NewType('VerifiedData', Dict[str, Any])
