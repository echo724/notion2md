import unittest
import sys
sys.path.append('../notion2md')
from notion2md.evaluator.block import blocks_evaluator
from notion2md.client_handler import notion_client
from .config import specific_block_id

class ExportBlocksTest(unittest.TestCase):
    def test_runs(self):
        test_blocks = notion_client.blocks.children.list(
            block_id=specific_block_id
        )
        print(blocks_evaluator(test_blocks['results']))
        with open('output.md','w') as file:
            file.write(blocks_evaluator(test_blocks['results']))

if __name__ == "__main__":
    unittest.main()