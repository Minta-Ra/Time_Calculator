import unittest
from io import StringIO
import sys

class TestHello(unittest.TestCase):
    def test_main_prints_hello(self):
        # Import here so tests can be run from project root
        from main import main
        saved_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            main()
            output = sys.stdout.getvalue().strip()
        finally:
            sys.stdout = saved_stdout
        self.assertEqual(output, "Hello, World!")


if __name__ == '__main__':
    unittest.main()
