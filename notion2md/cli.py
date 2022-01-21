from notion2md.exporter import *
from notion2md.config_store import config

def call_exporter(config:Config):
    target_type_map ={
        'block': block_exporter,
        # 'page': page_exporter,
        # 'database': database
    }

    target_type_map[config.exporter_type](config)
    
def run():
    call_exporter(config)