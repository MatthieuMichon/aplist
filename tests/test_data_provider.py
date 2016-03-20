"""Airport List Query package.

Data Provider Tester module: checks the behavior of the Data Provider class.
"""

import os
import requests.exceptions as rqexceptions
import unittest

from aplist.data_provider import DataProvider


class DataProviderTester(unittest.TestCase):
    """airport_db module test class."""

    def setUp(self):
        """Test fixture setup."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        self.cache_dir = os.path.join(test_dir, 'cache')
        if not os.path.isdir(self.cache_dir):
            os.mkdir(self.cache_dir)
        self.cache_filename = os.path.join(self.cache_dir, 'test.dat')

    def tearDown(self):
        """Post-run cleanup."""
        if os.path.isfile(self.cache_filename):
            os.remove(self.cache_filename)
        os.rmdir(self.cache_dir)

    def test_defaults(self):
        """Test with default arguments."""
        dp = DataProvider(filename=self.cache_filename)
        self.assertGreater(len(dp.data), 1000)
        for _ in range(3):
            dp = DataProvider(filename=self.cache_filename)
            self.assertGreater(len(dp.data), 1000)
            self.assertTrue(dp.cache_hit)

    def test_cache_disabled(self):
        """Test with default arguments."""
        for _ in range(3):
            dp = DataProvider(filename=self.cache_filename, use_cache=False)
            self.assertGreater(len(dp.data), 1000)
            self.assertFalse(dp.cache_hit)

    def test_invalid_uri(self):
        """Test with invalid URI."""
        bad_uri = 'https://none.example.com/airports.dat'
        for _ in range(3):
            with self.assertRaises(rqexceptions.RequestException):
                dp = DataProvider(filename=self.cache_filename, uri=bad_uri)
                self.assertGreater(len(dp.data), 1000)
                self.assertFalse(dp.cache_hit)

    def test_bad_data(self):
        """Test with non-CSV data."""
        bad_uri = 'https://www.example.com'
        for _ in range(3):
            with self.assertRaises(SyntaxError):
                dp = DataProvider(filename=self.cache_filename, uri=bad_uri)
                self.assertGreater(len(dp.data), 1000)
                self.assertFalse(dp.cache_hit)


if __name__ == '__main__':
    unittest.main()
