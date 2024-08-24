import unittest
from pippy.utils import check_api_status


class TestAPIAvailability(unittest.TestCase):
    def test_api_availability(self):
        status = check_api_status()
        for endpoint, status_msg in status.items():
            with self.subTest(endpoint=endpoint):
                self.assertEqual(
                    status_msg,
                    "OK",
                    f"API endpoint {endpoint} is not available",
                )


if __name__ == "__main__":
    unittest.main()
