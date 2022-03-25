class MissingTokenError(Exception):
    """Exception for missing notion token error.

    Notion2Md requires Notion Integration token key to export Notion page to Markdown.
    The token should be saved as envronmental variable. If it is not, this exception
    is raised.
    """

    def __init__(self) -> None:
        super().__init__("Envrionment Variable 'NOTION_TOKEN' is not found")


class MissingTargetIDError(Exception):
    """Exception for missing Notion page's id error.

    Notion2Md requires url or id of Notion's page. This exception is raised if there
    is no target id from user input.
    """

    def __init__(self) -> None:
        super().__init__("Notion Page's id or url is not given as argument")
