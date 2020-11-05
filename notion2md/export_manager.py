import notion
import os
from notion.client import NotionClient
import requests
from notion2md.exporter import PageBlockExporter
import json
# export the markdown file(string).
def export_cli(token_v2="",url="",bmode=-1):
    """
    Exports a folder to a folder.

    Args:
        token_v2: (str): write your description
        url: (str): write your description
        bmode: (str): write your description
    """
    output_folder = './notion2md_output/'
    if not(os.path.isdir(output_folder)):
        os.makedirs(os.path.join(output_folder))
    if token_v2=="":
        client = parse_token()
    else:
        client = NotionClient(token_v2=token_v2)
    if url=="":
        url = input("Enter Notion Page Url: ")
    if bmode==-1:
        inp = input("Will you export the Notion Page as blog post? [y/n]")
        if inp == "y":
            blog_mode = True
        elif inp == "n":
            blog_mode = False
        else:
            print("Invaild Input -> Set None")
    else:
        blog_mode=bool(bmode)
    
    exporter = PageBlockExporter(url,client,blog_mode=blog_mode)
    exporter.create_main_folder(output_folder)
    exporter.create_file()
    export(exporter)

    print("\nExporter successfully exported notion page to markdown")


if __name__ == "__main__":
    export_cli()


def parse_token():
    """Get 'token_v2' from the json file.
        - Save the token in the json if use the Exporter first time.
        - Parse the token in the json if entered the token before.
        < Never Share your token_v2 with others >\n
        Returns:
            client(NotionClient): return notion client object.
    """
    Error = False
    try:
        with open('./notion2md_output/notion_token.json','r') as json_read:
            data = json.load(json_read)
        token = data["token"]
    except:
        token = ""
    while True:
        if token is "" or Error:
            token = input("Enter Token_v2: ")
        try:
            client = NotionClient(token_v2 = token)
            notion_token = {}
            notion_token["token"] = token
            with open("./notion2md_output/notion_token.json",'w') as json_make:
                json.dump(notion_token,json_make,indent=4)
            return client
        except:
            print("[Error] Invaild Token_v2. Enter Token_v2 again")
            Error = True


def export(exporter):
    """Recursively export page block with its sub pages
    
        Args:
            exporter(PageBlockExporter()): export page block
    """
    exporter.page2md()
    exporter.write_file()
    for sub_exporter in exporter.sub_exporters:
        export(sub_exporter)
