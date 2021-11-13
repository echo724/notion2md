import unittest
import sys
sys.path.append('../notion2md')

class ExporterTest(unittest.TestCase):
    def test_runs(self):
        from notion2md import exporter

if __name__ == "__main__":
    unittest.main()