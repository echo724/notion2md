import os
import requests
from datetime import datetime

class PageBlockExporter:
  def __init__(self,url,client,blog_mode):
    self.client = client
    self.page = self.client.get_block(url)
    self.title = self.page.title
    self.bmode = blog_mode
    if self.bmode:
      self.md = self._page_header()
      self.file_name = self._set_filename()
    else:
      self.file_name = self.page.title
      self.md = ""
    self.image_dir=""
    self.download_dir=""
    self.sub_exporters = []
  
  def create_main_folder(self,directory):
    """create folder with file name

      Args:
        directory(Stirng): set empty by default.
    """
    self.dir = directory + self.title +'/'

    if not(os.path.isdir(self.dir)):
        os.makedirs(os.path.join(self.dir))
  
  def create_folder(self,directory):
    """create folder with directory

      Args:
        directory(Stirng): set empty by default.
    """
    self.dir = directory

    if not(os.path.isdir(self.dir)):
        os.makedirs(os.path.join(self.dir))
  
  def create_sub_folder(self):
    """create sub folder with current file name

      Args:
        directory(Stirng): set empty by default.
    """
    self.sub_dir = self.dir + 'subpage/'
    if not(os.path.isdir(self.sub_dir)):
        os.makedirs(os.path.join(self.sub_dir))

  def create_file(self):
    """create md file that md will be stored

      Returns:
        self.file(String): path of file
    """
    file_path = os.path.join(self.dir ,self.file_name + '.md')
    self.file = open(file_path,'w')
    return file_path

  def write_file(self):
    """save markdown output in the file
    """
    self.file.write(self.md)
    self.file.close()
  
  def create_image_foler(self):
    """create image output directory
    """
    self.image_dir = os.path.join(self.dir,'image/')
    if not(os.path.isdir(self.image_dir)):
        os.makedirs(os.path.join(self.image_dir))

  def image_export(self,url,count):
    """make image file based on url and count.

      Args:
        url(Stirng): url of image
        count(int): the number of image in the page

      Returns:
        image_path(String): image_path for the link in markdown
    """
    if self.image_dir is "":
      self.create_image_foler()
    
    image_path = self.image_dir + 'img_{0}.png'.format(count)
    r = requests.get(url, allow_redirects=True)
    open(image_path,'wb').write(r.content)
    return image_path
  
  def create_download_foler(self):
    """create download output directory
    """
    self.download_dir = os.path.join(self.dir,'download/')
    if not(os.path.isdir(self.download_dir)):
        os.makedirs(os.path.join(self.download_dir))

  def downlaod_file(self,url,file_name):
    """download a file in the page.

      Args:
        url(Stirng): url of the downlaod file
        file_name(String): name of the file

      Returns:
        None
    """
    if self.download_dir is "":
      self.create_download_foler()
    
    download_path = self.download_dir + file_name
    r = requests.get(url, allow_redirects=True)
    open(download_path,'wb').write(r.content)
  
  def _page_header(self):
    """return the page's header formatted as Front Matter

      Returns:
        header(Stirng): return Front Matter header
    """
    header = "---\n"
    header += "title: {0}\n".format(self.title)
    try:
      header += "date: {0}\n".format(self._format_date())
    except:
      header += ""
    tags = self._get_tags()
    if len(tags) != 0:
        header += "tags:\n"
        for tag in tags:
            header += '- ' + tag +'\n'
    header += '---\n'
    return header

  def _get_tags(self):
    """return tags in the page

      Condition:
        "Tags" or "tags" property should exit in the page

      Returns:
        tags([String]): tags in "Tags or tags" property in the page
    """
    try:
        tags = self.page.get_property('tags')
    except:
        print("\n[Notice] '{0}' has no Tags".format(self.page.title))
        tags = []
    return tags

  def _format_date(self):
    """return created date in the page

      Condition:
        "created" or "Created" property should exit in the page

      Returns:
        formatted_date(String): formatted created date
    """
    date = self.page.get_property("created")
    formatted_date = date.strftime('%Y-%m-%d')
    return formatted_date

  def _set_filename(self):
    """return formatted file name

      Returns:
        file name(String): formatted_file_name
    """
    try:
        date_in_name = self._format_date() + "-"
    except:
        print("[Notice] '{0}' has no Created Date".format(self.page.title))
        date_in_name = ""
    file_name = date_in_name + self.title.replace(" ","-")
    return file_name
  
  def block2md(self,block):
        try:
            btype = block.type
        except:
            print(block)
            return
        if btype != "numbered_list":
            numbered_list_index = 0
        try:
            bt = block.title
        except:
            pass
        if btype == 'header':
            return "# " + bt
        if btype == "sub_header":
            return "## " +bt
        if btype == "sub_sub_header":
            return "### " +bt
        if btype == 'page':
              self.create_sub_folder()
              sub_url = block.get_browseable_url()
              exporter = PageBlockExporter(sub_url,self.client,self.bmode)
              exporter.create_folder(self.sub_dir)
              sub_page_path = exporter.create_file()
              try:
                if "https:" in block.icon:
                    icon = "!"+link_format("",block.icon)
                else:
                    icon = block.icon
              except:
                icon = ""
              self.sub_exporters.append(exporter)
              return icon + link_format(exporter.file_name,sub_page_path)
        if btype == 'text':
            if bt == "":
              return
            return bt +"  "
        if btype == 'bookmark':
            return link_format(bt,block.link)
        if btype == "video" or btype == "file" or btype =="audio" or btype =="pdf" or btype == "gist":
            return link_format(block.source,block.source)
        if btype == "bulleted_list" or btype == "toggle":
            return '- '+bt
        if btype == "numbered_list":
            numbered_list_index += 1
            return str(numbered_list_index)+'. ' + bt
        if btype == "image":
            img_count += 1
            img_path = self.image_export(block.source,img_count)
            return "!"+link_format(img_path,img_path)
        if btype == "code":
            return "``` "+block.language.lower()+"\n"+block.title+"\n```"
        if btype == "equation":
            return "$$"+block.latex+"$$"
        if btype == "divider":
            return "---"
        if btype == "to_do":
            if block.checked:
                return "- [x] "+ bt
            else:
                return "- [ ]" + bt
        if btype == "quote":
            return "> "+bt
        if btype == "column" or btype =="column_list":
            return
        if btype == "file":
            self.downlaod_file(block.source,block.title)
            print("\n[Download]'{0}' is saved in 'download' folder".format(block.title))
        if btype == "collection_view":
            collection = block.collection
            return self.make_table(collection)
        if block.children and btype != 'page':
            tapped += 1
            self.page2md(tapped,page=block)
    
  def page2md(self,tapped,page=None):
    """change notion's block to markdown string
    """
    if tapped == 0:
        img_count = 0
        numbered_list_index = 0
    else:
        self.md += '\n'
        for i in range(tapped):
            self.md += '\t'
    if page is None:
      page = self.page
    count = 0
    for block in page.children:
        if block != page.children[0]:
          self.md +="\n\n"
        try:
          self.md += self.block2md(block)
        except:
          self.md += ""

  def make_table(self,collection):
    columns = []
    row_blocks=collection.get_rows()
    for proptitle in row_blocks[0].schema:
      prop = proptitle['name']
      if prop == "Name":
          columns.insert(0,prop)
      else:
          columns.append(prop)
    table = []
    table.append(columns)
    for row in row_blocks:
      row_content = []
      for column in columns:
        if column == "Name" and row.get("content") is not None:
            content = self.block2md(row)
        else:
            content = row.get_property(column)
        if str(type(content))=="<class 'list'>":
            content = ', '.join(content)
        if str(type(content)) == "<class 'datetime.datetime'>":
            content = content.strftime('%b %d, %Y')
        if column =="Name":
            row_content.insert(0,content)
        else:
            row_content.append(content)
      table.append(row_content)
    return table_to_markdown(table)

def link_format(name,url):
    """make markdown link format string
    """
    return "["+name+"]"+"("+url+")"

def table_to_markdown(table):
    md = ""
    md += join_with_vertical(table[0])
    md += "\n---|---|---\n"
    for row in table[1:]:
      if row != table[1]:
        md += '\n'
      md += join_with_vertical(row)
    return md

def join_with_vertical(list):
    return " | ".join(list)