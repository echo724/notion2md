![Notion2Md logo - an arrow pointing from "N" to "MD"](Notion2md.jpg)

<br/>

## About Notion2Md

[![PyPI version](https://badge.fury.io/py/notion2md.svg)](https://badge.fury.io/py/notion2md)

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

## Useage: Shell Command

![Terminal output of the `notion2md -h` command](notion2md-options.png)

```Bash
notion2md -p ~/MyBlog/content/posts -u https://notion.so/...
```

## Usage: Python
```Python
from notion2md.exporter import block_exporter

#output_path is optional
block_exporter("id of notion page","OutPut Path(Relative)")
```

## To-do

- [ ] Page Exporter
- [ ] Database Exporter
- [ ] export file object(image and files)
- [ ] export child page
 
## Contribution
Pull requests are welcome. 
1. folk this repo's **develop** branch into yours
2. make changes and push to your **develop** branch repo
3. send pull request from your **develop** branch to this develop branch

"This will be only way to give pull request to this repo. Thank you

## License
[MIT](https://choosealicense.com/licenses/mit/)
