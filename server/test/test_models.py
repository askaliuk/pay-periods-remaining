import unittest
from models import Frequency


class ModelsTestCase(unittest.TestCase):

    def test_frequency(self):
        self.assertEqual(Frequency.SEMI_MONTHLY, 'SEMI_MONTHLY')

if __name__ == '__main__':
    unittest.main()
