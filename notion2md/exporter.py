import os
import requests

class PageBlockExporter:
  def __init__(self,url,client):
    self.client = client
    self.page = self.client.get_block(url)
    self.title = self.page.title
    self.md = self._page_header()
    self.image_dir=""
    self.download_dir=""
    self.sub_exporters = []
    self.file_name = self._set_filename()
  
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
      header += "date: {0}\n".format(self.page.created)
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
    formatted_date = []
    formatted_date.append(str(date.year))
    formatted_date.append(str(date.month))
    formatted_date.append(str(date.day))
    formatted_date = "-".join(formatted_date)
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
    for block in page.children:
        try:
            btype = block.type
        except:
            print(block)
            continue
        if btype != "numbered_list":
            numbered_list_index = 0
        try:
            bt = block.title
        except:
            pass
        if btype == 'header':
            self.md += "# " + bt
        if btype == "sub_header":
            self.md += "## " +bt
        if btype == "sub_sub_header":
            self.md += "### " +bt
        if btype == 'page':
              self.create_sub_folder()
              sub_url = block.get_browseable_url()
              exporter = PageBlockExporter(sub_url,self.client)
              exporter.create_folder(self.sub_dir)
              sub_page_path = exporter.create_file()
              try:
                if "https:" in block.icon:
                    icon = "!"+link_format("",block.icon)
                else:
                    icon = block.icon
              except:
                icon = ""
              self.md += icon + link_format(exporter.file_name,sub_page_path)
              self.sub_exporters.append(exporter)
        if btype == 'text':
            self.md += bt +"  "
        if btype == 'bookmark':
            self.md += link_format(bt,block.link)
        if btype == "video" or btype == "file" or btype =="audio" or btype =="pdf" or btype == "gist":
            self.md += link_format(block.source,block.source)
        if btype == "bulleted_list" or btype == "toggle":
            self.md += '- '+bt
        if btype == "numbered_list":
            numbered_list_index += 1
            self.md += str(numbered_list_index)+'. ' + bt
        if btype == "image":
            img_count += 1
            img_path = self.image_export(block.source,img_count)
            self.md += "!"+link_format(img_path,img_path)
        if btype == "code":
            self.md += "``` "+block.language.lower()+"\n"+block.title+"\n```"
        if btype == "equation":
            self.md += "$$"+block.latex+"$$"
        if btype == "divider":
            self.md += "---"
        if btype == "to_do":
            if block.checked:
                self.md += "- [x] "+ bt
            else:
                self.md += "- [ ]" + bt
        if btype == "quote":
            self.md += "> "+bt
        if btype == "column" or btype =="column_list":
            continue
        if btype == "file":
            self.downlaod_file(block.source,block.title)
            print("\n[Download]'{0}' is saved in 'download' folder".format(block.title))
        if block.children and btype != 'page':
            tapped += 1
            self.page2md(tapped,page=block)
            continue
        self.md += "\n\n"

def link_format(name,url):
    """make markdown link format string
    """
    return "["+name+"]"+"("+url+")"

