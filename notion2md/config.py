import os

from notion_client.helpers import get_id

from notion2md.exceptions import MissingTargetIDError


class Config(object):
    __slots__ = (
        "file_name",
        "target_id",
        "output_path",
        "tmp_path",
        "download",
        "unzipped",
        "path_name",
    )

    def __init__(
        self,
        block_id: str = None,
        block_url: str = None,
        output_filename: str = None,
        output_path: str = None,
        download: bool = False,
        unzipped: bool = False,
    ):
        if block_url:
            self.target_id = get_id(block_url)
        elif block_id:
            self.target_id = block_id
        else:
            raise MissingTargetIDError

        if output_filename:
            self.file_name = output_filename
        else:
            self.file_name = self.target_id

        if output_path:
            self.path_name = output_path
            self.output_path = os.path.abspath(output_path)

        else:
            self.path_name = "notion2md-output"
            self.output_path = os.path.join(os.getcwd(), "notion2md-output")

        if download:
            self.download = True
        else:
            self.download = False

        if unzipped:
            self.unzipped = True
            self.tmp_path = self.output_path
        else:
            self.unzipped = False
            self.tmp_path = os.path.join(os.getcwd(), "tmp")
