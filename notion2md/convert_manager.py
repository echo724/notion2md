import notion
import os
from notion import block
from notion2md.converter import PageBlockConverter
import json


# convert page block to markdown string
def convert_cli(block, blog_mode):
    # 1. initialize converter
    converter = PageBlockConverter(block, blog_mode=blog_mode)

    # 2. export the markdown text from notion page block
    return convert(converter)


def convert( converter ):
    """Recursively export page block with its sub pages

        Args:
            exporter(PageBlockExporter()): export page block
    """
    converter.page2md()
    return converter.getMd()


if __name__ == "__main__":
    convert_cli()