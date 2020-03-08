__all__ = (
    'PureUtils',
)

import re
from typing import Any, Tuple


class PureUtils:
    """与疫情上报网站无关的工具函数。可以将同一个本类的实例注入到多个类中。"""

    @staticmethod
    def is_number_data_in_range(data: Any, range: Tuple[int, int]) -> bool:
        """
        检查 data 所表示的十进制数字是否在 range 所表示的前闭后开区间内。
        :param data: 数字，或可转换为数字的类型
        :param range: 前闭后开区间
        :return: True/False 表示是/否在区间内
        """
        if isinstance(data, int):
            int_data = data
        else:
            try:
                int_data = int(data)
            except:
                return False

        return range[0] <= int_data < range[1]

    @staticmethod
    def match_re_group1(re_str: str, text: str) -> str:
        """
        在 text 中匹配正则表达式 re_str，返回第 1 个捕获组（即首个用括号包住的捕获组）
        :param re_str: 正则表达式（字符串）
        :param text: 要被匹配的文本
        :return: 第 1 个捕获组捕获到的内容（字符串）
        """
        match = re.search(re_str, text)
        if match is None:
            raise ValueError(f'在文本中匹配 {re_str} 失败，没找到任何东西。\n请阅读脚本文档中的「使用前提」部分。')

        return match.group(1)

    @staticmethod
    def looks_falsy(x: Any) -> bool:
        """
        判断传入的参数是否看起来像是 False。
        参考：https://dorey.github.io/JavaScript-Equality-Table/

        使用例：
        >>> PureUtils.looks_falsy('false')
        True
        >>> PureUtils.looks_falsy('1')
        False
        >>> PureUtils.looks_falsy(dict())
        True
        >>> PureUtils.looks_falsy([0])
        True

        :param x: 几乎任意参数
        :return: 如果看起来像 False，则返回 True
        """
        FALSY_OBJECTS = (
            '0', 'false', 'False', [0],
        )

        if isinstance(x, str):
            x = x.lower().strip()

        if bool(x) == False:
            return True
        for i in FALSY_OBJECTS:
            if x == i:
                return True

        return False

    @staticmethod
    def looks_truthy(x: Any) -> bool:
        """
        判断传入的参数是否看起来像是 False。
        参考：https://dorey.github.io/JavaScript-Equality-Table/

        使用例：
        >>> PureUtils.looks_truthy('false')
        False
        >>> PureUtils.looks_truthy('1')
        True
        >>> PureUtils.looks_truthy(dict())
        False
        >>> PureUtils.looks_truthy([0])
        False

        :param x: 几乎任意参数
        :return: 如果看起来像 True，则返回 True
        """
        return not PureUtils.looks_falsy(x)
