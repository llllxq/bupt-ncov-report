__all__ = (
    'INotifier',
)

from abc import ABCMeta, abstractmethod
from typing import Optional


class INotifier(metaclass=ABCMeta):
    """
    用于向指定的平台（如 Telegram、微信）发送通知的基类。
    主函数会调用 INotifier 的子类，向用户发送通知。
    """

    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """

    @abstractmethod
    def notify(self, *, success: bool, msg: Optional[str]) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """
