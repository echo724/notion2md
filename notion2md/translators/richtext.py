#Link
def link(item:dict):
    """
    input: item:dict ={"content":str,"link":str}
    """
    return f"[{item['content']}]({item['link']})"

#Annotations
def bold(content:str):
    return f"**{content}**"

def italic(content:str):
    return f"*{content}*"

def strikethrough(content:str):
    return f"~~{content}~~"

def underline(content:str):
    return f"<u>{content}</u>"

def code(content:str):
    return f"`{content}`"

def color(content:str,color):
    return f"<span style='color:{color}'>{content}</span>"

def equation(content:str):
    return f"$ {content} $"

annotation_map = {
    "bold": bold,
    "italic": italic,
    "strikethrough": strikethrough,
    "underline": underline,
    "code": code,
}

def list_translator(richtext_list:list):
    output = ""
    for richtext in richtext_list:
        output += word_translator(richtext)
    return output

def word_translator(rich:object):
    output = ""
    text = rich["plain_text"]
    if rich['type'] == "equation":
        output = equation(text)
    else:
        annot = rich["annotations"]
        if rich["href"]:
            output = link(rich["text"])
        else:
            output = text
        for key,transfer in annotation_map.items():
            if annot[key]:
                output = transfer(output)
        if annot["color"] != "default":
            output = color(output,annot["color"])
    return output