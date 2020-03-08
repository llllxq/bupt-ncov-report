__all__ = (
    'IFiller',
)

from abc import ABCMeta, abstractmethod
from typing import Mapping, MutableMapping, Optional

from ..predef import *


class IFiller(metaclass=ABCMeta):

    @abstractmethod
    def fill(
            self,
            config: MutableMapping[str, Optional[SupportedConfigType]],
            config_schema: Mapping[str, ConfigSchemaItem],
    ) -> None:
        """
        将该 filler 所读取的配置填入 config 中。
        若未读取到或读取失败（如：读取到的配置值不是数字，但其 type 为 int），则 config 中的值保持不变。
        :param config: dict，为填写的目标
        :return: None
        """
