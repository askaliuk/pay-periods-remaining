import unittest
import logic
from datetime import datetime
from models import Frequency


class LogicTestCase(unittest.TestCase):

    def test_daily(self):
        fr = Frequency.DAILY
        self.assertEqual(365, logic.pay_periods_remaining(
            datetime(2013, 1, 1), fr))
        self.assertEqual(1, logic.pay_periods_remaining(
            datetime(2013, 12, 31), fr))
        self.assertEqual(360, logic.pay_periods_remaining(
            datetime(2008, 1, 7), fr))  # leap year

    def test_weekly(self):
        fr = Frequency.WEEKLY
        # 1/1/13 is Tue. 2013 has 52 friday's to be paid
        self.assertEqual(52, logic.pay_periods_remaining(
            datetime(2013, 1, 1), fr))
        # 12/18/13 is Wed. Each payment done on Friday. So two next Friday's
        # (20 and 27) will be paid before end of year
        self.assertEqual(
            2, logic.pay_periods_remaining(datetime(2013, 12, 18), fr))

    def test_semi_monthly(self):
        fr = Frequency.SEMI_MONTHLY
        self.assertEqual(18, logic.pay_periods_remaining(
            datetime(2013, 4, 9), fr))
        self.assertEqual(24, logic.pay_periods_remaining(
            datetime(2013, 1, 1), fr))
        self.assertEqual(1, logic.pay_periods_remaining(
            datetime(2013, 12, 31), fr))

        self.assertEqual(18, logic.pay_periods_remaining(
            datetime(2014, 4, 11), fr))
        self.assertEqual(2, logic.pay_periods_remaining(
            datetime(2014, 12, 1), fr))
        self.assertEqual(1, logic.pay_periods_remaining(
            datetime(2014, 12, 16), fr))
        self.assertEqual(2, logic.pay_periods_remaining(
            datetime(2014, 12, 15), fr))

    def test_monthly(self):
        fr = Frequency.MONTHLY
        self.assertEqual(1, logic.pay_periods_remaining(
            datetime(2013, 12, 1), fr))
        self.assertEqual(2, logic.pay_periods_remaining(
            datetime(2013, 11, 1), fr))
        self.assertEqual(12, logic.pay_periods_remaining(
            datetime(2013, 1, 1), fr))

    def test_quarterly(self):
        fr = Frequency.QUARTERLY
        self.assertEqual(4, logic.pay_periods_remaining(
            datetime(2013, 1, 1), fr))
        self.assertEqual(4, logic.pay_periods_remaining(
            datetime(2013, 3, 1), fr))
        self.assertEqual(3, logic.pay_periods_remaining(
            datetime(2013, 6, 6), fr))
        self.assertEqual(1, logic.pay_periods_remaining(
            datetime(2013, 12, 1), fr))


if __name__ == '__main__':
    unittest.main()
