import urllib.request as request
from urllib.parse import urlparse
import os
import uuid
from notion2md import console
from notion2md.config_store import get_config

# Since external file block cannot guarantees
# whether the file is downloadable or not,
# there is no external file downloader
def downloader(url:str) -> str:
    file_name = os.path.basename(urlparse(url).path)
    cfg = get_config()

    if cfg.download:
        if file_name:
            name,ext = os.path.splitext(file_name)

            downloaded_file_name = str(uuid.uuid4())[:8]+ext 
            fullpath = os.path.join(cfg.output_path,downloaded_file_name)
                
            try:
                console.print_status("Downloading",f"{file_name}")
                request.urlretrieve(url,fullpath)
                console.print_status("Downloaded",f'successfully downloaded "{file_name}" -> "{downloaded_file_name}"')
                return name,downloaded_file_name
            except:
                console.print_error(f"cannot download {file_name}")
        else:
            console.print_error(f"unvalid {url}")
    else:
        return file_name,url
