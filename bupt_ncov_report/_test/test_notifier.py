import unittest

from bupt_ncov_report import *
from bupt_ncov_report._test.constant import *
from bupt_ncov_report._test.mock import *


class NothingNotifier(INotifier):
    pass


class Test_NothingNotifier(unittest.TestCase):

    def test_initialization_fail(self):
        with self.assertRaises(Exception) as _asRa:
            NothingNotifier()


class Test_Notifiers(unittest.TestCase):
    MSG = 'bupt_ncov_report-Test_Notifiers'

    def setUp(self) -> None:
        self._sess = MockRequestsSession()
        self.sc = ServerChanNotifier(sckey=SCKEY, sess=self._sess)
        self.tg = TelegramNotifier(token=TG_TOKEN, chat_id='114514', session=self._sess)

    def test_telegramNotifier_normal(self):
        self._sess.when(
            action='post', url=f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
        ).respond(status_code=200, text=TG_API_SUCC_RESP)
        self.tg.notify(success=True, msg=self.MSG)

        history = self._sess.find_history(f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage')
        self.assertEqual(1, len(history))
        self.assertIsNotNone(history[0].json)
        self.assertIn(self.MSG, history[0].json.get('text', ''))

    def test_telegramNotifier_fail(self):
        for i in (TG_API_BAD_JSON, TG_API_REDIR_HTML):
            self._sess.when(
                action='post', url=f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
            ).respond(status_code=200, text=i)

            with self.assertRaises(Exception) as _asRa:
                self.tg.notify(success=True, msg=self.MSG)

    def test_serverChanNotifier_normal(self):
        self._sess.when(
            action='post', url=f'https://sc.ftqq.com/{SCKEY}.send'
        ).respond(status_code=200, text=SERV_CHAN_SUCC_RESP)
        self.sc.notify(success=True, msg=self.MSG)

        history = self._sess.find_history(f'https://sc.ftqq.com/{SCKEY}.send')
        self.assertEqual(1, len(history))
        self.assertIsNotNone(history[0].data)
        self.assertIn(self.MSG, history[0].data.get('desp', ''))
