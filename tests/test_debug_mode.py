import unittest
import io
import sys
from pippy import get_stats
from pippy.exceptions import PIPAPIError


class TestDebugMode(unittest.TestCase):
    def test_debug_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            get_stats(country="ALB", year=2019, debug=True)
        except PIPAPIError:
            pass  # We expect an error, but we still want to check the debug output
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Request URL:", output)
        self.assertIn("Request params:", output)
        self.assertIn("Response status code:", output)


if __name__ == "__main__":
    unittest.main()
