import urllib.request as request
from urllib.parse import urlparse
import os
import uuid

from notion2md.console.formatter import *
from notion2md.config import Config

from clikit.api.io import IO

# Since external file block cannot guarantees
# whether the file is downloadable or not,
# there is no external file downloader
def downloader(url:str,cfg:Config,io:IO) -> str:
    file_name = os.path.basename(urlparse(url).path)
    if cfg.download and io:
        if file_name:
            name,ext = os.path.splitext(file_name)

            downloaded_file_name = str(uuid.uuid4())[:8]+ext 
            fullpath = os.path.join(cfg.output_path,downloaded_file_name)
                
            try:
                io.write_line(status("Downloading",f"{file_name}"))
                request.urlretrieve(url,fullpath)
                io.write_line(status("Downloaded",f'successfully downloaded "{file_name}" -> "{downloaded_file_name}"'))
                return name,downloaded_file_name
            except Exception as e:
                io.write_line(error(f"cannot download {file_name}: {e}"))
        else:
            io.write_line(error(f"unvalid {url}"))
    else:
        return file_name,url
