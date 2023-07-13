import unittest
from unittest.mock import patch, mock_open
from src import excel_to_csv_converter

class TestExcelToCsvConverter(unittest.TestCase):

    @patch('os.walk')
    def test_find_excel_files(self, mock_walk):
        mock_walk.return_value = [
            ('/path/to', ('dir1',), ('file1.xlsx', 'file2.xlsb', 'file3.txt')),
            ('/path/to/dir1', (), ('file4.xlsx', 'file5.xlsb', 'file6.txt'))
        ]

        result = excel_to_csv_converter.find_excel_files('/path/to')
        expected_result = [
            '/path/to/file1.xlsx',
            '/path/to/file2.xlsb',
            '/path/to/dir1/file4.xlsx',
            '/path/to/dir1/file5.xlsb',
        ]

        self.assertListEqual(result, expected_result)

    @patch('subprocess.run')
    def test_convert_excel_to_csv(self, mock_subprocess):
        excel_file = '/path/to/file.xlsx'
        csv_file = '/path/to/file.csv'
        excel_to_csv_converter.convert_excel_to_csv(excel_file, csv_file)
        mock_subprocess.assert_called_once()

    # For this test, you'd need to mock a lot more operations such as os.path.relpath, os.path.join, etc.
    # This is just a very basic test to ensure the loop is working and the convert_excel_to_csv function is being called
    @patch('src.excel_to_csv_converter.convert_excel_to_csv')
    def test_convert_excel_files(self, mock_convert):
        excel_files = ['/path/to/file1.xlsx', '/path/to/file2.xlsb']
        excel_to_csv_converter.convert_excel_files(excel_files, '/path/to/destination', '/path/to')
        self.assertEqual(mock_convert.call_count, 2)


if __name__ == '__main__':
    unittest.main()
