import concurrent.futures
import hashlib
import os
import urllib.request as request
from urllib.parse import urlparse,unquote

from cleo.io.io import IO

from notion2md.config import Config
from notion2md.console.formatter import error
from notion2md.console.formatter import status
from notion2md.console.formatter import success
from notion2md.notion_api import NotionClient
from .richtext import richtext_convertor


class BlockConvertor:
    def __init__(self, config: Config, client: NotionClient, io: IO = None):
        self._config = config
        self._client = client
        self._io = io

    def convert(self, blocks: dict) -> str:
        outcome_blocks: str = ""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(self.convert_block, blocks)
            outcome_blocks = "".join([result for result in results])
        return outcome_blocks

    def convert_block(
            self,
            block: dict,
            depth=0,
    ):
        outcome_block: str = ""
        block_type = block["type"]
        # Special Case: Block is blank
        if check_block_is_blank(block, block_type):
            return blank() + "\n\n"
        # Normal Case
        try:
            if block_type in BLOCK_TYPES:
                outcome_block = (
                        BLOCK_TYPES[block_type](
                            self.collect_info(block[block_type])
                        )
                        + "\n\n"
                )
            else:
                outcome_block = f"[//]: # ({block_type} is not supported)\n\n"
            # Convert child block
            if block["has_children"]:
                # create child page
                if block_type == "child_page":
                    # call make_child_function
                    pass
                # create table block
                elif block_type == "table":
                    depth += 1
                    child_blocks = self._client.get_children(block["id"])
                    outcome_block = self.create_table(cell_blocks=child_blocks)
                # create indent block
                else:
                    depth += 1
                    child_blocks = self._client.get_children(block["id"])
                    for block in child_blocks:
                        converted_block = self.convert_block(
                            block,
                            depth,
                        )
                        outcome_block += "\t" * depth + converted_block
        except Exception as e:
            if self._io:
                self._io.write_line(
                    error(f"{e}: Error occured block_type:{block_type}")
                )
        return outcome_block

    def create_table(self, cell_blocks: dict):
        table_list = []
        for cell_block in cell_blocks:
            cell_block_type = cell_block["type"]
            table_list.append(
                BLOCK_TYPES[cell_block_type](
                    self.collect_info(cell_block[cell_block_type])
                )
            )
        # convert to markdown table
        for index, value in enumerate(table_list):
            if index == 0:
                table = " | " + " | ".join(value) + " | " + "\n"
                table += (
                        " | " + " | ".join(["----"] * len(value)) + " | " + "\n"
                )
                continue
            table += " | " + " | ".join(value) + " | " + "\n"
        table += "\n"
        return table

    def collect_info(self, payload: dict) -> dict:
        info = dict()
        if "rich_text" in payload:
            info["text"] = richtext_convertor(payload["rich_text"])
        if "icon" in payload:
            info["icon"] = payload["icon"]["emoji"]
        if "checked" in payload:
            info["checked"] = payload["checked"]
        if "expression" in payload:
            info["text"] = payload["expression"]
        if "url" in payload:
            info["url"] = payload["url"]
        if "caption" in payload:
            info["caption"] = richtext_convertor(payload["caption"])
        if "external" in payload:
            info["url"] = payload["external"]["url"]
            name, file_path = self.download_file(info["url"])
            info["file_name"] = name
            info["file_path"] = file_path
        if "language" in payload:
            info["language"] = payload["language"]
        # interal url
        if "file" in payload:
            info["url"] = payload["file"]["url"]
            name, file_path = self.download_file(info["url"])
            info["file_name"] = name
            info["file_path"] = file_path
        # table cells
        if "cells" in payload:
            info["cells"] = payload["cells"]
        return info

    def download_file(self, url: str) -> tuple[str, str]:
        file_name = os.path.basename(urlparse(url).path)
        unquoted_file_name = unquote(file_name)
        if self._config.download:
            if unquoted_file_name:
                name, extension = os.path.splitext(unquoted_file_name)

                if not extension:
                    return unquoted_file_name, url

                url_hash = hashlib.blake2s(
                    urlparse(url).path.encode()
                ).hexdigest()[:8]
                downloaded_file_name = f"{url_hash}_{unquoted_file_name}"

                fullpath = os.path.join(
                    self._config.tmp_path, downloaded_file_name
                )

                if self._io:
                    self._io.write_line(status("Downloading", f"{unquoted_file_name}"))
                    request.urlretrieve(url, fullpath)
                    self._io.write_line(
                        success(
                            "Downloaded",
                            f'"{unquoted_file_name}" -> "{downloaded_file_name}"',
                        )
                    )
                else:
                    request.urlretrieve(url, fullpath)
                return name, downloaded_file_name
            else:
                if self._io:
                    self._io.write_line(error(f"invalid {url}"))
        else:
            return unquoted_file_name, url

    def to_string(self, blocks: dict) -> str:
        return self.convert(blocks)


def check_block_is_blank(block, block_type):
    return (
            block_type == "paragraph"
            and not block["has_children"]
            and not block[block_type]["rich_text"]
    )


# Converting Methods
def paragraph(info: dict) -> str:
    return info["text"]


def heading_1(info: dict) -> str:
    return f"# {info['text']}"


def heading_2(info: dict) -> str:
    return f"## {info['text']}"


def heading_3(info: dict) -> str:
    return f"### {info['text']}"


def callout(info: dict) -> str:
    return f"{info['icon']} {info['text']}"


def quote(info: dict) -> str:
    return f"> {info['text']}"


# toggle item will be changed as bulleted list item
def bulleted_list_item(info: dict) -> str:
    return f"- {info['text']}"


# numbering is not supported
def numbered_list_item(info: dict) -> str:
    """
    input: item:dict = {"number":int, "text":str}
    """
    return f"1. {info['text']}"


def to_do(info: dict) -> str:
    """
    input: item:dict = {"checked":bool, "test":str}
    """
    return f"- {'[x]' if info['checked'] else '[ ]'} {info['text']}"


# not yet supported
# child_database will be changed as child page
# def child_page(info:dict) -> str:
#     """
#     input: item:dict = {"id":str,"text":str}
#     """
#     #make_page(info['id'])
#     text = info['text']
#     return f'[{text}]({text})'


def code(info: dict) -> str:
    """
    input: item:dict = {"language":str,"text":str}
    """
    return f"\n```{info['language']}\n{info['text']}\n```"


def embed(info: dict) -> str:
    """
    input: item:dict ={"url":str,"text":str}
    """
    return f"[{info['url']}]({info['url']})"


def image(info: dict) -> str:
    """
    input: item:dict ={"url":str,"text":str,"caption":str}
    """
    # name,file_path = downloader(info['url'])

    if info["caption"]:
        return (
            f"![{info['file_name']}]({info['file_path']})\n\n{info['caption']}"
        )
    else:
        return f"![{info['file_name']}]({info['file_path']})"


def file(info: dict) -> str:
    # name,file_path = downloader(info['url'])
    return f"[{info['file_name']}]({info['file_path']})"


def bookmark(info: dict) -> str:
    """
    input: item:dict ={"url":str,"text":str,"caption":str}
    """
    if info["caption"]:
        return f"[{info['url']}]({info['url']})\n\n{info['caption']}"
    else:
        return f"[{info['url']}]({info['url']})"


def equation(info: dict) -> str:
    return f"$$ {info['text']} $$"


def divider(info: dict) -> str:
    return "---"


def blank() -> str:
    return "<br/>"


def table_row(info: list) -> list:
    """
    input: item:list = [[richtext],....]
    """
    column_list = []
    for column in info["cells"]:
        column_list.append(richtext_convertor(column))
    return column_list


# Since Synced Block has only child blocks, not name, it will return blank
def synced_block(info: list) -> str:
    return "[//]: # (Synced Block)"


# Block type map
BLOCK_TYPES = {
    "paragraph": paragraph,
    "heading_1": heading_1,
    "heading_2": heading_2,
    "heading_3": heading_3,
    "callout": callout,
    "toggle": bulleted_list_item,
    "quote": quote,
    "bulleted_list_item": bulleted_list_item,
    "numbered_list_item": numbered_list_item,
    "to_do": to_do,
    # "child_page": child_page,
    "code": code,
    "embed": embed,
    "image": image,
    "bookmark": bookmark,
    "equation": equation,
    "divider": divider,
    "file": file,
    "table_row": table_row,
    "synced_block": synced_block,
}
