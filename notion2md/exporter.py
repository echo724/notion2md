from notion2md.client_store import notion_client_object
from notion2md.convertor.block import blocks_convertor
import os
import time

os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def fprint(left,right):
    print(f"{style.GREEN}{style.BOLD}{left+' ':>12}{style.RESET}{right}")

def block_exporter(target_id:str,output_path="notion2md-output"):
    start_time = time.time()
    #Directory Checking and Creating
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    #Get title from parent page block
    block_title = notion_client_object.blocks.retrieve(target_id)['child_page']['title']
    #Get actual blocks
    print()
    fprint("Retrieving",f"blocks from '{target_id}'")
    blocks = notion_client_object.blocks.children.list(target_id)['results']
    #Write(Export) Markdown file
    with open(os.path.join(output_path,block_title+'.md'),'w') as output:
        output.write(blocks_convertor(blocks))
    #Result and Time Check
    fprint("Converted", f"{str(len(blocks))} blocks to markdown in {time.time() - start_time:.2f}s")
    fprint("Exported", f'"{block_title}.md" in "{os.path.abspath(output_path)}/"')
    print()

# page_exporter()

# database_exporter()