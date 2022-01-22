import urllib.request as request
from urllib.parse import urlparse
import os
import sys
from notion2md import console
from notion2md.config_store import get_config

# Since external file block cannot guarantees
# whether the file is downloadable or not,
# there is no external file downloader
def downloader(url:str) -> str:
    filename = os.path.basename(urlparse(url).path)
    cfg = get_config()
    if filename:
        fullpath = os.path.join(cfg.output_path,filename)
        try:
            console.print_status("Downloading",filename)
            request.urlretrieve(url,fullpath)
            console.print_status("Downloaded",f"successfully downloaded {filename}")
            return filename
        except:
            console.print_error("Cannot download a file or an image")
            sys.exit(1)
    else:
        console.print_error("Cannot find a file or an image name")
        sys.exit(1)
