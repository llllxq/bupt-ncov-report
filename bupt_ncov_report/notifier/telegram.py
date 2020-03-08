__all__ = (
    'TelegramNotifier',
)

import html
import logging
from typing import Optional

import requests

from .base import *
from ..constant import *

logger = logging.getLogger(__name__)


class TelegramNotifier(INotifier):
    PLATFORM_NAME = 'Telegram 机器人'

    def __init__(self, *, token: str, chat_id: str, session: requests.Session):
        """
        :param token: Telegram Bot Token
        :param chat_id: 要发送到的 chat_id；如果要发送给您自己，请设为您的 user id（可通过多种方式获取）
        """
        self._token = token
        self._chat_id = chat_id
        self._sess = session

    def notify(self, *, success: bool, msg: Optional[str]) -> None:
        PREFIX = '[bupt-ncov-report] '

        if msg is not None:
            if success:
                body = f'<b>成功：</b>服务器的返回是：\n\n<pre>{html.escape(msg)}</pre>'
            else:
                body = f'<b>失败：</b>产生如下异常：\n\n<pre>{html.escape(msg)}</pre>'
        else:
            body = '<b>成功</b>' if success else '<b>失败</b>'

        self._send(f'{PREFIX}{body}')

    def _send(self, msg: Optional[str]) -> None:
        """发送消息。"""
        tg_res_raw = self._sess.post(
            f'https://api.telegram.org/bot{self._token}/sendMessage',
            json={
                'chat_id': self._chat_id,
                'text': msg,
                'parse_mode': 'HTML',
            },
            timeout=TIMEOUT_SECOND,
        )

        # 处理可能出现的异常情况
        try:
            tg_res = tg_res_raw.json()
        except:
            raise RuntimeError(f'Telegram API 的返回值不能解析为 JSON。返回值为：\n{tg_res_raw.text}')

        if 'ok' not in tg_res:
            raise RuntimeError(f'Telegram API 的返回值很奇怪，可能您的 Token 或 chat id 配置有误。'
                               f'API 的返回是：\n{tg_res}')
        if not tg_res['ok']:
            raise RuntimeError(f'Telegram API 调用失败，可能您的 Token 或 chat id 配置有误。'
                               f'API 的返回是：\n{tg_res}')
