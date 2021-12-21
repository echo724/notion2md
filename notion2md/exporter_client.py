from notion_client.helpers import get_id
import notion2md
from notion2md.exporter import *
import os
import sys
import argparse

def cli():
    parser = argparse.ArgumentParser(description="Notion2md: Notion to Markdown Exporter")
    parser.add_argument('--type','-t',type=str,help="Set a type of target page: block, page, database",default="block")
    parser.add_argument('--url','-u',type=str,help="Set an url of target page")
    parser.add_argument('--id','-i',type=str,help="Set an id of target page")
    parser.add_argument('--path','-p',type=str,help="Set a relative path of output file")
    parser.add_argument('--name','-n',type=str,help="Set a custom name of output file")
    parser.add_argument('--version','-v', action='store_true',help="Show a version of Notion2Md")

    args = parser.parse_args()

    if args.version:
        print(notion2md.__version__)
        sys.exit()

    def get_url():
        return input("Enter Notion Url: ")

    custom_name = args.name if args.name else ""

    target_id = get_id(args.url) if args.url \
        else ( args.id if args.id \
        else get_id(get_url()))

    output_path = os.path.abspath(args.path) if args.path \
        else os.path.join(os.getcwd(),'notion2md-output')

    target_type_map ={
        'block': block_exporter,
        # 'page': page_exporter,
        # 'database': database
    }

    target_type_map[args.type](target_id,output_path,custom_name)

    # page_exporter()

    # database_exporter()