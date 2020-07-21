import notion
import os
from notion.client import NotionClient
import requests

#get notion's page info(url,token_v2)
def get_page():
    token_v2 = input("Token_v2: ")
    url = input("Notion Page Url: ")
    return token_v2,url

#set Markdown file name and path
def set_filename():
    directory = './notion_output/'
    if not(os.path.isdir(directory)):
        os.makedirs(os.path.join(directory))
    fname = input("Markdown file name: ") + ".md"
    fname = os.path.join(directory,fname)
    return fname,directory

#get children blocks in notion's page
def recursive_getblocks(block,container,client):
    container.append(client.get_block(block.id))
    try:
        for children_id in block.get("content"):
            children = client.get_block(children_id)
            recursive_getblocks(children,container,client)
    except:
        return

#make markdown link format string
def link(name,url):
    return "["+name+"]"+"("+url+")"

#make image file
def image_export(url,count,dir):
    img_dir = dir + 'img_{0}.png'.format(count)
    r = requests.get(url, allow_redirects=True)
    open(img_dir,'wb').write(r.content)
    return img_dir

#change notion's block to markdown string
def block2md(blocks,dir):
    md = ""
    img_count = 0
    numbered_list_index = 0
    dir += '{0}/'.format(blocks[0].title)
    for block in blocks:
        try:
            btype = block.type
        except:
            continue
        if btype != "numbered_list":
            numbered_list_index = 0
        try:
            bt = block.title
        except:
            pass
        if btype == 'header':
            md += "# " + bt
        elif btype == "sub_header":
            md += "## " +bt
        elif btype == "sub_sub_header":
            md += "### " +bt
        elif btype == 'page':
            try:
                if "https:" in block.icon:
                    icon = "!"+link("",block.icon)
                else:
                    icon = block.icon
                md += "# " + icon + bt
            except:
                md += "# " + bt
        elif btype == 'text':
            md += bt +"  "
        elif btype == 'bookmark':
            md += link(bt,block.link)
        elif btype == "video" or btype == "file" or btype =="audio" or btype =="pdf" or btype == "gist":
            md += link(block.source,block.source)
        elif btype == "bulleted_list" or btype == "toggle":
            md += '- '+bt
        elif btype == "numbered_list":
            numbered_list_index += 1
            md += str(numbered_list_index)+'. ' + bt
        elif btype == "image":
            if not(os.path.isdir(dir)):
                os.makedirs(os.path.join(dir))
            img_count += 1
            img_dir = image_export(block.source,img_count,dir)
            md += "!"+link(img_dir,img_dir)
        elif btype == "code":
            md += "``` "+block.language.lower()+"\n"+block.title+"\n```"
        elif btype == "equation":
            md += "$$"+block.latex+"$$"
        elif btype == "divider":
            md += "---"
        elif btype == "to_do":
            if block.checked:
                md += "- [x] "+ bt
            else:
                md += "- [ ]" + bt
        elif btype == "quote":
            md += "> "+bt
        elif btype == "column" or btype =="column_list":
            continue
        else:
            pass
        md += "\n\n"
    return md

# return the string file.
def export(url,token):
    client = NotionClient(token_v2=token)
    page = client.get_block(url)
    blocks = []
    recursive_getblocks(page,blocks,client)
    md = block2md(blocks,'./')
    return md

# export the markdown file(string).
def export_cli():
    fname,dir = set_filename()
    file = open(fname,'w')
    token_v2, url = get_page()
    blocks = []

    client = NotionClient(token_v2 = token_v2)
    page = client.get_block(url)

    recursive_getblocks(page,blocks,client)
    md = block2md(blocks,dir)

    file.write(md)
    file.close()

    print("\n--- Exporter successfully exported notion page to markdown ---")

if __name__ == "__main__":
    export_cli()
