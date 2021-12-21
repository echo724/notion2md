from notion_client.helpers import get_id
import notion2md
from notion2md.exporter import *
import os
import sys
import argparse
from notion2md.console import print_error

class Config(object):
    __slots__ = ("file_name", "target_id", "output_path","exporter_type")
    def __init__(self,args:dict):
        self.file_name = args["name"] if args["name"] else args["id"]

        self.output_path = os.path.abspath(args["path"]) if args["path"] \
        else os.path.join(os.getcwd(),'notion2md-output')

        self.target_id = get_id(args["url"]) if args["url"] else args["id"]

        if not self.target_id:
            print_error("please enter Notion page's id or url")
            print()
            sys.exit(1)
        
        self.exporter_type = args["type"]

def parse_config() -> dict:
    parser = argparse.ArgumentParser(description="Notion2md: Notion to Markdown Exporter")
    parser.add_argument('--type','-t',type=str,help="Set a type of target page: block, page, database",default="block")
    parser.add_argument('--url','-u',type=str,help="Set an url of target page")
    parser.add_argument('--id','-i',type=str,help="Set an id of target page")
    parser.add_argument('--path','-p',type=str,help="Set a relative path of output file")
    parser.add_argument('--name','-n',type=str,help="Set a custom name of output file")
    parser.add_argument('--version','-v', action='store_true',help="Show a version of Notion2Md")

    return vars(parser.parse_args())

def call_exporter(config:Config):
    target_type_map ={
        'block': block_exporter,
        # 'page': page_exporter,
        # 'database': database
    }

    target_type_map[config.exporter_type](config)
    
def cli():

    args = parse_config()

    if args["version"]:
        print(notion2md.__version__)
        sys.exit(None)

    config = Config(args)
    print()
    call_exporter(config)
    print()