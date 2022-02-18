import os
import urllib.request as request
import uuid

from urllib.parse import urlparse

from cleo.io.io import IO

from notion2md.config import Config
from notion2md.console.formatter import error
from notion2md.console.formatter import status
from notion2md.console.formatter import success
from notion2md.exceptions import UnInitializedConfigException


# Since external file block cannot guarantees
# whether the file is downloadable or not,
# there is no external file downloader
def downloader(url: str, io: IO = None) -> str:
    try:
        cfg = Config()
    except UnInitializedConfigException as e:
        if io:
            io.write_line(error(e))
        else:
            print(e)
    file_name = os.path.basename(urlparse(url).path)
    if cfg.download:
        if file_name:
            name, ext = os.path.splitext(file_name)

            if not ext:
                return file_name, url

            downloaded_file_name = str(uuid.uuid4())[:8] + ext
            fullpath = os.path.join(cfg.tmp_path, downloaded_file_name)

            if io:
                io.write_line(status("Downloading", f"{file_name}"))
                request.urlretrieve(url, fullpath)
                io.write_line(
                    success(
                        "Downloaded",
                        f'successfully downloaded "{file_name}" -> "{downloaded_file_name}"',
                    )
                )
            else:
                request.urlretrieve(url, fullpath)
            return name, downloaded_file_name
        else:
            if io:
                io.write_line(error(f"invalid {url}"))
    else:
        return file_name, url
