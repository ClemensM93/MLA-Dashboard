import unittest
from src.processing.query_processing import process_event_dates
from src.filters.format_filter import filter_by_format
from src.filters.date_filter import filter_by_date

class TestQueryProcessing(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.data = [
            {'date': '2023-10-01', 'format': 'Workshop', 'check_in': 30, 'check_out': 28},
            {'date': '2023-10-02', 'format': 'Webinar', 'check_in': 50, 'check_out': 45},
            {'date': '2023-10-03', 'format': 'Seminar', 'check_in': 20, 'check_out': 18},
            {'date': '2023-10-04', 'format': 'Workshop', 'check_in': 25, 'check_out': 24},
        ]

    def test_process_event_dates(self):
        # Test processing of event dates
        processed_data = process_event_dates(self.data)
        self.assertEqual(len(processed_data), 4)
        self.assertIn('date', processed_data[0])
        self.assertIn('format', processed_data[0])

    def test_filter_by_format(self):
        # Test filtering by format
        filtered_data = filter_by_format(self.data, 'Workshop')
        self.assertEqual(len(filtered_data), 2)
        for entry in filtered_data:
            self.assertEqual(entry['format'], 'Workshop')

    def test_filter_by_date(self):
        # Test filtering by date
        filtered_data = filter_by_date(self.data, '2023-10-01', '2023-10-02')
        self.assertEqual(len(filtered_data), 2)
        self.assertTrue(all(entry['date'] >= '2023-10-01' and entry['date'] <= '2023-10-02' for entry in filtered_data))

if __name__ == '__main__':
    unittest.main()