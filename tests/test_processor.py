"""Airport List Query package.

Processor Tester module: checks the behavior of the Processor class.
"""

import unittest

from aplist.processor import Processor


class ProcessorTester(unittest.TestCase):
    """processor module test class."""

    def setUp(self):
        """Test fixture setup."""
        self.dataset = [
            {'dst': 'E', 'name': 'Charles De Gaulle', 'uid': 1382,
             'icao': 'LFPG', 'latitude': 49.012779, 'city': 'Paris',
             'altitude': 392, 'iata': 'CDG', 'longitude': 2.55, 'tzoffset': 1,
             'tzname': 'Europe/Paris', 'country': 'France'},
            {'dst': 'U', 'name': 'Kansai', 'uid': 3992, 'icao': 'RJBB',
             'latitude': 34.4347222, 'city': 'Osaka', 'altitude': 49,
             'iata': 'KIX', 'longitude': 135.244167, 'tzoffset': 9,
             'tzname': 'Asia/Tokyo', 'country': 'Japan'},
            {'dst': 'U', 'name': 'Tokyo Intl', 'uid': 2359, 'icao': 'RJTT',
             'latitude': 35.552258, 'city': 'Tokyo', 'altitude': 35,
             'iata': 'HND', 'longitude': 139.779694, 'tzoffset': 9,
             'tzname': 'Asia/Tokyo', 'country': 'Japan'},
            {'dst': 'U', 'name': 'Hong Kong Intl', 'uid': 3077, 'icao': 'VHHH',
             'latitude': 22.308919, 'city': 'Hong Kong', 'altitude': 28,
             'iata': 'HKG', 'longitude': 113.914603, 'tzoffset': 8,
             'tzname': 'Asia/Hong_Kong', 'country': 'Hong Kong'}
        ]
        self.proc = Processor()

    def test_init(self):
        """Check that class initialize with an empty dataset."""
        self.assertEqual(self.proc.base_dataset, [])
        self.assertEqual(self.proc.dataset, [])

    def test_load(self):
        """Check load() method."""
        self.proc.load(dataset=self.dataset)
        self.assertEqual(self.proc.get_selection(), self.dataset)

    def test_reload(self):
        """Check reload() method."""
        # Tested explicitly in the following test methods
        pass

    def test_filter_eq(self):
        """Check filter_eq() method."""
        self.proc.load(dataset=self.dataset)
        self.proc.filter_eq(field='icao', value='LFPG')
        self.assertEqual(self.proc.get_selection(), [self.dataset[0]])
        self.proc.reload()
        self.proc.filter_eq(field='icao', value='VHHH')
        self.assertEqual(self.proc.get_selection(), [self.dataset[3]])

    def test_sort(self):
        """Check sort() method with both directions."""
        self.proc.load(dataset=self.dataset)
        self.proc.sort(field='altitude', direction='asc')
        self.assertEqual(self.proc.get_selection()[0], self.dataset[3])
        self.assertEqual(self.proc.get_selection()[3], self.dataset[0])
        self.proc.reload()
        self.proc.sort(field='altitude', direction='des')
        self.assertEqual(self.proc.get_selection()[0], self.dataset[0])
        self.assertEqual(self.proc.get_selection()[3], self.dataset[3])

    def test_paginate(self):
        """Check paginate() method with both directions."""
        self.proc.load(dataset=self.dataset)
        for offset in range(0, len(self.dataset)-1):
            self.proc.reload()
            self.proc.paginate(offset=offset, limit=1)
            self.assertEqual(self.proc.get_selection(), [self.dataset[offset]])
        for limit in range(1, len(self.dataset)):
            self.proc.reload()
            self.proc.paginate(offset=0, limit=limit)
            self.assertEqual(len(self.proc.get_selection()), limit)


if __name__ == '__main__':
    unittest.main()
