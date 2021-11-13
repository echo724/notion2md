from .richtext import richtext_evaluator
from notion2md.client_handler import notion_client_object

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
    return f"```{information['language']}\n\t{information['text']}\n```"

def embed(information:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str}
    """
    return f"[{information['url']}]({information['url']})"

def image(information:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str,"caption":str}
    """
    #if internal: make_image(url)
    return f"![{information['url']}]({information['url']})\n\n{information['caption']}"

def bookmark(information:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str,"caption":str}
    """
    #if internal: make_image(url)
    return f"[{information['url']}]({information['url']})\n\n{information['caption']}"

def equation(information:dict) -> str:
    return f"$$ {information['text']} $$"

def divider(information:dict) -> str:
    return f"---"

def none(information:dict) -> str:
    return ""

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
    "imgae": image,
    "bookmark": bookmark,
    "equation": equation,
    "divider": divider,
    "none": none
}

def blocks_evaluator(block_list:object) -> str:
    outcome_blocks:str = ""
    for block in block_list:
        outcome_blocks += block_evaluator(block)
    return outcome_blocks

def information_collector(payload:dict) -> dict:
    information = dict()
    if "text" in payload:
        information['text'] = richtext_evaluator(payload['text'])
    if "icon" in payload:
        information['icon'] = payload['icon']['emoji']
    if "checked" in payload:
        information['checked'] = payload['checked']
    if "expression" in payload:
        information['text'] = payload['expression']
    if "url" in payload:
        information['url'] = payload['url']
    if "caption" in payload:
        information['caption'] = richtext_evaluator(payload['caption'])
    if "external" in payload:
        information['url'] = payload['external']['url']
    if "language" in payload:
        information['language'] = payload['language']
    return information

def block_evaluator(block:object,depth=0) -> str:
    outcome_block:str = ""
    block_type = block['type']
    if block_type in block_type_map:
        outcome_block = block_type_map[block_type](information_collector(block[block_type])) + "\n\n"
    else:
        outcome_block = f"[{block_type} is not supported]\n\n"
    if block['has_children']:
        if block_type == "child_page":
            #call make_child_function
            pass
        else:
            depth += 1
            child_blocks = notion_client_object.blocks.children.list(block_id=block['id'])
            for block in child_blocks['results']:
                outcome_block += "&nbsp;&nbsp;&nbsp;&nbsp;"*depth + block_evaluator(block,depth)
    return outcome_block