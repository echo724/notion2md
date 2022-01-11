#Link
def text_link(item:dict):
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

#Mentions
def _mention_link(content,url):
    return f"([{content}]({url}])"

def user(information:dict):
    return f"({information['content']})"

def page(information:dict):
    return _mention_link(information['content'], information['url'])

def date(information:dict):
    return f"({information['content']})"

def database(information:dict):
    return _mention_link(information['content'], information['url'])

def mention_information(payload:dict):
    information = dict()
    if payload['href']:
        information['url'] = payload['href']
        if payload['plain_text'] != "Untitled":
            information['content'] = payload['plain_text']
        else:
            information['content'] = payload['href']
    else:
        information['content'] = payload['plain_text']
    
    return information

mention_map = {
    "user": user,
    "page": page,
    "database": database,
    "date": date
}

def richtext_word_converter(richtext:dict) -> str:
    outcome_word = ""
    plain_text = richtext["plain_text"]
    if richtext['type'] == "equation":
        outcome_word = equation(plain_text)
    elif richtext['type'] == "mention":
        mention_type = richtext['mention']['type']
        if mention_type in mention_map:
            outcome_word = mention_map[mention_type](mention_information(richtext))
    else:
        if richtext["href"]:
            outcome_word = text_link(richtext["text"])
        else:
            outcome_word = plain_text
        annot = richtext["annotations"]
        for key,transfer in annotation_map.items():
            if richtext["annotations"][key]:
                outcome_word = transfer(outcome_word)
        if annot["color"] != "default":
            outcome_word = color(outcome_word,annot["color"])
    return outcome_word


def richtext_convertor(richtext_list:list) -> str:
    outcome_sentence = ""
    for richtext in richtext_list:
        outcome_sentence += richtext_word_converter(richtext)
    return outcome_sentence