import unittest
import sys
sys.path.append('../notion2md')
sys.path.append('../Test')
from Test.config import specific_block_id

class ExporterTest(unittest.TestCase):
    def test_runs(self):
        from notion2md import exporter
        exporter.block_exporter(specific_block_id)

if __name__ == "__main__":
    unittest.main()