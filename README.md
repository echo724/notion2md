![Notion2Md logo - an arrow pointing from "N" to "MD"](Notion2md.jpg)

<br/>

## About Notion2Md

[![Downloads](https://static.pepy.tech/badge/notion2md)](https://pepy.tech/project/notion2md)
[![PyPI version](https://badge.fury.io/py/notion2md.svg)](https://badge.fury.io/py/notion2md)
[![Code Quality](https://github.com/echo724/notion2md/actions/workflows/code_quality.yaml/badge.svg)](https://github.com/echo724/notion2md/actions/workflows/code_quality.yaml)
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fecho724%2Fnotion2md&count_bg=%23949191&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=visited&edge_flat=false"/></a>

- Notion Markdown Exporter using **official notion api** by [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)

### Notion2Medium

- Check out [Notion2Medium](https://github.com/echo724/notion2medium) that publishes a **Medium** post from **Notion** using Notion2Md.

## API Key(Token)

- Before getting started, create [an integration and find the token](https://www.notion.so/my-integrations). → [Learn more about authorization](https://developers.notion.com/docs/authorization).

- Then save your api key(token) as your os environment variable

- From version 2.9.0, you can use `--token` or `-t` option to set your token key.

```Bash
$ export NOTION_TOKEN="{your integration token key}"
```

## Install

```Bash
$ pip install notion2md
```

## Usage: Shell Command

![Terminal output of the `notion2md -h` command](notion2md_options.png)

- Notion2md requires either `id` or `url` of the Notion page/block.

- **download** option will download files/images in the `path` directory.

- **unzipped** option makes Notion2Md export ***unzipped*** output of Notion block.

```Bash
notion2md --download -n post -p ~/MyBlog/content/posts -u https://notion.so/...
```

- This command will generate "**post.zip**" in your '**~/MyBlog/content/posts**' directory.

## Usage: Python

```Python
from notion2md.exporter.block import MarkdownExporter, StringExporter

# MarkdownExporter will make markdown file on your output path
MarkdownExporter(block_id='...',output_path='...',download=True).export()

# StringExporter will return output as String type
md = StringExporter(block_id='...',output_path='...').export()
```

## To-do

- [x] Download file object(image and files)
- [x] Table blocks
- [x] Synced Block
- [ ] Page Exporter
- [ ] Child page
- [ ] Column List and Column Blocks

## Contribution

Please read [Contribution Guide](CONTRIBUTION.md)

## Donation

If you think **Notion2Md** is helpful to you, you can support me here:

<a href="https://www.buymeacoffee.com/echo724" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 54px;" height="54"></a>

## License
[MIT](https://choosealicense.com/licenses/mit/)
