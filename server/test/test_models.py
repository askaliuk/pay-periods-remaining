import unittest
from models import Frequency


class ModelsTestCase(unittest.TestCase):

    def test_frequency(self):
        for fr in Frequency:
            self.assertEqual(getattr(Frequency, fr), fr)

if __name__ == '__main__':
    unittest.main()
