import os
import sys

from notion_client import Client  # ,AsyncClient

from notion2md.exceptions import EnvVariableNotFound
from notion2md.exceptions import InvalidIntegrationKey


def singleton(cls):
    instance = {}

    def get_instance():
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]

    return get_instance


@singleton
class NotionClient:
    def __init__(self):
        self._client = None

    def _get_env_variable(self):
        try:
            return os.environ["NOTION_TOKEN"]
        except Exception:
            raise EnvVariableNotFound

    @property
    def client(self):
        try:
            token = self._get_env_variable()
            self._client = Client(auth=token)
        except Exception:
            raise InvalidIntegrationKey
        return self._client

    def get_children(self, parent_id):
        return self.client.blocks.children.list(parent_id)["results"]
