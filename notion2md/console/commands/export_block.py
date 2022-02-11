import os,sys
import time

from notion2md.console.formatter import *
from notion2md.config import set_config,get_config
from notion2md.notion_api import get_children
from notion2md.convertor.block import BlockConvertor

from cleo import option
from cleo import Command

class ExportBlockCommand(Command):
    name = "block"
    description = "Export a Notion block object to markdown."

    options = [
        option("url", "u", "The url of Notion block object.", flag=False),
        option("id", "i", "The id of Notion block object.", flag=False),
        option("name", "N", "The name of Notion block object", flag=False),
        option("path", "p", "The path to save exported markdown file.", flag=False),
        option("download", None, "Download files/images inside of the block object", flag=True),
    ]
    help = """The block command retrieves and exports Notion <highlight>block object</highlight> to markdownfile.

By default, the <highlight>id</highlight> of the block will be the name of markdown file, but if you path a value after <code>--name/-n</code>, the value will be the name of the markdown file.
    
It will save the exported markdown file in the path(<highlight>"notion-output/"</highlight> or <highlight>specific path you entered</highlight>)

By default, it won't save files/images in the block object, but if you pass <code>--download</code> option, it will download files/images in the path(<highlight>"notion-output/"</highlight> or <highlight>specific path you entered</highlight>)
    """
    def handle(self):
        set_config(**self.option())
        config = get_config()
        if not config.target_id:
            self.line_error(error("Notion2Md requires either id or url."))
            sys.exit(1)
        start_time = time.time()
        exporter = BlockConvertor(self.io,config)
        #Directory Checking and Creating
        if not os.path.exists(config.output_path):
            os.mkdir(config.output_path)
        #Get actual blocks
        self.line("")
        self.line(status("Retrieving",f"blocks from '{config.target_id}'"))
        blocks = get_children(config.target_id)
        #Write(Export) Markdown file
        with open(os.path.join(config.output_path,config.file_name + '.md'),'w',encoding="utf-8") as output:
            output.write(exporter.convert(blocks))
            
        #Result and Time Check
        self.line(status("Converted", f"{str(len(blocks))} blocks to markdown in {time.time() - start_time:.2f}s"))
        self.line(status("Exported", f'"{config.file_name}.md" in "{os.path.abspath(config.output_path)}/"'))
        self.line("")