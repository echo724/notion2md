from notion2md.notion_api import get_children
from notion2md.convertor.block import blocks_convertor
import os,sys
import time
from notion2md.console import print_status,print_error
from notion2md.config_store import set_config,get_config

def block_markdown_exporter(**kargs):
    set_config(**kargs)
    config = get_config()

    if not config:
        print_error("cannot make a config from input")
        sys.exit(1)
    else:
        start_time = time.time()
        #Directory Checking and Creating
        if not os.path.exists(config.output_path):
            os.mkdir(config.output_path)
        #Get actual blocks
        print()
        print_status("Retrieving",f"blocks from '{config.target_id}'")
        blocks = get_children(config.target_id)
        #Write(Export) Markdown file
        with open(os.path.join(config.output_path,config.file_name + '.md'),'w',encoding="utf-8") as output:
            output.write(blocks_convertor(blocks))
            
        #Result and Time Check
        print_status("Converted", f"{str(len(blocks))} blocks to markdown in {time.time() - start_time:.2f}s")
        print_status("Exported", f'"{config.file_name}.md" in "{os.path.abspath(config.output_path)}/"')
        print()

def block_string_exporter(**kargs):
    set_config(**kargs)
    config = get_config()
    blocks = get_children(config.target_id)
    return blocks_convertor(blocks)