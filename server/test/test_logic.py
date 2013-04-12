import unittest
import logic
from datetime import datetime


class LogicTestCase(unittest.TestCase):

    def test_pay_periods_remaining(self):
        self.assertEqual(18, logic.pay_periods_remaining(
            datetime(2013, 4, 9)))
        self.assertEqual(24, logic.pay_periods_remaining(
            datetime(2013, 1, 1)))
        self.assertEqual(1, logic.pay_periods_remaining(
            datetime(2013, 12, 31)))

        self.assertEqual(18, logic.pay_periods_remaining(
            datetime(2014, 4, 11)))
        self.assertEqual(2, logic.pay_periods_remaining(
            datetime(2014, 12, 1)))


if __name__ == '__main__':
    unittest.main()
