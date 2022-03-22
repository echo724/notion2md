class EnvVariableNotFound(Exception):
    def __init__(self) -> None:
        super().__init__("Envrionment Variable 'NOTION_TOKEN' is not found")


class InvalidIntegrationKey(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid Notion Integration key")
