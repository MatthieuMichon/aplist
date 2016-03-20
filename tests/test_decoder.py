"""Airport List Query package.

Decoder Tester module: checks the behavior of the Decoder class.
"""

import unittest

from aplist.decoder import Decoder


# Following class could gain using the unittest.mock framework
class ProcessorTestStub(object):
    """Stub Process class for test purposes."""

    def __init__(self):
        """Constructor."""
        self._test_clear_called_markers()
        self.dataset = []
        self.filter_queries = []
        self.sort_queries = []
        self.paginate_queries = []

    def reload(self):
        """Reload all database records."""
        self.called_reload = True

    def filter_eq(self, field, value):
        """Filter records where the contents of the given field matches."""
        self.called_filter_eq = True
        self.filter_queries.append({'field': field, 'value': value})

    def sort(self, field, direction):
        """Sort filtered records."""
        self.called_sort = True

    def paginate(self, offset, limit):
        """Extract a part of the records."""
        self.called_paginate = True
        self.paginate_query = {'offset': offset, 'limit': limit}

    def get_selection(self):
        """Return paginated records."""
        self.called_get_selection = True
        return self.dataset

    def _test_clear_called_markers(self):
        """Clear all function called markers."""
        self.called_reload = False
        self.called_filter_eq = False
        self.called_sort = False
        self.called_paginate = False
        self.called_get_selection = False

    def _test_load_data(self, dataset):
        """Load default dataset."""
        self.dataset = dataset


class DecoderTester(unittest.TestCase):
    """decoder module test class."""

    def setUp(self):
        """Test fixture setup."""
        self.dataset = [
            {'dst': 'E', 'name': 'Charles De Gaulle', 'uid': 1382,
             'icao': 'LFPG', 'latitude': 49.012779, 'city': 'Paris',
             'altitude': 392, 'iata': 'CDG', 'longitude': 2.55, 'tzoffset': 1,
             'tzname': 'Europe/Paris', 'country': 'France'},
            {'dst': 'U', 'name': 'Tokyo Intl', 'uid': 2359, 'icao': 'RJTT',
             'latitude': 35.552258, 'city': 'Tokyo', 'altitude': 35,
             'iata': 'HND', 'longitude': 139.779694, 'tzoffset': 9,
             'tzname': 'Asia/Tokyo', 'country': 'Japan'}
        ]
        proc = ProcessorTestStub()
        self.dec = Decoder()
        self.dec.assign_processor(proc)

    def test_proc_assign(self):
        """Check that processor is correctly assigned."""
        self.assertIsInstance(self.dec.processor, ProcessorTestStub)

    def test_processor_calls(self):
        """Check that processor calls are performed during query."""
        query = {}
        query['search'] = {'icao': 'RJTT'}
        query['sort'] = {'country': 'asc'}
        query['page'] = {'offset': 50, 'limit': 50}
        self.dec.query(query=query)
        self.assertTrue(self.dec.processor.called_reload)
        self.assertTrue(self.dec.processor.called_filter_eq)
        self.assertTrue(self.dec.processor.called_sort)
        self.assertTrue(self.dec.processor.called_paginate)
        self.assertTrue(self.dec.processor.called_get_selection)

    def test_query_return(self):
        """Check that processor query returns correctly data."""
        self.dec.processor._test_load_data(dataset=self.dataset)
        self.assertEqual(self.dec.query(query={}), self.dataset)

    def test_query_search(self):
        """Check that processor query returns correctly data."""
        proc = self.dec.processor
        proc._test_load_data(dataset=self.dataset)
        search_query = {'search': {'icao': 'LFPG'}, 'sort': {}, 'page': {}}
        self.dec.query(query=search_query)
        self.assertEqual(proc.filter_queries[0]['field'], 'icao')
        self.assertEqual(proc.filter_queries[0]['value'], 'LFPG')

if __name__ == '__main__':
    unittest.main()
