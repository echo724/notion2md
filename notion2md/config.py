import os

from notion_client.helpers import get_id

from notion2md.console.formatter import *
from notion2md.exceptions import UnInitializedConfigException

def singleton(cls):
    instance = {}
    def get_instance(**kargs):
        if cls not in instance:
            if kargs:
                instance[cls] = cls(**kargs)
            else:
                raise UnInitializedConfigException
        return instance[cls]
    return get_instance

@singleton
class Config(object):
    __slots__ = ("file_name", "target_id", "output_path","tmp_path","download","unzipped","path_name")
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
            self.path_name = kargs['path']
            self.output_path = os.path.abspath(kargs['path'])
            
        else:
            self.path_name = 'notion2md-output'
            self.output_path = os.path.join(os.getcwd(),'notion2md-output')

        if "download" in kargs and kargs['download']:
            self.download = True
        else:
            self.download = False

        if "unzipped" in kargs and kargs["unzipped"]:
            self.unzipped = True
            self.tmp_path = self.output_path
        else:
            self.unzipped = False
            self.tmp_path = os.path.join(os.getcwd(),'tmp')