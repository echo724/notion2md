from notion2md.notion_client import notion_client_object
from notion2md.convertor.block import blocks_convertor
import os
import time
from notion2md.console import print_status

def block_exporter(config):
    start_time = time.time()
    #Directory Checking and Creating
    if not os.path.exists(config.output_path):
        os.mkdir(config.output_path)
    #Get actual blocks

    print_status("Retrieving",f"blocks from '{config.target_id}'")
    blocks = notion_client_object.blocks.children.list(config.target_id)['results']
    #Write(Export) Markdown file
    with open(os.path.join(config.output_path,config.file_name + '.md'),'w',encoding="utf-8") as output:
        output.write(blocks_convertor(blocks))
        
    #Result and Time Check
    print_status("Converted", f"{str(len(blocks))} blocks to markdown in {time.time() - start_time:.2f}s")
    print_status("Exported", f'"{config.file_name}.md" in "{os.path.abspath(config.output_path)}/"')

# page_exporter()

# database_exporter()
