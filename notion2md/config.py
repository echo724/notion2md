import os
from notion_client.helpers import get_id
from notion2md.console.formatter import *

class Config(object):
    __slots__ = ("file_name", "target_id", "output_path","download")
    def __init__(self,**kargs):
        if "url" in kargs and kargs['url']:
            self.target_id = get_id(kargs['url'])
        elif "id" in kargs and kargs['id']:
            self.target_id = kargs['id']
        else:
            self.target_id = ""
        
        if "name" in kargs and kargs['name']:
            self.file_name = kargs['name']
        else:
            self.file_name = self.target_id

        if "path" in kargs and kargs['path']:
            self.output_path = os.path.abspath(kargs['path'])
        else:
            self.output_path = os.path.join(os.getcwd(),'notion2md-output')

        if "download" in kargs and kargs['download']:
            self.download = True
        else:
            self.download = False
        
config = None

def set_config(**kargs):
    global config
    config = Config(**kargs)

def get_config():
    global config
    return config