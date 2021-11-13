from notion2md.client_handler import notion_client_object
from notion2md.evaluator.block import blocks_evaluator
import os

def block_exporter(target_id:str,output_path="notion2md-output"):
    parent_block = notion_client_object.blocks.retrieve(target_id)
    block_title = parent_block['child_page']['title']
    blocks = notion_client_object.blocks.children.list(target_id)
    with open(os.path.join(output_path,block_title+'.md'),'w') as output:
        output.write(blocks_evaluator(blocks['results']))
    print("Export Completed")

# page_exporter()

# database_exporter()