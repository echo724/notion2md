from turtle import down
import urllib.request as request
from urllib.parse import urlparse
import os
import re
from notion2md import console

def internal_downloader(url:str) -> str:
    filename = re.search("[.\-\w]+(?=\?)",url).group(0)
    downlaoder(url,filename)
    return filename

# Since external file block cannot guarantees
# whether the file is downloadable or not,
# there is no external file downloader
def external_img_downlaoder(url:str) -> str:
    filename = os.path.basename(urlparse(url).path)
    downlaoder(url,filename)
    return filename

def downlaoder(url,filename):
    if filename:
        try:
            console.print_status("Downloading",filename)
            request.urlretrieve(url,filename)
            console.print_status("Downloaded",f"successfully downloaded {filename}")
        except:
            console.print_error("Cannot download a file or an image")
    else:
        console.print_error("Cannot find a file or an image name")
