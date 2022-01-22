import os
from notion_client.helpers import get_id

class Config(object):
    __slots__ = ("file_name", "target_id", "output_path","exporter_type")
    def __init__(self,id,name="",path="",url="",type=""):
        self.file_name = name if name else id

        self.output_path = os.path.abspath(path) if path \
        else os.path.join(os.getcwd(),'notion2md-output')

        self.target_id = get_id(url) if url else id

        self.exporter_type = type

config = None

def set_config(**kargs):
    global config
    config = Config(**kargs)

def get_config():
    global config
    return config