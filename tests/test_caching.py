import unittest
import time
from pippy import get_stats
from pippy.exceptions import PIPAPIError
from pippy.cache import cache_response, get_cached_response


class TestCaching(unittest.TestCase):
    def test_caching(self):
        try:
            # Clear the cache for this specific call
            cache_key = "stats_ALB_2019_None_None_all_all_None_None"
            cache_response(cache_key, None)

            # First call, should take some time
            start = time.time()
            df1 = get_stats(country="ALB", year=2019)
            time1 = time.time() - start

            # Ensure some time has passed
            self.assertGreater(
                time1, 0, "First call should take some measurable time"
            )

            # Second call, should be faster due to caching
            start = time.time()
            df2 = get_stats(country="ALB", year=2019)
            time2 = time.time() - start

            # Check if data is the same
            self.assertTrue(
                df1.equals(df2),
                "Cached data should be the same as original data",
            )

            # Check if second call is faster
            self.assertLess(
                time2,
                time1,
                f"Cached call should be faster (First call: {time1:.6f}s, Second call: {time2:.6f}s)",
            )

            # Check if cache is actually being used
            cached_data = get_cached_response(cache_key)
            self.assertIsNotNone(
                cached_data, "Cache should contain data after the calls"
            )

        except PIPAPIError as e:
            self.fail(f"API request failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
