from .richtext import richtext_evaluator
from client_handler import notion_client

def paragraph(**kwargs:dict) -> str:
    return kwargs['text']

def heading_1(**kwagrs:dict) -> str:
    return f"# {kwagrs['text']}"

def heading_2(**kwagrs:dict) -> str:
    return f"## {kwagrs['text']}"

def heading_3(**kwagrs:dict) -> str:
    return f"### {kwagrs['text']}"

def callout(**kwagrs:dict) -> str:
    return f"{kwagrs['icon']}"

def quote(**kwagrs:dict) -> str:
    return f"> {kwagrs['text']}"

#toggle item will be changed as bulleted list item
def bulleted_list_item(**kwagrs:dict) -> str:
    return f"- {kwagrs['text']}"

def numbered_list_item(**kwargs:dict) -> str:
    """
    input: item:dict = {"number":int, "text":str}
    """
    return f"{kwargs['number']}. {kwargs['text']}"

def to_do(**kwargs:dict) -> str:
    """
    input: item:dict = {"checked":bool, "test":str}
    """
    return f"- {'[x]' if kwargs['checked'] else '[ ]'} {kwargs['text']}"

#child_database will be changed as child page
def child_page(**kwargs:dict) -> str:
    """
    input: item:dict = {"id":str,"text":str}
    """
    #make_page(kwargs['id'])
    text = kwargs['text']
    return f'[{text}]({text})'

def code_block(**kwargs:dict) -> str:
    """
    input: item:dict = {"lang":str,"text":str}
    """
    return f"""
    ```{kwargs['lang']}
    {kwargs['text']}
    ```
    """

def embed(**kwargs:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str}
    """
    return f"[{kwargs['text']}]({kwargs['url']})"

def image(**kwargs:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str,"caption":str}
    """
    #if internal: make_image(url)
    return f"""
    ![{kwargs['text']}]({kwargs['url']})
    {kwargs['caption']}
    """

def bookmark(**kwargs:dict) -> str:
    """
    input: item:dict ={"url":str,"text":str,"caption":str}
    """
    #if internal: make_image(url)
    return f"""
    ![{kwargs['text']}]({kwargs['url']})
    {kwargs['caption']}
    """

def equation(**kwargs:dict) -> str:
    return f"$$ {kwargs['text']} $$"

def divider(**kwargs:dict) -> str:
    return f"---"

def none(**kwargs:dict) -> str:
    return ""

block_type_map = {
    "heading_1": heading_1,
    "heading_2": heading_2,
    "heading_3": heading_3,
    "callout": callout,
    "quote": quote,
    "bulleted_list_item": bulleted_list_item,
    "numbered_list_item": numbered_list_item,
    "to_do": to_do,
    "child_page": child_page,
    "code_block": code_block,
    "embed": embed,
    "imgae": image,
    "bookmark": bookmark,
    "equation": equation,
    "divider": divider,
    "none": none
}

# def plain_evaluator(block:object) -> str:
#     btype = block['type']
#     text = richtext_evaluator(block[btype]['text'])
#     return plain_map(text)

# def has_children_evaluator(block:object) -> str:
#     btype = block['type']

def blocks_evaluator(block_list:object) -> str:
    outcome_blocks:str = ""
    return outcome_blocks

def block_evaluator(block:object) -> str:
    outcome_block:str = ""
    if block['has_children']:
        child_blocks = notion_client.blocks.children.list(block_id=block['id'])
        for block in child_blocks['results']:
            outcome_block += "&nbsp;&nbsp;&nbsp;&nbsp;" + block_evaluator(block) + "\n\n"
    if block['']
    
    return 1