from notion2md.exporter import *
from notion2md.config_store import CONFIG
    
def run():
    target_type_map ={
        'block': block_exporter,
        # 'page': page_exporter,
        # 'database': database
    }

    target_type_map[CONFIG.exporter_type](CONFIG)