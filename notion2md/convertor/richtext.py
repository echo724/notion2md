#Link
def link(item:dict):
    """
    input: item:dict ={"content":str,"link":str}
    """
    return f"[{item['content']}]({item['link']['url']})"

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

def richtext_convertor(richtext_list:list) -> str:
    outcome_sentence = ""
    for richtext in richtext_list:
        outcome_word = ""
        plain_text = richtext["plain_text"]
        if richtext['type'] == "equation":
            outcome_word = equation(plain_text)
        else:
            annot = richtext["annotations"]
            if richtext["href"]:
                outcome_word = link(richtext["text"])
            else:
                outcome_word = plain_text
            for key,transfer in annotation_map.items():
                if annot[key]:
                    outcome_word = transfer(outcome_word)
            if annot["color"] != "default":
                outcome_word = color(outcome_word,annot["color"])
        outcome_sentence += outcome_word
    return outcome_sentence