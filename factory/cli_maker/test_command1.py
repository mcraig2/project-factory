import unittest

sys.path.insert(0, os.path.abspath('..'))
from {NAME}.command1 import run_no_arg

class TestCommand1(unittest.TestCase):
    def test_no_arg(self):
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    unittest.main()
