from notion_client import Client
import os

notion_client_object = Client(auth=os.environ["NOTION_TOKEN"])