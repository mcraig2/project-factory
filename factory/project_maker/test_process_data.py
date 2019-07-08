import unittest

import {NAME}.process_data as dio

class TestProcessData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = dio.read_data('data/somedata.csv')

    def test_something(self):
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    unittest.main()
