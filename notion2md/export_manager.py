import notion
import os
from notion.client import NotionClient
import requests
from notion2md.exporter import PageBlockExporter


# export the markdown file(string).
def export_cli():
    
    token_v2, url = get_page()
    client = NotionClient(token_v2)
    output_folder = './Notion_Exporter_Output/'

    if not(os.path.isdir(output_folder)):
        os.makedirs(os.path.join(output_folder))
    
    exporter = PageBlockExporter(url,client)
    exporter.create_main_folder(output_folder)
    exporter.create_file()
    export(exporter)

    print("\nExporter successfully exported notion page to markdown")


if __name__ == "__main__":
    export_cli()


def get_page():
    """get notion's page info(url,token_v2)
    """
    token_v2 = input("Token_v2: ")
    url = input("Notion Page Url: ")
    return token_v2,url


def export(exporter):
    exporter.page2md(tapped = 0)
    exporter.write_file()
    for sub_exporter in exporter.sub_exporters:
        export(sub_exporter)