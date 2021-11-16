import unittest
import sys
sys.path.append('../notion2md')
sys.path.append('../Test')
from notion2md.exporter import block_exporter
from Test.config import specific_block_id

class ExporterTest(unittest.TestCase):
    def test_runs(self):
        block_exporter(specific_block_id)

if __name__ == "__main__":
    unittest.main()