from notion_client import Client #,AsyncClient
import os

notion_client_object = Client(auth=os.environ["NOTION_TOKEN"])

# notion_async_client = AsyncClient(auth=os.environ["NOTION_TOKEN"])