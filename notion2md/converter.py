import os
import requests
from notion import block
from datetime import datetime


class PageBlockConverter:
    def __init__(self, page, blog_mode=-1):
        self.page = page
        self.title = self.page.title
        self.bmode = blog_mode
        if self.bmode:
            # if blog mode we set the page header to markdown top
            self.md = self._page_header()
        else:
            self.md = ""

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
                header += '- ' + tag + '\n'
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
        date = self.page.get_property("created_time")
        formatted_date = date.strftime('%Y-%m-%d')
        return formatted_date

    def getMd(self):
        return self.md

    def page2md(self, page=None):
        """change notion's block to markdown string
        """
        params = {'tap_count': 0, 'img_count': 0, 'num_index': 0}
        if page is None:
            page = self.page
        for i, block in enumerate(page.children):
            try:
                self.block2md(block, params)
            except Exception as e:
                self.md += ""
        self.md = self.md[:-1]

    def block2md(self, block, params):
        if params['tap_count'] != 0:
            self.md += '\n'
            for i in range(params['tap_count']):
                self.md += '\t'
        try:
            btype = block.type
        except:
            pass
        if btype != "numbered_list":
            params['num_index'] = 0
        try:
            bt = block.title
        except:
            pass
        if btype == 'header':
            self.md += "# " + filter_inline_math(block)
        if btype == "sub_header":
            self.md += "## " + filter_inline_math(block)
        if btype == "sub_sub_header":
            self.md += "### " + filter_inline_math(block)
        if btype == 'page':
            # if type is page, we will get the page link and set as link
            self.md += link_format(block.name, block.get_browseable_url())
        if btype == 'text':
            try:
                self.md += filter_inline_math(block)
            except:
                self.md += ""
        if btype == 'bookmark':
            self.md += link_format(bt, block.link)
        if btype == "video" or btype == "file" or btype == "audio" or btype == "pdf" or btype == "gist":
            self.md += link_format(block.source, block.source)
        if btype == "bulleted_list" or btype == "toggle":
            self.md += '- ' + filter_inline_math(block)
        if btype == "numbered_list":
            params['num_index'] += 1
            self.md += str(params['num_index']) + '. ' + filter_inline_math(block)
        if btype == "code":
            self.md += "``` " + block.language.lower() + "\n" + block.title + "\n```"
        if btype == "equation":
            self.md += "$$" + block.latex + "$$"
        if btype == "divider":
            self.md += "---"
        if btype == "to_do":
            if block.checked:
                self.md += "- [x] " + bt
            else:
                self.md += "- [ ]" + bt
        if btype == "quote":
            self.md += "> " + bt
        if btype == "column" or btype == "column_list":
            self.md += ""
        if btype == "collection_view":
            collection = block.collection
            self.md += self.make_table(collection)
        if block.children and btype != 'page':
            params['tap_count'] += 1
            for child in block.children:
                self.block2md(child, params)
            params['tap_count'] -= 1
        if params['tap_count'] == 0:
            self.md += "\n\n"

    def make_table(self, collection):
        columns = []
        row_blocks = collection.get_rows()
        for proptitle in row_blocks[0].schema:
            prop = proptitle['name']
            if prop == "Name":
                columns.insert(0, prop)
            else:
                columns.append(prop)
        table = []
        table.append(columns)
        for row in row_blocks:
            row_content = []
            for column in columns:
                if column == "Name" and row.get("content") is not None:
                    content = self.page2md(row)
                else:
                    content = row.get_property(column)
                if str(type(content)) == "<class 'list'>":
                    content = ', '.join(content)
                if str(type(content)) == "<class 'datetime.datetime'>":
                    content = content.strftime('%b %d, %Y')
                if column == "Name":
                    row_content.insert(0, content)
                else:
                    row_content.append(content)
            table.append(row_content)
        return table_to_markdown(table)


def link_format(name, url):
    """make markdown link format string
    """
    return "[" + name + "]" + "(" + url + ")"


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


def filter_inline_math(block):
    """This function will get inline math code and append it to the text
    """
    text = ""
    elements = block.get("properties")["title"]
    for i in elements:
        if i[0] == "⁍":
            text += "$$" + i[1][0][1] + "$$"
        else:
            text += block.title
    return text


def filter_source_url(block):
    try:
        return block.get('properties')['source'][0][0]
    except:
        return block.title
