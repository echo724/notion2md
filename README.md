![Notion2Md logo - an arrow pointing from "N" to "MD"](Notion2md.jpg)

<br/>

## About Notion2Md

[![PyPI version](https://badge.fury.io/py/notion2md.svg)](https://badge.fury.io/py/notion2md)
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fecho724%2Fnotion2md&count_bg=%23949191&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=visited&edge_flat=false"/></a>

- Notion Markdown Exporter using **official notion api** by [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)

## API Key(Token)

- Before getting started, create [an integration and find the token](https://www.notion.so/my-integrations). → [Learn more about authorization](https://developers.notion.com/docs/authorization).

- Then save your api key(token) as your os environment variable

```Bash
$ export NOTION_TOKEN="{your integration token key}"
```

## Install

```Bash
$ pip install notion2md
```

## Usage: Shell Command

![Terminal output of the `notion2md -h` command](notion2md_options.png)

- Notion2md requires either `id` or `url` of the Notion page/block
- **Download** option will download files/images in the `path` directory

```Bash
notion2md --download -n post -p ~/MyBlog/content/posts -u https://notion.so/...
```

- This command will generate "**post.md**" in your '**~/MyBlog/content/posts**' directory

## Usage: Python

```Python
from notion2md.exporter import block_markdown_exporter, block_string_exporter

# block_markdown_exporter will make markdown file on your output path
block_markdown_exporter(id='...',path='...',download=True)

# block_string_exporter will return output as String type
md = block_string_exporter(id='...',path='...')
```

## To-do

- [x] Download file object(image and files)
- [x] Table blocks
- [x] Synced Block
- [ ] Page Exporter
- [ ] Database Exporter
- [ ] Child page
- [ ] Column List and Column Blocks

## Contribution

Please read [Contribution Guide](CONTRIBUTION.md)

## Donation

If you think **Notion2Md** is helpful to you, you can support me here:

<a href="https://www.buymeacoffee.com/echo724" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 54px;" height="54"></a>

## License
[MIT](https://choosealicense.com/licenses/mit/)
