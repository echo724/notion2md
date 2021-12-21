import unittest
import sys
sys.path.append('../notion2md')
sys.path.append('../Test')
from notion2md.exporter import block_exporter
from notion2md.cli import Config
from .config import specific_block_id

class ExporterTest(unittest.TestCase):
    def test_runs(self):
        config = Config(id=specific_block_id)
        block_exporter(config)

if __name__ == "__main__":
    unittest.main()