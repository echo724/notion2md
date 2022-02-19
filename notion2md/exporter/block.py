import os
import shutil

from notion2md.config import Config
from notion2md.convertor.block import BlockConvertor
from notion2md.notion_api import get_children
from notion2md.util import zip_dir


def markdown_exporter(
    block_id: str = None,
    block_url: str = None,
    output_filename: str = None,
    output_path: str = None,
    download: bool = False,
    unzipped: bool = False,
):
    config = Config(
        block_id, block_url, output_filename, output_path, download, unzipped
    )
    # Directory Checking and Creating
    if not os.path.exists(config.tmp_path):
        os.makedirs(config.tmp_path)
    if not os.path.exists(config.output_path):
        os.mkdir(config.output_path)
    # Get actual blocks
    blocks = get_children(config.target_id)
    # Write(Export) Markdown file
    with open(
        os.path.join(config.output_path, config.file_name + ".md"),
        "w",
        encoding="utf-8",
    ) as output:
        output.write(BlockConvertor().convert(blocks))
    # Make Zip file and Delete tmp
    if not config.unzipped:
        zip_dir(
            os.path.join(config.output_path, config.file_name) + ".zip",
            config.tmp_path,
        )
        shutil.rmtree(config.tmp_path)


def string_exporter(
    block_id: str = None,
    block_url: str = None,
    output_filename: str = None,
    output_path: str = None,
    download: bool = False,
    unzipped: bool = False,
):
    config = Config(
        block_id, block_url, output_filename, output_path, download, unzipped
    )
    if config.download and not os.path.exists(config.output_path):
        os.mkdir(config.output_path)
    if not config.unzipped and not os.path.exists(config.tmp_path):
        os.makedirs(config.tmp_path)
    blocks = get_children(config.target_id)
    md = BlockConvertor().to_string(blocks)
    # Make Zip file and Delete tmp
    if not config.unzipped:
        zip_dir(
            os.path.join(config.output_path, config.file_name) + ".zip",
            config.tmp_path,
        )
        shutil.rmtree(config.tmp_path)
    return md
