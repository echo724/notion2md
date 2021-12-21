from notion_client import Client #,AsyncClient
import os,sys
from notion2md.console import print_error

try:
    notion_client_object = Client(auth=os.environ["NOTION_TOKEN"])
except:
    print_error("Notion Integration Token is not found")
    print(
    """
        Welcome to notion2md!

        To get started, you need to save your Notion Integration Token.
        Find your token at

            https://www.notion.so/my-integrations

        Then run shell command:

            $export NOTION_TOKEN="<Your Token>"
        
        If you want to save this environment variable after reboot,
        put upper command in your shell resource(ex: .bashrc or .zshrc)
    """
    )
    print()
    sys.exit(1)
# notion_async_client = AsyncClient(auth=os.environ["NOTION_TOKEN"])