import os, sys, argparse
import notion2md
from notion2md.console import print_error,print_status
from notion_client.helpers import get_id

class Config(object):
    __slots__ = ("file_name", "target_id", "output_path","exporter_type")
    def __init__(self,id,name="",path="",url="",type=""):
        self.file_name = name if name else id

        self.output_path = os.path.abspath(path) if path \
        else os.path.join(os.getcwd(),'notion2md-output')

        self.target_id = get_id(url) if url else id

        self.exporter_type = type

def parse_config() -> dict:
    parser = argparse.ArgumentParser(description="Notion2md: Notion Markdown Exporter with Python Cli")
    parser.add_argument('--type','-t',type=str,help="Set a type of target page: block, page, database",default="block")
    parser.add_argument('--url','-u',type=str,help="Set an url of target page")
    parser.add_argument('--id','-i',type=str,help="Set an id of target page")
    parser.add_argument('--path','-p',type=str,help="Set a relative path of output file")
    parser.add_argument('--name','-n',type=str,help="Set a custom name of output file")
    parser.add_argument('--version','-v', action='store_true',help="Show a version of Notion2Md")

    return vars(parser.parse_args())

args = parse_config()

if args["version"]:
    print_status("Version", notion2md.__version__)
    sys.exit(None)
else:
    del args["version"]

if not args["id"] and not args["name"]:
    print_error("please enter a Notion page's id or url")
    sys.exit(1)

CONFIG = Config(**args)