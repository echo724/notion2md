from notion2md.convertor.block import BlockConvertor
from notion2md.config import Config
from notion2md.notion_api import get_children
from notion2md.exceptions import UnInitializedConfigException

import os

def block_markdown_exporter(**kargs):
    config = Config(**kargs)
    #Directory Checking and Creating
    if not os.path.exists(config.output_path):
        os.mkdir(config.output_path)
    #Get actual blocks
    blocks = get_children(config.target_id)
    #Write(Export) Markdown file
    with open(os.path.join(config.output_path,config.file_name + '.md'),'w',encoding="utf-8") as output:
        output.write(BlockConvertor().convert(blocks))
    
def block_string_exporter(**kargs):
    config = Config(**kargs)
    blocks = get_children(config.target_id)
    return BlockConvertor().to_string(blocks)