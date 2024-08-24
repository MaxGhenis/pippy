import unittest
from pippy import get_stats, PIPAPIError


class TestErrorHandling(unittest.TestCase):
    def test_invalid_country(self):
        with self.assertRaises(PIPAPIError):
            get_stats(country="INVALID")

    def test_invalid_year(self):
        with self.assertRaises(PIPAPIError):
            get_stats(country="ALB", year=9999)

    def test_invalid_povline(self):
        with self.assertRaises(PIPAPIError):
            get_stats(country="ALB", povline=-1)

    # Add more error handling tests as needed


if __name__ == "__main__":
    unittest.main()
