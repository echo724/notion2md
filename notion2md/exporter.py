from notion2md.client_handler import notion_client_object
from notion2md.evaluator.block import blocks_evaluator
import os
import time

def block_exporter(target_id:str,output_path="notion2md-output"):
    start_time = time.time()
    #Directory Checking and Creating
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    #Get title from parent page block
    block_title = notion_client_object.blocks.retrieve(target_id)['child_page']['title']
    #Get actual blocks
    blocks = notion_client_object.blocks.children.list(target_id)['results']
    #Write(Export) Markdown file
    with open(os.path.join(output_path,block_title+'.md'),'w') as output:
        output.write(blocks_evaluator(blocks))
    #Result and Time Check
    print(f"Export Completed in {time.time() - start_time:.2f}s")

# page_exporter()

# database_exporter()