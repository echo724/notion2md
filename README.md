# Notion Markdown Exporter
[![PyPI version](https://badge.fury.io/py/notion2md.svg)](https://badge.fury.io/py/notion2md)

- This is Notion Markdown Exporter using [`notion-py`](https://github.com/jamalex/notion-py)

- **notion2md** will export your [notion.so](http://notion.so) page to markdown formatted file.

## [Note from notion2md developer](announcement.md)

## Notice

- Saving images and files is not supported anymore(Maybe the notion's security rule had changed)


## Requirements

- token_v2: check the way to get Token_v2 in Notion-py [Quickstart](https://github.com/jamalex/notion-py#quickstart)

> **Caution** Do not share your `Token_v2` with others. Others can access your notion page if the token is shared.

- url: the link that you will export

## Installation
``` bash
pip install notion2md
```

## Usage in Terminal
In your Bash/Zsh terminal,
``` bash
$python -m notion2md
#Token_v2: <your token_v2 on notion.so>
#Notion Page Url: <your notion page to export>
# Choose you will export the notion page as blog post: [y/n]
```

This will make `<date-page-title>.md` file in `your directory/notion_output` folder.

## Usage in Python

``` python
from notion2md import *

export_cli(token_v2=<Token_v2>,url=<Notion.so Page's url>,bmode=<0 or 1>)

# Without any parameters will call this prompts
# Token_v2: <your token_v2 on notion.so>
# Notion Page Url: <your notion page to export>
# Choose you will export the notion page as blog post: [y/n]
```

## Output Structure.
The structure of the output looks like this path.

```
notion2md_output/
├── notion_token.json
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

## [Change Log](./change_log.md)

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
