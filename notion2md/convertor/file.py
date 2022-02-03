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
    filename = os.path.basename(urlparse(url).path)
    cfg = get_config()
    
    if filename:
        name,ext = os.path.splitext(filename)

        outfilename = str(uuid.uuid4())[:8]+ext 
        fullpath = os.path.join(cfg.output_path,outfilename)
            
        try:
            console.print_status("Downloading",f"{filename}")
            request.urlretrieve(url,fullpath)
            console.print_status("Downloaded",f'successfully downloaded "{filename}" -> "{outfilename}"')
            return outfilename,name
        except:
            console.print_error(f"cannot download {filename}")
    else:
        console.print_error(f"unvalid {url}")
