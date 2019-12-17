import unittest
from csv_util.csv_cache import CsvUtil
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        self.csv_util = CsvUtil()

    def test_empty_datafile(self):
        # use non-existent city and parameter
        u = self.csv_util.get_data("asdfas", "safsdfa")
        self.assertFalse(u)

    def delete_file(self):
        self.csv_util.delete_cache()
        os.path.exists(self.csv_util.csv_file.name)
