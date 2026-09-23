import unittest
from src.data.loader import load_data

class TestLoader(unittest.TestCase):

    def setUp(self):
        self.file_path = 'data/kommunikationskalender.xlsx'

    def test_load_data(self):
        data = load_data(self.file_path)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)  # Assuming the data is returned as a dictionary
        self.assertIn('formats', data)  # Check if 'formats' key exists in the data
        self.assertIn('check_in', data)  # Check if 'check_in' key exists in the data
        self.assertIn('check_out', data)  # Check if 'check_out' key exists in the data

    def test_load_data_empty_file(self):
        empty_file_path = 'data/empty_file.xlsx'
        data = load_data(empty_file_path)
        self.assertEqual(data, {})  # Assuming an empty file returns an empty dictionary

if __name__ == '__main__':
    unittest.main()