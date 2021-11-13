from notion_client import Client
from notion2md.config import api_key

if api_key:
    notion_client = Client(auth=api_key)