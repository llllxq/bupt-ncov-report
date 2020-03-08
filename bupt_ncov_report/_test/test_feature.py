import os
import tempfile
import unittest
from typing import Any, Dict

from bupt_ncov_report import *
from bupt_ncov_report._test.constant import *
from bupt_ncov_report._test.mock import *

LOGIN_PAGE_URL = r'https://app.bupt.edu.cn/uc/wap/login'
LOGIN_API_RESP = r'''{"e":0,"m":"操作成功","d":{}}'''
LOGIN_API_FAILED_RESP = r'''{"e":0,"m":"ユーザーまたはパスワードは正しくありません。","d":{}}'''
REPORT_API_RESP = r'''{"e":1,"m":"今天已经填报了","d":{}, "f": "bupt_ncov_report-FeatureTest"}'''

LOGIN_PAGE_HTML = r'''
<!DOCTYPE html>
<html lang="zh-CN">

<head>
  <title>登录</title>
</head>

<body class="">

  <div id="app" v-cloak>
    <div class="content">
      <div><i class="icon iconfont icon-touxiang"></i>
        <input type="text" :placeholder="'请输入'+setting.account_copy" v-model="username" autocomplete="off" />
      </div>
      <div><i class="icon iconfont icon-mima" style=""></i>
        <input type="password" :placeholder="'请输入'+setting.password_copy" v-model="password" autocomplete="off" />
      </div>
    </div>
    <div class="btn" @click='login()'>登 录</div>
    <div class="footer" v-if="setting.login_remarks != undefined && setting.login_remarks != ''">
      <h2><span></span>注意事项<span></span></h2>
      <p v-html="setting.login_remarks"></p>
    </div>
    <div class="foot">
      <p>版权所有&copy;{{setting.copyright}}</p>
    </div>
  </div>
</body>

</html>
'''


def correctly_login_tester(self: unittest.TestCase, session: MockRequestsSession) -> None:
    """测试：断言正确提交登录请求"""

    login_history = session.find_history(LOGIN_API)
    self.assertEqual(1, len(login_history))
    login_history = login_history[0]

    self.assertEqual({
        'username': '2020114514',
        'password': '114514',
    }, login_history.data)


def visited_url_tester(self: unittest.TestCase, session: MockRequestsSession, url: str) -> None:
    """
    测试用例的工具函数：断言访问了指定的 url。
    :param self: 测试类实例
    :param session: MockRequestsSession
    :param url: URL
    :return: None
    """

    history = session.find_history(url)
    self.assertEqual(1, len(history))


def not_visit_url_tester(self: unittest.TestCase, session: MockRequestsSession, url: str) -> None:
    """
    测试用例的工具函数：断言没有访问指定的 url。
    :param self: 测试类实例
    :param session: MockRequestsSession
    :param url: URL
    :return: None
    """

    history = session.find_history(url)
    self.assertEqual([], history)


def correctly_post_report_data_tester(self: unittest.TestCase, session: MockRequestsSession) -> None:
    """测试：断言上报 API 提交内容正确"""

    report_history = session.find_history(REPORT_API)
    self.assertEqual(1, len(report_history))
    report_history = report_history[0]

    self.assertEqual(POST_DATA_FINAL, report_history.data)


def log_written_tester(self: unittest.TestCase, log_path: str, written_text: str) -> None:
    """
    测试：断言写了日志
    :param log_path: 日志文件路径
    :param written_text: 在日志里能找到的内容
    :return: None
    """
    # 如果日志文件中有 REPORT_API_RESP 的内容，那整个程序运行一定成功了。
    with open(log_path, 'r', encoding='utf-8') as f:
        text = f.read()

    self.assertIn(written_text, text)


def generate_config(stop_when_sick: bool) -> Dict[str, Any]:
    """
    生成 config。会返回完美 config，启用所有功能。
    会调用 tempfile 以生成临时日志文件。其中的 BNR_LOG_PATH 是合法的日志地址。

    :param stop_when_sick: STOP_WHEN_SICK 配置。
    :return: 完美配置，用于传入 bupt_ncov_report.Program
    """
    log_fd, log_path = tempfile.mkstemp(suffix='.log')
    os.close(log_fd)

    config = {
        'BUPT_SSO_USER': '2020114514',
        'BUPT_SSO_PASS': '114514',
        'TG_BOT_TOKEN': TG_TOKEN,
        'TG_CHAT_ID': '1145141919810',
        'BNR_LOG_PATH': log_path,
        'STOP_WHEN_SICK': stop_when_sick,
        'SERVER_CHAN_SCKEY': SCKEY,
    }

    return config


def register_respond_to_mock(session: MockRequestsSession, login_success: bool, is_sick: bool) -> None:
    """
    将模拟的 HTML 响应逻辑注册到 session 上。
    :param session: MockRequestsSession
    :param login_success: 登录是否成功；为 False 时将模拟登录失败场景
    :param is_sick: 用户是否生病；为 True 时将模拟带病的上报页面
    :return:
    """
    session.when(action='POST', url=LOGIN_API).respond(
        text=LOGIN_API_RESP if login_success else LOGIN_API_FAILED_RESP
    )

    if login_success:
        session.when(action='GET', url=REPORT_PAGE).respond(
            text=REPORT_PAGE_HTML_OF_SICK_PEOPLE if is_sick else REPORT_PAGE_HTML
        )
    else:
        session.when(action='GET', url=REPORT_PAGE).respond(
            url=LOGIN_PAGE_URL,
            text=LOGIN_PAGE_HTML,
        )

    session.when(action='POST', url=REPORT_API).respond(text=REPORT_API_RESP)

    session.when(
        action='POST', url=f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
    ).respond(text=TG_API_SUCC_RESP)


def setup_testCase(
        self: unittest.TestCase, *,
        stop_when_sick: bool,
        login_success: bool,
        is_sick: bool,
) -> None:
    """
    多个 TestCase 的 setUp 函数有公共代码，因此抽取出来。
    :param self: 测试类实例
    :param stop_when_sick: 是否开启 stop_when_sick 功能
    :param login_success: （模拟的）登录是否成功
    :param is_sick: 是否模拟用户数据带病的场景
    :return: None
    """
    # 初始化 config 对象
    self.config = generate_config(stop_when_sick=stop_when_sick)

    self.sess = MockRequestsSession()
    register_respond_to_mock(self.sess, login_success=login_success, is_sick=is_sick)

    # 此处类型错误忽略
    notifiers = [
        TelegramNotifier(token=TG_TOKEN, chat_id='114514', session=self.sess),
        ServerChanNotifier(sckey=SCKEY, sess=self.sess),
    ]
    pure_util = PureUtils()
    self.prog = Program(
        config=self.config,
        program_utils=ProgramUtils(pure_util),
        session=self.sess,
        notifiers=notifiers,
    )
    self.prog.main()


class TestFeature_Normal(unittest.TestCase):

    def _expected_behavior(self):
        # 正确提交登录请求
        correctly_login_tester(self, self.sess)

        # 访问了报告页
        visited_url_tester(self, self.sess, REPORT_PAGE)

        # 上报 API 提交内容正确
        correctly_post_report_data_tester(self, self.sess)

        # 访问了 Tg API、Server 酱 API
        visited_url_tester(self, self.sess, f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage')
        visited_url_tester(self, self.sess, f'https://sc.ftqq.com/{SCKEY}.send')

        # 日志中有上报 API 的服务器返回
        log_written_tester(self, self.config['BNR_LOG_PATH'], 'bupt_ncov_report-FeatureTest')

        # 状态码为 0
        self.assertEqual(0, self.prog.get_exit_status())

    def test_everythingAsUsual(self):
        setup_testCase(self, login_success=True, stop_when_sick=True, is_sick=False)
        self._expected_behavior()

    def tearDown(self) -> None:
        print('--- 当前测试完成 ---')


class TestFeature_SickButDoNotStop(unittest.TestCase):

    def _expected_behavior(self):
        # 正确提交登录请求
        correctly_login_tester(self, self.sess)

        # 访问了报告页
        visited_url_tester(self, self.sess, REPORT_PAGE)

        # 访问了上报 API（不检查上报内容）、Tg API、Server 酱 API
        visited_url_tester(self, self.sess, REPORT_API)
        visited_url_tester(self, self.sess, f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage')
        visited_url_tester(self, self.sess, f'https://sc.ftqq.com/{SCKEY}.send')

        # 日志中有上报 API 的服务器返回
        log_written_tester(self, self.config['BNR_LOG_PATH'], 'bupt_ncov_report-FeatureTest')

        # 状态码为 0
        self.assertEqual(0, self.prog.get_exit_status())

    def test_sickButDoNotStop(self):
        setup_testCase(self, login_success=True, stop_when_sick=False, is_sick=True)
        self._expected_behavior()

    def tearDown(self) -> None:
        print('--- 当前测试完成 ---')


class TestFeature_FailWhenRunning(unittest.TestCase):

    def _expected_behavior(self):
        # 正确提交登录请求
        correctly_login_tester(self, self.sess)

        # 访问了报告页
        visited_url_tester(self, self.sess, REPORT_PAGE)

        # 未访问上报 API
        not_visit_url_tester(self, self.sess, REPORT_API)

        # 访问了 Tg API、Server 酱 API
        visited_url_tester(self, self.sess, f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage')
        visited_url_tester(self, self.sess, f'https://sc.ftqq.com/{SCKEY}.send')

        # 日志中有 Error
        log_written_tester(self, self.config['BNR_LOG_PATH'], 'Error')

        # 状态码不为 0
        self.assertNotEqual(0, self.prog.get_exit_status())

    def test_sickData_Stop(self):
        setup_testCase(self, login_success=True, stop_when_sick=True, is_sick=True)
        self._expected_behavior()

    def test_loginFailed_Stop(self):
        setup_testCase(self, login_success=False, stop_when_sick=True, is_sick=False)
        self._expected_behavior()

    def tearDown(self) -> None:
        print('--- 当前测试完成 ---')


if __name__ == '__main__':
    unittest.main()
