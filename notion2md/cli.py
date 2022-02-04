from notion2md.exporter import *
from notion2md.config_store import *
import sys, argparse
import notion2md
from notion2md.console import print_error,print_status

def parse_config() -> dict:
    parser = argparse.ArgumentParser(description="Notion2md: Notion Markdown Exporter with Python Cli")
    parser.add_argument('--type','-t',type=str,help="Set a type of target page: block, page, database",default="block")
    parser.add_argument('--url','-u',type=str,help="Set an url of target page")
    parser.add_argument('--id','-i',type=str,help="Set an id of target page")
    parser.add_argument('--path','-p',type=str,help="Set a relative path of output file")
    parser.add_argument('--name','-n',type=str,help="Set a custom name of output file")
    parser.add_argument('--version','-v', action='store_true',help="Show a version of Notion2Md")
    parser.add_argument('--download',action='store_true',help="will download files/images inside of target page")

    return vars(parser.parse_args())


    
def run():
    args = parse_config()

    if args["version"]:
        print_status("Version", notion2md.__version__)
        sys.exit(None)
    else:
        del args["version"]

    if not args["id"] and not args["name"]:
        print_error("please enter a Notion page's id or url")
        sys.exit(1)
    
    target_type_map ={
        'block': block_markdown_exporter,
        # 'page': page_exporter,
        # 'database': database
    }

    if args['type'] in target_type_map:
        target_type_map[args['type']](**args)
    else:
        print_error("the type of target page is not supported")
        sys.exit(1)