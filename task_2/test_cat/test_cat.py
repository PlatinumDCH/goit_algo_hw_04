import unittest
import os
from data import *
from pathlib import Path
import sys



current_path = Path(__file__).resolve()
parent_path = current_path.parent.parent
sys.path.append(str(parent_path))
from main import get_cats_info

class TestReadCatsData(unittest.TestCase):

    def setUp(self):
       
        self.temp_file_path = "temp_data.txt"

    def tearDown(self):
        
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

    def write_temp_file(self, data):
        with open(self.temp_file_path, "w", encoding="utf-8") as temp_file:
            temp_file.write(data)

    
    def test_valid_data(self):
        self.write_temp_file(valid_data)
        result = get_cats_info(self.temp_file_path)
        expected = [
            {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": '3'},
            {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": '1'},
        ]
        self.assertEqual(result, expected)

    
    def test_empty_file(self):
        self.write_temp_file(empty_file)
        result = get_cats_info(self.temp_file_path)
        self.assertEqual(result, "Empty file: no data to process")

    
    def test_invalid_data_format(self):
        self.write_temp_file(invalid_data_format)
        result = get_cats_info(self.temp_file_path)
        self.assertEqual(
            result, "Invalid data format"
        )

    
    def test_invalid_age_value(self):
        self.write_temp_file(invalid_age_value)
        result = get_cats_info(self.temp_file_path)
        self.assertEqual(
            result, "Invalid data format",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
