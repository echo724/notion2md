import unittest
import sys
sys.path.append('../notion2md')
sys.path.append('../Test')
from notion2md.exporter import block_makrdown_exporter
from notion2md.config_store import set_config,get_config
from .config import specific_block_id

class ExporterTest(unittest.TestCase):
    def test_runs(self):
        block_makrdown_exporter(id=specific_block_id)

if __name__ == "__main__":
    unittest.main()