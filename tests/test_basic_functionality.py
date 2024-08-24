import unittest
from pippy import (
    get_stats,
    get_wb,
    get_aux,
    get_countries,
    get_regions,
    get_cpi,
    get_dictionary,
    get_gdp,
)
from pippy.exceptions import PIPAPIError


class TestBasicFunctionality(unittest.TestCase):
    def test_get_stats(self):
        try:
            df = get_stats(country="ALB", year=2019)
            self.assertIsNotNone(df)
            self.assertTrue(len(df) > 0)
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")

    def test_get_wb(self):
        try:
            df = get_wb(year=2019)
            self.assertIsNotNone(df)
            self.assertTrue(len(df) > 0)
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")

    def test_get_aux(self):
        try:
            df = get_aux("countries")
            self.assertIsNotNone(df)
            self.assertTrue(len(df) > 0)
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")

    def test_get_countries(self):
        try:
            df = get_countries()
            self.assertIsNotNone(df)
            self.assertTrue(len(df) > 0)
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")

    def test_get_regions(self):
        try:
            df = get_regions()
            self.assertIsNotNone(df)
            self.assertTrue(len(df) > 0)
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")

    def test_get_cpi(self):
        try:
            df = get_cpi()
            self.assertIsNotNone(df)
            self.assertTrue(len(df) > 0)
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")

    def test_get_dictionary(self):
        try:
            df = get_dictionary()
            self.assertIsNotNone(df)
            self.assertTrue(len(df) > 0)
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")

    def test_get_gdp(self):
        try:
            df = get_gdp()
            self.assertIsNotNone(df)
            self.assertTrue(len(df) > 0)
        except PIPAPIError as e:
            self.skipTest(f"API is currently unavailable: {str(e)}")


if __name__ == "__main__":
    unittest.main()
