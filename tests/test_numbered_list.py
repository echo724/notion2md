import unittest

from unittest.mock import MagicMock
from unittest.mock import patch

from notion2md.exporter.block import StringExporter  # type: ignore


expected_md = """1. Thing1:

\t1. Thing2:

\t\t1. one

\t\t2. two

<br/>

Stuff

<br/>

1. Schema

\t1. id (integer)

\t2. type (string)

"""


mock_responses = [
    {
        "object": "list",
        "results": [
            {
                "object": "block",
                "id": "94641568-819d-4a12-a313-c64a3d176cf5",
                "parent": {
                    "type": "page_id",
                    "page_id": "811969e6-f4f5-4e27-a6ac-2b58c2f22e26",
                },
                "created_time": "2023-09-02T22:46:00.000Z",
                "last_edited_time": "2023-09-02T22:48:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": True,
                "archived": False,
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "Thing1:", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "Thing1:",
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            },
            {
                "object": "block",
                "id": "8138f3ff-8fb8-4fb6-8692-e69f7b2a64a5",
                "parent": {
                    "type": "page_id",
                    "page_id": "811969e6-f4f5-4e27-a6ac-2b58c2f22e26",
                },
                "created_time": "2023-09-02T22:48:00.000Z",
                "last_edited_time": "2023-09-02T22:48:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": False,
                "archived": False,
                "type": "paragraph",
                "paragraph": {"rich_text": [], "color": "default"},
            },
            {
                "object": "block",
                "id": "36e6d74c-0069-4089-a0db-3979467a15f6",
                "parent": {
                    "type": "page_id",
                    "page_id": "811969e6-f4f5-4e27-a6ac-2b58c2f22e26",
                },
                "created_time": "2023-09-02T22:48:00.000Z",
                "last_edited_time": "2023-09-02T22:48:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": False,
                "archived": False,
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "Stuff", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "Stuff",
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            },
            {
                "object": "block",
                "id": "994496db-727e-42b0-bf7c-a346ad5070b8",
                "parent": {
                    "type": "page_id",
                    "page_id": "811969e6-f4f5-4e27-a6ac-2b58c2f22e26",
                },
                "created_time": "2023-09-02T22:46:00.000Z",
                "last_edited_time": "2023-09-02T22:48:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": False,
                "archived": False,
                "type": "paragraph",
                "paragraph": {"rich_text": [], "color": "default"},
            },
            {
                "object": "block",
                "id": "e6bb8ac2-7af3-4cbe-af41-e7ac75fe6231",
                "parent": {
                    "type": "page_id",
                    "page_id": "811969e6-f4f5-4e27-a6ac-2b58c2f22e26",
                },
                "created_time": "2023-09-02T22:46:00.000Z",
                "last_edited_time": "2023-09-02T22:48:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": True,
                "archived": False,
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "Schema", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "Schema",
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            },
        ],
        "next_cursor": None,
        "has_more": False,
        "type": "block",
        "block": {},
    },
    {
        "object": "list",
        "results": [
            {
                "object": "block",
                "id": "a86e3565-da49-47ba-9e96-2c22b426f66b",
                "parent": {
                    "type": "block_id",
                    "block_id": "94641568-819d-4a12-a313-c64a3d176cf5",
                },
                "created_time": "2023-09-02T22:46:00.000Z",
                "last_edited_time": "2023-09-02T22:48:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": True,
                "archived": False,
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "Thing2:", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "Thing2:",
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            }
        ],
        "next_cursor": None,
        "has_more": False,
        "type": "block",
        "block": {},
    },
    {
        "object": "list",
        "results": [
            {
                "object": "block",
                "id": "da029b1b-f4ae-40d5-95dd-c0a869f8196d",
                "parent": {
                    "type": "block_id",
                    "block_id": "a86e3565-da49-47ba-9e96-2c22b426f66b",
                },
                "created_time": "2023-09-02T22:46:00.000Z",
                "last_edited_time": "2023-09-02T22:46:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": False,
                "archived": False,
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "one", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "one",
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            },
            {
                "object": "block",
                "id": "1a490359-e05a-4b3e-b39e-0f2eb867b527",
                "parent": {
                    "type": "block_id",
                    "block_id": "a86e3565-da49-47ba-9e96-2c22b426f66b",
                },
                "created_time": "2023-09-02T22:46:00.000Z",
                "last_edited_time": "2023-09-02T22:46:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": False,
                "archived": False,
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "two", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "two",
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            },
        ],
        "next_cursor": None,
        "has_more": False,
        "type": "block",
        "block": {},
    },
    {
        "object": "list",
        "results": [
            {
                "object": "block",
                "id": "612fac7c-d5a9-4946-819d-efd14b444760",
                "parent": {
                    "type": "block_id",
                    "block_id": "e6bb8ac2-7af3-4cbe-af41-e7ac75fe6231",
                },
                "created_time": "2023-09-02T22:46:00.000Z",
                "last_edited_time": "2023-09-02T22:46:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": False,
                "archived": False,
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "id (integer)", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "id (integer)",
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            },
            {
                "object": "block",
                "id": "29a6591f-67cd-4d34-9ab5-2ac917bdbcab",
                "parent": {
                    "type": "block_id",
                    "block_id": "e6bb8ac2-7af3-4cbe-af41-e7ac75fe6231",
                },
                "created_time": "2023-09-02T22:46:00.000Z",
                "last_edited_time": "2023-09-02T22:49:00.000Z",
                "created_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "last_edited_by": {
                    "object": "user",
                    "id": "a7c39264-1886-4b50-ba48-87d1791cf3f4",
                },
                "has_children": False,
                "archived": False,
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "type (string)", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "type (string)",
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            },
        ],
        "next_cursor": None,
        "has_more": False,
        "type": "block",
        "block": {},
    },
]


class NumberedListTest(unittest.TestCase):
    @patch("os.environ")
    def test_get_children(self, mock_env) -> None:
        # Mock environment variable
        mock_env["NOTION_TOKEN"] = "mock_token"

        # Mock the Client class
        with patch("notion2md.notion_api.Client") as MockedClient:
            # Mock the blocks.children.list method to return different values on subsequent calls
            mock_blocks_children_list = MagicMock()
            mock_blocks_children_list.side_effect = mock_responses

            # Attach the mock to the Client instance
            MockedClient.return_value.blocks.children.list = (
                mock_blocks_children_list
            )

            block_id = "1"
            md: str = StringExporter(block_id).export()

            assert md == expected_md


if __name__ == "__main__":
    unittest.main()
