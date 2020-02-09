import json
import os
import tempfile
import unittest
from collections import namedtuple
from typing import List

import main

RequestHistory = namedtuple('RequestHistory', [
    'action', 'url', 'data', 'json'
])

MockWhenWrapper = namedtuple('MockWhenWrapper', [
    'respond'
])


class MockResponse(namedtuple('MockResponse', ['status_code', 'text', 'url'])):
    def json(self):
        return json.loads(self.text)


class MockRequestsSession:
    def __init__(self):
        self._resp = {}
        self._history: List[RequestHistory] = []

    def history(self) -> List[RequestHistory]:
        return self._history.copy()

    def find_history(self, url):
        return [x for x in self._history if x.url == url]

    def last_request(self) -> RequestHistory:
        if len(self._history) == 0:
            raise ValueError('No any history')

        return self._history[-1]

    def get(self, url, *args, **kwargs):
        self._history.append(RequestHistory('get', url, None, None))

        resp = self._resp.get(('get', url))
        if resp is None:
            return MockResponse(status_code=200, text='', url=url)

        return resp

    def post(self, url, data=None, json=None, *args, **kwargs):
        self._history.append(RequestHistory('post', url, data, json))

        resp = self._resp.get(('post', url))
        if resp is None:
            return MockResponse(status_code=200, text='', url=url)

        return resp

    def when(self, action: str, url: str) -> MockWhenWrapper:
        action = action.lower()
        assert action == 'post' or action == 'get'

        def respond(status_code=200, text='', url=url):
            self._resp[action, url] = MockResponse(status_code, text, url)

        return MockWhenWrapper(respond)


class TestUnit_UtilFunctions(unittest.TestCase):
    MOCK_SCHEMA = {
        'FUCK': {
            'description': '123',
            'for_short': 'f',
            'default': 233,
        },
        'SHIT_HOLE': {
            'description': 'shit hole',
            'for_short': 'sh',
            'default': None,
        },
    }

    def test_initializeConfig(self):
        config = {}
        main.initialize_config(config, self.MOCK_SCHEMA)

        self.assertEqual(config, {
            'FUCK': 233,
            'SHIT_HOLE': None,
        })

    def test_fillConfigWithEnv(self):
        original_config = {
            'FUCK': 233,
            'SHIT_HOLE': None,
        }
        config = original_config

        main.fill_config_with_env(config, {})
        self.assertEqual(config, original_config)

        main.fill_config_with_env(config, {
            'FUCK': 'abc',
            'SHIT': 'def',
        })
        self.assertEqual(config, {
            'FUCK': 'abc',
            'SHIT_HOLE': None,
        })

    def test_fillConfigWithArgparse(self):
        original_config = {
            'FUCK': 233,
            'SHIT_HOLE': None,
        }
        config = original_config

        main.fill_config_with_argparse(config, self.MOCK_SCHEMA, [])
        self.assertEqual(config, original_config)

        main.fill_config_with_argparse(config, self.MOCK_SCHEMA, [
            '--fuck', 'abc'
        ])
        self.assertEqual(config, {
            'FUCK': 'abc',
            'SHIT_HOLE': None,
        })

    def test_configTypeConsistency(self):
        config = {
            '1': 1,
            '2': 'a',
            '3': None,
            '4': '',
        }

        main.config_type_consistency(config)
        self.assertEqual(config, {
            '1': None,
            '2': 'a',
            '3': None,
            '4': None,
        })

    def test_matchReGroup1(self):
        self.assertEqual(main.match_re_group1(r'abc(\d+)def', 'abc1234def'), '1234')
        with self.assertRaises(BaseException) as _ctxt:
            main.match_re_group1(r'abc(\d+)def', 'abcdef')

    def test_extractPostData(self):
        html = '''
            var def = {"fuck": 0, "shit": 2, "damn": "a"};
            var app = new Vue({
                data: {
                    oldInfo: {"fuck": "abc", "shit": "1"},
                }
            })
        '''
        post_data = main.extract_post_data(html)
        self.assertEqual(post_data, {
            'fuck': 0,
            'shit': 2,
            'damn': 'a',
        })


class TestFeature(unittest.TestCase):
    LOGIN_API_RESP = r'''{"e":0,"m":"操作成功","d":{}}'''
    REPORT_API_RESP = r'''{"e":1,"m":"今天已经填报了","d":{}, "f": "FeatureTest"}'''
    REPORT_PAGE_HTML = r'''
        <!DOCTYPE html>
        <html lang="zh-CN">
        
        <head>
          <title>每日上报</title>
        </head>
        
        <body class="">
        
          <script type="text/javascript">
            var def = { "fuck": "bitch", "shit_hole": 1, "damn": "a" };
            var vm = new Vue({
              el: '.form-detail2',
              data: {
                realname: '田所浩二',
                number: '2020114514',
                date: '2020-02-08',
                info: $.extend({ ismoved: 0 }, def),
                oldInfo: { "fuck": 0, "shit": "1" },
                tipMsg: '',
                ajaxLock: false,
                showFxyy: false,
                hasFlag: '1',
              }
            });
        
          </script>
        </body>
        
        </html>
    '''
    TG_API_RESP = r'''{"ok": true}'''

    def setUp(self) -> None:
        log_fd, self.log_path = tempfile.mkstemp(suffix='.log')
        os.close(log_fd)

        os.environ['BUPT_SSO_USER'] = '2020114514'
        os.environ['BUPT_SSO_PASS'] = '114514'
        os.environ['TG_BOT_TOKEN'] = '114514:abcdef'
        os.environ['TG_CHAT_ID'] = '1145141919810'
        os.environ['BNR_LOG_PATH'] = self.log_path

        self.session = MockRequestsSession()
        self.session.when('POST', main.LOGIN_API).respond(text=self.LOGIN_API_RESP)
        self.session.when('GET', main.REPORT_PAGE).respond(text=self.REPORT_PAGE_HTML)
        self.session.when('POST', main.REPORT_API).respond(text=self.REPORT_API_RESP)
        self.session.when(
            'POST', 'https://api.telegram.org/bot114514:abcdef/sendMessage'
        ).respond(text=self.TG_API_RESP)
        main.set_session(self.session)

        main.main()

    def tearDown(self) -> None:
        del os.environ['BUPT_SSO_USER']
        del os.environ['BUPT_SSO_PASS']
        del os.environ['TG_BOT_TOKEN']
        del os.environ['TG_CHAT_ID']
        del os.environ['BNR_LOG_PATH']

    def test_all_features(self):
        # 测试：正确提交登录请求
        login_history = self.session.find_history(main.LOGIN_API)
        self.assertEqual(len(login_history), 1)
        login_history = login_history[0]

        self.assertEqual(login_history.data, {
            'username': '2020114514',
            'password': '114514',
        })

        # 测试：访问了报告页
        history = self.session.find_history(main.REPORT_PAGE)
        self.assertEqual(len(history), 1)

        # 测试：报告 API 提交内容正确
        report_history = self.session.find_history(main.REPORT_API)
        self.assertEqual(len(report_history), 1)
        report_history = report_history[0]

        self.assertEqual(report_history.data, {
            'shit': '1', 'fuck': 'bitch', 'shit_hole': 1, 'damn': 'a'
        })

        # 测试：写了日志
        # 如果日志文件中有 REPORT_API_RESP 的内容，那整个程序运行一定成功了。
        with open(self.log_path, 'r', encoding='utf-8') as f:
            text = f.read()

        self.assertIn('FeatureTest', text)


if __name__ == '__main__':
    unittest.main()
