from notion2md.convertor.block import BlockConvertor
from notion2md.config import Config
from notion2md.notion_api import get_children
from notion2md.util import zip_dir

import os
import shutil


def block_markdown_exporter(**kargs):
    config = Config(**kargs)
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
            os.path.join(config.output_path, config.file_name) + ".zip", config.tmp_path
        )
        shutil.rmtree(config.tmp_path)


def block_string_exporter(**kargs):
    config = Config(**kargs)
    if config.download and not os.path.exists(config.output_path):
        os.mkdir(config.output_path)
    if not config.unzipped and not os.path.exists(config.tmp_path):
        os.makedirs(config.tmp_path)
    blocks = get_children(config.target_id)
    md = BlockConvertor().to_string(blocks)
    # Make Zip file and Delete tmp
    if not config.unzipped:
        zip_dir(
            os.path.join(config.output_path, config.file_name) + ".zip", config.tmp_path
        )
        shutil.rmtree(config.tmp_path)
    return md
