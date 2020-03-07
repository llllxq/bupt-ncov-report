import unittest

from bupt_ncov_report.pure_utils import *


class Test_PureUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.u = PureUtils()

    def test_isNumberDataInRange_None(self):
        self.assertFalse(self.u.is_number_data_in_range(None, (-1, 1)))

    def test_isNumberDataInRange_EmptyStr(self):
        self.assertFalse(self.u.is_number_data_in_range('', (-1, 1)))

    def test_isNumberDataInRange_Hex_1(self):
        self.assertFalse(self.u.is_number_data_in_range('0X1A', (0, 32)))

    def test_isNumberDataInRange_Hex_2(self):
        self.assertFalse(self.u.is_number_data_in_range('1A', (0, 32)))

    def test_isNumberDataInRange_Text(self):
        self.assertFalse(self.u.is_number_data_in_range('abc', (0, 32)))

    def test_isNumberDataInRange_UpperBound(self):
        self.assertFalse(self.u.is_number_data_in_range(100, (-82, 100)))

    def test_isNumberDataInRange_NumInStr(self):
        self.assertTrue(self.u.is_number_data_in_range('233', (0, 1000)))

    def test_isNumberDataInRange_LowerBound(self):
        self.assertTrue(self.u.is_number_data_in_range('-82', (-82, 100)))

    def test_matchReGroup1_1Group(self):
        with self.assertRaises(BaseException) as _ctxt:
            self.u.match_re_group1(r'abc(\d+)def', 'abcdef')

        self.assertEqual('1234', self.u.match_re_group1(r'abc(\d+)def', 'abc1234def'))

    def test_matchReGroup1_2Group(self):
        self.assertEqual('1234', self.u.match_re_group1(r'abc(\d+)(def)', 'abc1234def'))

    def test_looksTruthy(self):
        self.assertTrue(PureUtils.looks_truthy('Fuck You'))
        self.assertTrue(PureUtils.looks_truthy('true'))
        self.assertTrue(PureUtils.looks_truthy('1 '))
        self.assertTrue(PureUtils.looks_truthy(1))
        self.assertTrue(PureUtils.looks_truthy([[]]))

        self.assertFalse(PureUtils.looks_truthy('fAlSe'))
        self.assertFalse(PureUtils.looks_truthy(' 0'))
        self.assertFalse(PureUtils.looks_truthy(0))
        self.assertFalse(PureUtils.looks_truthy(dict()))
        self.assertFalse(PureUtils.looks_truthy([0]))
        self.assertFalse(PureUtils.looks_truthy(None))

    def test_looksFalsy(self):
        self.assertFalse(PureUtils.looks_falsy('Fuck You'))
        self.assertFalse(PureUtils.looks_falsy('true'))
        self.assertFalse(PureUtils.looks_falsy('1 '))
        self.assertFalse(PureUtils.looks_falsy(1))
        self.assertFalse(PureUtils.looks_falsy([[]]))

        self.assertTrue(PureUtils.looks_falsy('fAlSe'))
        self.assertTrue(PureUtils.looks_falsy(' 0'))
        self.assertTrue(PureUtils.looks_falsy(0))
        self.assertTrue(PureUtils.looks_falsy(dict()))
        self.assertTrue(PureUtils.looks_falsy([0]))
        self.assertTrue(PureUtils.looks_falsy(None))


if __name__ == '__main__':
    unittest.main()
