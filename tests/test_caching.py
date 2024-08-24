import unittest
import time
from pippy import get_stats
from pippy.exceptions import PIPAPIError


class TestCaching(unittest.TestCase):
    def test_caching(self):
        try:
            # First call, should take some time
            start = time.time()
            df1 = get_stats(country="ALB", year=2019)
            time1 = time.time() - start

            # Second call, should be faster due to caching
            start = time.time()
            df2 = get_stats(country="ALB", year=2019)
            time2 = time.time() - start

            self.assertLess(time2, time1)  # Second call should be faster
            self.assertTrue(df1.equals(df2))  # Results should be the same
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")


if __name__ == "__main__":
    unittest.main()
