__all__ = (
    'RequestHistory',
    'MockResponse',
    'MockWhenWrapper',
    'MockRequestsSession',
)

import json
from typing import Any, Dict, List, MutableMapping, NamedTuple, Optional, Tuple


class RequestHistory(NamedTuple):
    """
    Session 的 mock 类支持「调用历史」功能。

    本类用于存放 session mock 类的 get、post 方法被调用时传入的参数。
    以下类成员与 requests 的 html 方法的参数一一对应；请查阅 requests 文档。
    除以下参数以外的参数会被忽略，不会存入本类中。
    """

    action: str
    url: str
    data: Optional[Dict[str, Any]]
    json: Optional[Dict[str, Any]]


class MockResponse(NamedTuple):
    """
    模拟 requests 中调用 get、set 所返回的 Response 对象。
    关于属性的作用，请参照 requests 的文档。
    """

    status_code: int
    text: str
    url: str

    def json(self) -> Dict[str, Any]:
        """
        将 text 属性当作 json 格式解析，转换为 dict。
        :return: dict
        """
        return json.loads(self.text)


class MockWhenWrapper:
    """
    为了实现 mock.when(...).respond(...) 语法，该类实现了 respond 方法。
    在调用 session mock 类的 when 方法时会返回本类实例。
    本类与 MockRequestsSession 强依赖。
    """

    def __init__(
            self, *,
            resp: MutableMapping[Tuple[str, str], MockResponse],
            url: str,
            action: str,
    ):
        """
        传入实现 mock 功能所必要的参数。
        :param resp: MockRequestsSession 中的 _resp 对象
        :param url: 用户在 when 中指定的 url
        :param action: 用户在 when 中指定的 action
        """
        self._resp = resp
        self._url = url
        self._action = action

    def respond(self, *, status_code: int = 200, text: str = '', url: Optional[str] = None):
        if url is None:
            url = self._url

        self._resp[self._action, self._url] = MockResponse(status_code, text, url)


class MockRequestsSession:
    """
    该类用于模拟 requests 的 Session 类。

    该类的 API 设计模仿了著名 Java mocking 库 Mockito，允许用户用 mock.when(...).respond(...)
    的方式来表示「当访问某 url 时，返回的 Response 对象内容是……」。
    """

    def __init__(self):
        """初始化私有属性"""
        self._resp: MutableMapping[Tuple[str, str], MockResponse] = {}
        self._history: List[RequestHistory] = []

    def history(self) -> List[RequestHistory]:
        """返回该类被调用的历史"""
        return self._history.copy()

    def find_history(self, url) -> List[RequestHistory]:
        """
        查找访问该 URL 的调用历史。
        :param url: URL
        :return 调用历史列表；当没有调用历史时，返回空列表
        """
        return [x for x in self._history if x.url == url]

    def last_request(self) -> RequestHistory:
        """
        返回该类被最后一次调用的历史。
        当没被调用过时，抛出异常。
        :return: 调用历史
        """
        if len(self._history) == 0:
            raise ValueError('No any history')

        return self._history[-1]

    def get(self, url, *args, **kwargs):
        """模拟的 get 方法。该方法会记录调用历史。"""
        self._history.append(RequestHistory('get', url, None, None))

        resp = self._resp.get(('get', url))
        if resp is None:
            raise RuntimeError(f'UrlNotFoundError: when try to get {url}')

        return resp

    def post(self, url, data=None, json=None, *args, **kwargs):
        """模拟的 post 方法。该方法会记录调用历史。"""
        self._history.append(RequestHistory('post', url, data, json))

        resp = self._resp.get(('post', url))
        if resp is None:
            raise RuntimeError(f'UrlNotFoundError: when try to post to {url}')

        return resp

    def when(self, *, action: str, url: str) -> MockWhenWrapper:
        """
        用于注册调用 get/post 时的返回值。
        :param action: 字符串，只能为 get 或 post；若 action 为 post，则 get 此 url 时不会返回该值
        :param url: get/post 的 URL（精确匹配，大小写敏感）
        :return: MockWhenWrapper
        """
        action = action.lower()
        assert action == 'post' or action == 'get'

        return MockWhenWrapper(
            resp=self._resp,
            url=url,
            action=action
        )
