# Notion Markdown Exporter
[![PyPI version](https://badge.fury.io/py/notion2md.svg)](https://badge.fury.io/py/notion2md)

This is Notion Markdown Exporter using [`notion-py`](https://github.com/jamalex/notion-py)
notion2md will export your [notion.so](http://notion.so) page to markdown formatted file.

Also, the exporter will download the images in your notion page and save it to the sub folder named with `notion page's title`.

## Installation
```Plain Text
pip install notion2md
```
## Usage in Terminal
In your Bash/Zsh terminal,
```Bash
$python3 -m notion2md
#Markdown file name: <output file name(without .md)>
#Token_v2: <your token_v2 on notion.so>
#Notion Page Url: <your notion page to export>
```
This will make `.md` file in `your directory/notion_ouput` folder.

## Usage in Python

> I changed the way to use the jekyll exporter. Please follow these examples.

### With nothing
```Python
from notion2md import *

export_cli()
```
### With token_v2 & url
```Python
from notion2md import *

token_v2 = #<your notion token_v2>
url = #<your notion page url>

export(url,token_v2)
```

## Additional Info.

- This exporter will make path `<your notion tile>` in your `notion_output` if the page has any image.

## Todo
- export with subpage
- export with subfile

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
