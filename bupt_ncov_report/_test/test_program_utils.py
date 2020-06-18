import unittest

from bupt_ncov_report._test.constant import *
from bupt_ncov_report.program_utils import *
from bupt_ncov_report.pure_utils import *


class Test_ProgramUtils_SimpleFunc(unittest.TestCase):
    """测试 ProgramUtils 中的简单函数。"""

    SHORT_HTML = '''
        var def = {"a": 0};
        var app = new Vue({
            data: {
                oldInfo: {"b": "1"},
            }
        })
    '''

    def setUp(self) -> None:
        self.u = ProgramUtils(PureUtils())

    def test_extractPostData_normal(self):
        """测试其能匹配出 post data，并按照北邮逻辑将其混合"""

        post_data = self.u.extract_post_data(REPORT_PAGE_HTML)
        self.assertEqual(POST_DATA_FINAL, post_data)

    def test_extractPostData_tooShort(self):
        """太短时要抛出异常。"""
        with self.assertRaises(Exception) as _asRa:
            self.u.extract_post_data(self.SHORT_HTML)

    def test_extractPostData_noRequiredData(self):
        old_dict, new_dict = self.u.extract_old_new_data(REPORT_PAGE_HTML)
        broken_new_dict = new_dict.copy()

        # Partial mock：只 mock ProgramUtils 的其中一个函数。注：测试用例的 setUp 独立，故只影响当前测试用例。
        self.u.extract_old_new_data = lambda html: (old_dict, broken_new_dict)

        # 这些属性有可能修改。为防频繁修改测试用例，只测不太可能修改的属性
        TEST_PROPS = (
            'id', 'created',
        )

        # 测试：当属性完整时无异常，当属性不完整时抛出异常
        print('test_extractPostData_noRequiredData start')
        self.u.extract_post_data(REPORT_PAGE_HTML)
        for prop in TEST_PROPS:
            del broken_new_dict[prop]
            with self.assertRaises(Exception) as _asRa:
                self.u.extract_post_data(REPORT_PAGE_HTML)
            broken_new_dict[prop] = new_dict[prop]
        self.u.extract_post_data(REPORT_PAGE_HTML)
        print('test_extractPostData_noRequiredData fin')

    def test_extractOldNewData_normal(self):
        """测试 extract_old_new_data 能正确地匹配出 old_dict 与 new_dict。"""
        old_dict, new_dict = self.u.extract_old_new_data(REPORT_PAGE_HTML)
        self.assertEqual(POST_DATA_OLD, old_dict)
        self.assertEqual(POST_DATA_NEW, new_dict)

    def test_extractOldNewData_tooShort(self):
        """太短时要抛出异常。"""
        with self.assertRaises(Exception) as _asRa:
            self.u.extract_old_new_data(self.SHORT_HTML)


class Test_ProgramUtils_StopWhenSick(unittest.TestCase):
    """测试与「生病时停止有关」的函数。"""

    def setUp(self) -> None:
        self.u = ProgramUtils(PureUtils())

    def test_isDataBroken_normal(self):
        """普通情况"""
        self.assertFalse(self.u.is_data_broken(POST_DATA_FINAL))

    def test_verifyData_returnAsIs(self):
        """测试 verify_data 函数在 data 正确时，是否照原样返回传入的 data"""
        # 测试传入的和传出的是「同一个对象」，因此使用 is 而不用 equal
        self.assertIs(POST_DATA_FINAL, self.u.verify_data(POST_DATA_FINAL))

    def test_isDataBroken_1Lack(self):
        """缺一个属性"""
        data = POST_DATA_FINAL.copy()

        for key in POST_DATA_SICK_ITEMS.keys():
            del data[key]
            self.assertTrue(self.u.is_data_broken(data), msg=f'删除 {key}')
            with self.assertRaises(Exception) as _asRa:
                self.u.verify_data(data)

            data[key] = POST_DATA_FINAL[key]
            self.assertFalse(self.u.is_data_broken(data))
            self.u.verify_data(data)

    def test_isDataBroken_2Lack(self):
        """缺两个属性"""
        data = POST_DATA_FINAL.copy()

        for i, key in enumerate(POST_DATA_SICK_ITEMS.keys()):
            if i == 0:
                # 删掉第一个属性，之后不补充
                del data[key]
                continue

            # 从第二个属性开始删掉之后要补充
            del data[key]
            self.assertTrue(self.u.is_data_broken(data))
            with self.assertRaises(Exception) as _asRa:
                self.u.verify_data(data)
            data[key] = POST_DATA_FINAL[key]
            self.assertTrue(self.u.is_data_broken(data))
            with self.assertRaises(Exception) as _asRa:
                self.u.verify_data(data)

    def test_dataSickReport_checkDataSick_normal(self):
        self.assertEqual(
            [],
            self.u.data_sick_report(POST_DATA_FINAL),
        )
        self.u.check_data_sick(POST_DATA_FINAL)

    def test_dataSickReport_checkDataSick_1Anomaly(self):
        """一个属性异常"""
        data = POST_DATA_FINAL.copy()

        for i, key in enumerate(POST_DATA_SICK_ITEMS.keys()):
            data[key] = POST_DATA_SICK_ITEMS[key]
            self.assertEqual(1, len(self.u.data_sick_report(data)))
            with self.assertRaises(Exception) as _asRa:
                self.u.check_data_sick(data)

            data[key] = POST_DATA_FINAL[key]
            self.assertEqual([], self.u.data_sick_report(data))
            self.u.check_data_sick(data)

    def test_dataSickReport_checkDataSick_2Anomaly(self):
        """两个属性异常"""
        data = POST_DATA_FINAL.copy()

        for i, key in enumerate(POST_DATA_SICK_ITEMS.keys()):
            if i == 0:
                data[key] = POST_DATA_SICK_ITEMS[key]
                continue

            data[key] = POST_DATA_SICK_ITEMS[key]
            self.assertEqual(2, len(self.u.data_sick_report(data)))
            with self.assertRaises(Exception) as _asRa:
                self.u.check_data_sick(data)

            data[key] = POST_DATA_FINAL[key]
            self.assertEqual(1, len(self.u.data_sick_report(data)))
            with self.assertRaises(Exception) as _asRa:
                self.u.check_data_sick(data)

    def test_dataSickReport_correct(self):
        """检测改变 sfjcbh 属性时，报告中是否有「是否接触感染人群」"""
        data = POST_DATA_FINAL.copy()
        data['sfjcbh'] = 1

        sick_report = self.u.data_sick_report(data)
        self.assertEqual(1, len(sick_report))

        shjcbh_report = sick_report[0]
        self.assertIn('是否接触感染人群', shjcbh_report)


if __name__ == '__main__':
    unittest.main()
