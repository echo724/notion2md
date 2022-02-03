from .richtext import richtext_convertor
from notion2md.notion_api import get_children
import concurrent.futures
from .file import downloader

def paragraph(information:dict) -> str:
    return information['text']

def heading_1(information:dict) -> str:
    return f"# {information['text']}"

def heading_2(information:dict) -> str:
    return f"## {information['text']}"

def heading_3(information:dict) -> str:
    return f"### {information['text']}"

def callout(information:dict) -> str:
    return f"{information['icon']} {information['text']}"

def quote(information:dict) -> str:
    return f"> {information['text']}"

#toggle item will be changed as bulleted list item
def bulleted_list_item(information:dict) -> str:
    return f"- {information['text']}"

# numbering is not supported
def numbered_list_item(information:dict) -> str:
    """
    input: item:dict = {"number":int, "text":str}
    """
    return f"1. {information['text']}"

def to_do(information:dict) -> str:
    """
    input: item:dict = {"checked":bool, "test":str}
    """
    return f"- {'[x]' if information['checked'] else '[ ]'} {information['text']}"

#not yet supported
#child_database will be changed as child page
# def child_page(information:dict) -> str:
#     """
#     input: item:dict = {"id":str,"text":str}
#     """
#     #make_page(information['id'])
#     text = information['text']
#     return f'[{text}]({text})'

def code(information:dict) -> str:
    """
    input: item:dict = {"language":str,"text":str}
    """
    return f"\n```{information['language']}\n{information['text']}\n```"

def embed(information:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str}
    """
    return f"[{information['url']}]({information['url']})"

def image(information:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str,"caption":str}
    """
    name,file_path = downloader(information['url'])

    if information['caption']:
        return f"![{name}]({file_path})\n\n{information['caption']}"
    else:
        return f"![{name}]({file_path})"

def file(information:dict) -> str:
    name,file_path = downloader(information['url'])
    return f"[{name}]({file_path})"

def bookmark(information:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str,"caption":str}
    """
    if information['caption']:
        return f"![{information['url']}]({information['url']})\n\n{information['caption']}"
    else:
        return f"![{information['url']}]({information['url']})"

def equation(information:dict) -> str:
    return f"$$ {information['text']} $$"

def divider(information:dict) -> str:
    return f"---"

def blank() -> str:
    return "<br/>"

def table_row(information:list) -> list:
    """
    input: item:list = [[richtext],....]
    """
    column_list = []
    for column in information['cells']:
        column_list.append(richtext_convertor(column))
    return column_list

# Since Synced Block has only child blocks, not name, it will return blank
def synced_block(information:list) -> str:
    return "[//]: # (Synced Block)"

block_type_map = {
    "paragraph": paragraph,
    "heading_1": heading_1,
    "heading_2": heading_2,
    "heading_3": heading_3,
    "callout": callout,
    "toggle":bulleted_list_item,
    "quote": quote,
    "bulleted_list_item": bulleted_list_item,
    "numbered_list_item": numbered_list_item,
    "to_do": to_do,
    # "child_page": child_page,
    "code": code,
    "embed": embed,
    "image": image,
    "bookmark": bookmark,
    "equation": equation,
    "divider": divider,
    "file": file,
    'table_row': table_row,
    'synced_block':synced_block
}

def blocks_convertor(blocks:object) -> str:
    outcome_blocks:str = ""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(block_convertor,blocks)
        outcome_blocks = "".join([result for result in results])
    return outcome_blocks

def information_collector(payload:dict) -> dict:
    information = dict()
    if "text" in payload:
        information['text'] = richtext_convertor(payload['text'])
    if "icon" in payload:
        information['icon'] = payload['icon']['emoji']
    if "checked" in payload:
        information['checked'] = payload['checked']
    if "expression" in payload:
        information['text'] = payload['expression']
    if "url" in payload:
        information['url'] = payload['url']
    if "caption" in payload:
        information['caption'] = richtext_convertor(payload['caption'])
    if "external" in payload:
        information['url'] = payload['external']['url']
    if "language" in payload:
        information['language'] = payload['language']
    
    # interal url
    if "file" in payload:
        information['url'] = payload['file']['url']
    
    # table cells
    if "cells" in payload:
        information['cells'] = payload['cells']

    return information

def block_convertor(block:object,depth=0) -> str:
    outcome_block:str = ""
    block_type = block['type']
    #Special Case: Block is blank
    if block_type == "paragraph" and not block['has_children'] and not block[block_type]['text']:
        outcome_block = blank() +"\n\n"
    else:
        if block_type in block_type_map:
            outcome_block = block_type_map[block_type](information_collector(block[block_type])) + "\n\n"
        else:
            outcome_block = f"[{block_type} is not supported]\n\n"
        if block['has_children']:
            if block_type == "child_page":
                #call make_child_function
                pass
            elif block_type == 'table':
                depth += 1
                child_blocks = get_children(block['id'])
                table_list = []
                for cell_block in child_blocks:
                    cell_block_type = cell_block['type']
                    table_list.append(block_type_map[cell_block_type](information_collector(cell_block[cell_block_type])))
                # convert to markdown table
                for index,value in enumerate(table_list):
                    if index == 0:
                        outcome_block = " | " + " | ".join(value) + " | " + "\n"
                        outcome_block += " | " + " | ".join(['----'] * len(value)) + " | " + "\n"
                        continue
                    outcome_block += " | " + " | ".join(value) + " | " + "\n"
                outcome_block += "\n"
            else:
                depth += 1
                child_blocks = get_children(block['id'])
                for block in child_blocks:
                    outcome_block += "\t"*depth + block_convertor(block,depth)
    return outcome_block
