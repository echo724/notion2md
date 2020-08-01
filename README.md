# Notion Markdown Exporter
[![PyPI version](https://badge.fury.io/py/notion2md.svg)](https://badge.fury.io/py/notion2md)

### The Notion2md is updated to version 1.0.0. Please update the pacakge.

- This is Notion Markdown Exporter using [`notion-py`](https://github.com/jamalex/notion-py)

- **notion2md** will export your [notion.so](http://notion.so) page to markdown formatted file.

## Upadtes

- Changed the structure of the exporter to support exporting sub pages and sub files.

- Used Object named '`PageBlockExporter`' to connect supporting functions and attributes.

- Each Exporter has its client(`NotionClient`), page(`notion.Block`), and sub pages' exporter list (`[PageBlockExporter]`)

## Features

- Converts **almost every block** in the notion's page to Markdown texts

- Downloads **images** and **files** in notion's page

- Exports **Nested Pages** in the page!

- Create **Front Matters** for supporting CMS (Title, Created Date, Tags)

> Add "Created" and "Tags" properties in your page. Then exporter will put them in the md file's front matter.


## Installation
``` bash
pip install notion2md
```

## Usage in Terminal
In your Bash/Zsh terminal,
``` bash
$python3 -m notion2md
#Token_v2: <your token_v2 on notion.so>
#Notion Page Url: <your notion page to export>
```

This will make `<date-page-title>.md` file in `your directory/Notion_Exporter_Output` folder.

## Usage in Python

``` python
from notion2md import *

export_cli()
# Token_v2: <your token_v2 on notion.so>
# Notion Page Url: <your notion page to export>
```

## Output Structure.
The structure of the output looks like this path.

```
Notion_Exporter_Output
└── <main-page-title>/
    ├── <main-page-title>.md
    ├── download/
    │   └── ...
    ├── image/
    │   └── img_1.png
    │   └── ...
    └── subpage/
        └── ...
```

- in `subpage/`, there will be `image/`, `download/`, and `subpage/` folders if there are sub components in `sub page`.

## Todo
- convert other block types to md.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
