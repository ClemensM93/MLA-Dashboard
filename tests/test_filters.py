import unittest
from src.filters.format_filter import filter_by_format
from src.filters.date_filter import filter_by_date

class TestFilters(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.data = [
            {'format': 'Workshop', 'date': '2023-10-01', 'check_in': 30, 'check_out': 28},
            {'format': 'Webinar', 'date': '2023-10-02', 'check_in': 50, 'check_out': 45},
            {'format': 'Seminar', 'date': '2023-10-03', 'check_in': 20, 'check_out': 18},
            {'format': 'Workshop', 'date': '2023-10-04', 'check_in': 25, 'check_out': 24},
        ]

    def test_filter_by_format(self):
        result = filter_by_format(self.data, 'Workshop')
        expected = [
            {'format': 'Workshop', 'date': '2023-10-01', 'check_in': 30, 'check_out': 28},
            {'format': 'Workshop', 'date': '2023-10-04', 'check_in': 25, 'check_out': 24},
        ]
        self.assertEqual(result, expected)

    def test_filter_by_date(self):
        result = filter_by_date(self.data, '2023-10-02')
        expected = [
            {'format': 'Webinar', 'date': '2023-10-02', 'check_in': 50, 'check_out': 45},
        ]
        self.assertEqual(result, expected)

    def test_filter_by_date_range(self):
        result = filter_by_date(self.data, start_date='2023-10-01', end_date='2023-10-03')
        expected = [
            {'format': 'Workshop', 'date': '2023-10-01', 'check_in': 30, 'check_out': 28},
            {'format': 'Webinar', 'date': '2023-10-02', 'check_in': 50, 'check_out': 45},
            {'format': 'Seminar', 'date': '2023-10-03', 'check_in': 20, 'check_out': 18},
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()