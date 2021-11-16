from notion_client.helpers import get_id
from notion2md.exporter import *
import os
import argparse

parser = argparse.ArgumentParser(description="Notion2md: Notion to Markdown Exporter")
parser.add_argument('--type','-t',type=str,help="a type of target page: block, page, database",default="block")
parser.add_argument('--url','-u',type=str,help="an url of target page")
parser.add_argument('--id','-i',type=str,help="id of target page")
parser.add_argument('--path','-p',type=str,help="relative path of output file")

args = parser.parse_args()

def get_url():
    return input("Enter Notion Url: ")

if args.url:
    target_id = get_id(args.url)
elif args.id:
    target_id = args.id
else:
    target_id = get_id(get_url())

if args.path:
    output_path = os.path.abspath(args.path)
else:
    output_path = os.path.join(os.getcwd(),'notion2md-output')

target_type_map ={
    'block': block_exporter,
    # 'page': page_exporter,
    # 'database': database
}

target_type_map[args.type](target_id,output_path)

# page_exporter()

# database_exporter()