"""Airport List Query package.

Aiport List Tester module: checks the behavior of the main class.
"""

import unittest

from aplist.aplist import AirportList


class AirportListTester(unittest.TestCase):
    """AirportList test class."""

    def setUp(self):
        """Test fixture setup."""
        self.al = AirportList()

    def test_default_qeury(self):
        """Test query with no parameters."""
        results = self.al.query(query={})
        self.assertGreater(len(results), 5000)

    def test_single_search(self):
        """Test query with a single search request."""
        query = {'search': {'country': 'Russia', 'tzoffset': 6}}
        results = self.al.query(query=query)
        # print(results)
        self.assertGreater(len(results), 10)


if __name__ == '__main__':
    unittest.main()
