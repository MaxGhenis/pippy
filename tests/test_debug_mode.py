import unittest
import logging
from io import StringIO
from pippy import get_stats
from pippy.exceptions import PIPAPIError
from pippy.logger import pippy_logger
from pippy.cache import cache_response


class TestDebugMode(unittest.TestCase):
    def test_debug_output(self):
        # Clear the cache for the test case
        cache_key = "stats_ALB_2019_None_None_all_all_None_None"
        cache_response(cache_key, None)

        # Set up a string buffer to capture log output
        log_capture_string = StringIO()
        ch = logging.StreamHandler(log_capture_string)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

        # Add the handler to our custom logger
        pippy_logger.addHandler(ch)

        # Store the original level and set to DEBUG
        original_level = pippy_logger.level
        pippy_logger.setLevel(logging.DEBUG)

        try:
            get_stats(country="ALB", year=2019, debug=True, use_cache=False)
        except PIPAPIError as e:
            print(f"PIPAPIError occurred: {str(e)}")
        finally:
            # Restore the original logging level
            pippy_logger.setLevel(original_level)

        # Get the log output and print it for debugging
        log_contents = log_capture_string.getvalue()
        print("Captured log output:")
        print(log_contents)

        # Check for expected debug output
        self.assertIn("DEBUG - Debug mode enabled", log_contents)
        self.assertIn("DEBUG - Request URL:", log_contents)
        self.assertIn("DEBUG - Request params:", log_contents)

        # Clean up
        pippy_logger.removeHandler(ch)


if __name__ == "__main__":
    unittest.main()
