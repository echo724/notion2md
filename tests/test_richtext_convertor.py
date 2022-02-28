import unittest

from notion2md.convertor.richtext import richtext_word_converter


class ExportRichTextTest(unittest.TestCase):
    def test_mention_date_type(self):
        richtext = {
            "type": "mention",
            "mention": {
                "type": "date",
                "date": {
                    "start": "2022-01-11",
                    "end": None,
                    "time_zone": None,
                },
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "2022-01-11 → ",
            "href": None,
        }
        self.assertEqual(richtext_word_converter(richtext), "(2022-01-11 → )")

    def test_mention_reminder_type(self):
        richtext = {
            "type": "mention",
            "mention": {
                "type": "date",
                "date": {
                    "start": "2022-01-12T09:00:00.000+09:00",
                    "end": None,
                    "time_zone": None,
                },
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "2022-01-12T09:00:00.000+09:00 → ",
            "href": None,
        }
        self.assertEqual(
            richtext_word_converter(richtext),
            "(2022-01-12T09:00:00.000+09:00 → )",
        )

    def test_mention_user_type(self):
        richtext = {
            "type": "mention",
            "mention": {
                "type": "user",
                "user": {
                    "object": "user",
                    "id": "b138e1c9-4054-4713-bd7b-62af6d7641fb",
                    "name": "Eunchan Cho",
                    "avatar_url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/cd39a6ac-1c5a-4b50-9778-3e03885b1e44/sketch1549349815832.png",
                    "type": "person",
                    "person": {"email": "e4cho@ucsd.edu"},
                },
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "@Eunchan Cho",
            "href": None,
        }
        self.assertEqual(richtext_word_converter(richtext), "(@Eunchan Cho)")

    def test_mention_page_type(self):
        richtext = {
            "type": "mention",
            "mention": {
                "type": "page",
                "page": {"id": "ba475a4b-2614-4c51-9e90-5c92a937bd34"},
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "Untitled",
            "href": "https://www.notion.so/ba475a4b26144c519e905c92a937bd34",
        }
        self.assertEqual(
            richtext_word_converter(richtext),
            "([https://www.notion.so/ba475a4b26144c519e905c92a937bd34](https://www.notion.so/ba475a4b26144c519e905c92a937bd34])",
        )

    def test_mention_database_type(self):
        richtext = {
            "type": "mention",
            "mention": {
                "type": "database",
                "database": {"id": "44a4ecdc-7d09-4165-811c-13d9ed8ed7aa"},
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "Posts",
            "href": "https://www.notion.so/44a4ecdc7d094165811c13d9ed8ed7aa",
        }
        self.assertEqual(
            richtext_word_converter(richtext),
            "([Posts](https://www.notion.so/44a4ecdc7d094165811c13d9ed8ed7aa])",
        )

    def test_equation_type1(self):
        richtext = {
            "type": "equation",
            "equation": {"expression": "y = f(x)"},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "y = f(x)",
            "href": None,
        }
        self.assertEqual(richtext_word_converter(richtext), "$ y = f(x) $")

    def test_equation_type2(self):
        richtext = {
            "type": "equation",
            "equation": {"expression": "\\therefore a = 0"},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "\\therefore a = 0",
            "href": None,
        }
        self.assertEqual(
            richtext_word_converter(richtext), "$ \\therefore a = 0 $"
        )

    def test_text_normal_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "text", "link": None},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "text",
            "href": None,
        }
        self.assertEqual(richtext_word_converter(richtext), "text")

    def test_text_bold_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "bold", "link": None},
            "annotations": {
                "bold": True,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "bold",
            "href": None,
        }
        self.assertEqual(richtext_word_converter(richtext), "**bold**")

    def test_text_underline_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "underline", "link": None},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": True,
                "code": False,
                "color": "default",
            },
            "plain_text": "underline",
            "href": None,
        }
        self.assertEqual(richtext_word_converter(richtext), "<u>underline</u>")

    def test_text_italicaize_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "Italicize", "link": None},
            "annotations": {
                "bold": False,
                "italic": True,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "Italicize",
            "href": None,
        }
        self.assertEqual(richtext_word_converter(richtext), "*Italicize*")

    def test_text_strike_through_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "strike-through", "link": None},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": True,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "strike-through",
            "href": None,
        }
        self.assertEqual(
            richtext_word_converter(richtext), "~~strike-through~~"
        )

    def test_text_code_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "code", "link": None},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": True,
                "color": "default",
            },
            "plain_text": "code",
            "href": None,
        }
        self.assertEqual(richtext_word_converter(richtext), "`code`")

    def test_text_multiple_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "multiple", "link": None},
            "annotations": {
                "bold": True,
                "italic": True,
                "strikethrough": True,
                "underline": True,
                "code": True,
                "color": "default",
            },
            "plain_text": "multiple",
            "href": None,
        }
        self.assertEqual(
            richtext_word_converter(richtext), "`<u>~~***multiple***~~</u>`"
        )

    def test_text_color_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "colored", "link": None},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "blue",
            },
            "plain_text": "colored",
            "href": None,
        }
        self.assertEqual(
            richtext_word_converter(richtext),
            "<span style='color:blue'>colored</span>",
        )

    def test_text_link_type(self):
        richtext = {
            "type": "text",
            "text": {
                "content": "link",
                "link": {"url": "/8e3bb46322d54fcf85155f747d205f8d"},
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "link",
            "href": "/8e3bb46322d54fcf85155f747d205f8d",
        }
        self.assertEqual(
            richtext_word_converter(richtext),
            "[link](/8e3bb46322d54fcf85155f747d205f8d)",
        )

    def test_text_url_type(self):
        richtext = {
            "type": "text",
            "text": {"content": "url", "link": {"url": "https://google.com"}},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "url",
            "href": "https://google.com",
        }
        self.assertEqual(
            richtext_word_converter(richtext), "[url](https://google.com)"
        )


if __name__ == "__main__":
    unittest.main()
