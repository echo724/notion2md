from notion2md.convertor.block import BlockConvertor
from notion2md.config import set_config,get_config
from notion2md.notion_api import get_children

import os

def block_markdown_exporter(**kargs):
    set_config(**kargs)
    config = get_config()
    #Directory Checking and Creating
    if not os.path.exists(config.output_path):
        os.mkdir(config.output_path)
    #Get actual blocks
    blocks = get_children(config.target_id)
    #Write(Export) Markdown file
    with open(os.path.join(config.output_path,config.file_name + '.md'),'w',encoding="utf-8") as output:
        output.write(BlockConvertor(config).convert(blocks))
    
def block_string_exporter(**kargs):
    set_config(**kargs)
    config = get_config()
    blocks = get_children(config.target_id)
    return BlockConvertor(config).to_string(blocks)