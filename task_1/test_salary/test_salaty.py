import unittest
from pathlib import Path
from unittest.mock import patch
import sys
from test_data import *

current_path = Path(__file__).resolve()
parent_path = current_path.parent.parent
sys.path.append(str(parent_path))
from main import total_salary


class TestTotalSalary(unittest.TestCase):

    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data=valid_data)
    def test_valid_data(self, mock_file):
        """correct data_file"""
        result = total_salary("dummy_path.txt")
        self.assertEqual(result, (15500, 3100))

    @patch(
        "builtins.open",
        new_callable=unittest.mock.mock_open,
        read_data=invalid_data_value_error,
    )
    def test_invalid_value_error(self, mock_file):
        """invalid work_name and salary value"""
        result = total_salary("dummy_path.txt")
        self.assertEqual(result, "Invalid Data Value error")

    @patch(
        "builtins.open",
        new_callable=unittest.mock.mock_open,
        read_data=invalid_data_missing_salary,
    )
    def test_invalid_missing_salary(self, mock_file):
        """not found salary value"""
        result = total_salary("dummy_path.txt")
        self.assertEqual(result, "Invalid data salary")

    @patch(
        "builtins.open",
        new_callable=unittest.mock.mock_open,
        read_data=invalid_data_no_comma,
    )
    def test_invalid_no_comma(self, mock_file):
        """not found comma"""
        result = total_salary("dummy_path.txt")
        self.assertEqual(result, "Invalid data in file")

    @patch(
        "builtins.open",
        new_callable=unittest.mock.mock_open,
        read_data=invalid_data_missing_name,
    )
    def test_invalid_missing_name(self, mock_file):
        """not found work_name"""
        result = total_salary("dummy_path.txt")
        self.assertEqual(result, "No valid workers to calculate salary")

    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data=empty_file)
    def test_empty_file(self, mock_file):
        """not found data_file"""
        result = total_salary("dummy_path.txt")
        self.assertEqual(result, "Empty file: no workers to process")


if __name__ == "__main__":
    unittest.main(verbosity=2)
