from notion_client import Client #,AsyncClient
import os,sys

try:
    notion_client_object = Client(auth=os.environ["NOTION_TOKEN"])
except:
    print(
    """
        Token Error

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
    sys.exit()
# notion_async_client = AsyncClient(auth=os.environ["NOTION_TOKEN"])