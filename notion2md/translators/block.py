def paragraph(text:str):
    return text

def heading_1(text:str):
    return f"# {text}"

def heading_2(text:str):
    return f"## {text}"

def heading_3(text:str):
    return f"### {text}"

#toggle item will be changed as bulleted list item
def bulleted_list_item(text:str):
    return f"- {text}"

def numbered_list_item(**item:dict):
    """
    input: item:dict = {"number":int, "content":str}
    """
    return f"{item['number']}. {item['content']}"

def to_do(**item:dict):
    """
    input: item:dict = {"checked":bool, "test":str}
    """
    return f"- {'[x]' if item['checked'] else '[ ]'} {item['content']}"

#child_database will be changed as child page
def child_page(**item:dict):
    """
    input: item:dict = {"id":str,"content":str}
    """
    #make_page(item['id'])
    content = item['content']
    return f'[{content}]({content})'

def code_block(**item:dict):
    """
    input: item:dict = {"language":str,"content":str}
    """
    return f"""
    ```{item['language']}
    {item['content']}
    ```
    """

def embed(**item:dict):
    """
    input: item:dict ={"url":str,"content":str}
    """
    return f"[{item['content']}]({item['url']})"

def image(**item:dict):
    """
    input: item:dict ={"url":str,"content":str,"caption":str}
    """
    #if internal: make_image(url)
    return f"""
    ![{item['content']}]({item['url']})
    {item['caption']}
    """

def bookmark(**item:dict):
    """
    input: item:dict ={"url":str,"content":str,"caption":str}
    """
    #if internal: make_image(url)
    return f"""
    ![{item['content']}]({item['url']})
    {item['caption']}
    """

def equation(text:str):
    return f"$$ {text} $$"

def divider(**item:dict):
    return f"---"

def none(**item:dict):
    return ""
