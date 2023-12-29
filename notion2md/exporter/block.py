import os
import shutil

from notion2md.config import Config
from notion2md.convertor.block import BlockConvertor
from notion2md.notion_api import NotionClient
from notion2md.util import zip_dir


class Exporter:
    def __init__(
        self,
        block_id: str = None,
        block_url: str = None,
        output_filename: str = None,
        output_path: str = None,
        download: bool = False,
        unzipped: bool = False,
        token: str = None,
    ):
        self._config = Config(
            block_id=block_id,
            block_url=block_url,
            output_filename=output_filename,
            output_path=output_path,
            download=download,
            unzipped=unzipped,
        )
        self._client = NotionClient(token)
        self._io = None
        self._block_convertor = None

    @property
    def block_convertor(self):
        if not self._block_convertor:
            self._block_convertor = BlockConvertor(
                self._config, self._client, self._io
            )
        return self._block_convertor

    @property
    def config(self):
        return self._config

    @property
    def io(self):
        return self._io

    @io.setter
    def io(self, io):
        self._io = io

    def create_directories(self):
        if not os.path.exists(self._config.tmp_path):
            os.makedirs(self._config.tmp_path)
        if not os.path.exists(self._config.output_path):
            os.mkdir(self._config.output_path)

    def get_blocks(self):
        return self._client.get_children(self._config.target_id)

    def make_zip(self):
        zip_dir(
            os.path.join(self._config.output_path, self._config.file_name)
            + ".zip",
            self._config.tmp_path,
        )
        shutil.rmtree(self._config.tmp_path)

    def export(self):
        pass


class MarkdownExporter(Exporter):
    def export(self):
        self.create_directories()
        with open(
            os.path.join(
                self._config.tmp_path, self._config.file_name + ".md"
            ),
            "w",
            encoding="utf-8",
        ) as output:
            output.write(self.block_convertor.convert(self.get_blocks()))
        if not self._config.unzipped:
            self.make_zip()


class StringExporter(Exporter):
    def export(self):
        return self.block_convertor.to_string(self.get_blocks())


class CLIExporter(Exporter):
    def export(self, blocks):
        with open(
            os.path.join(
                self._config.tmp_path, self._config.file_name + ".md"
            ),
            "w",
            encoding="utf-8",
        ) as output:
            output.write(self.block_convertor.convert(blocks))
