#Link
def link(text):
    return f"[{text['content']}]({text['link']})"

#Annotations
def bold(str):
    return f"**{str}**"

def italic(str):
    return f"*{str}*"

def strikethrough(str):
    return f"~~{str}~~"

def underline(str):
    return f"<u>{str}</u>"

def code(str):
    return f"`{str}`"

def color(str,color):
    return f"<span style='color:{color}'>{str}</span>"

annotation_map = {
    "bold": bold,
    "italic": italic,
    "strikethrough": strikethrough,
    "underline": underline,
    "code": code,
}

def parse(rich):
    output = ""
    plain = rich["plain_text"]
    annot = rich["annotations"]
    if rich["href"]:
        output = link(rich["text"])
    else:
        output = plain
    for key,transfer in annotation_map.items():
        if annot[key]:
            output = transfer(output)
    if annot["color"] != "default":
        output = color(output,annot["color"])
    return output