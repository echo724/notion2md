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

## Useage: Shell Command

![Terminal output of the `notion2md -h` command](notion2md_terminal.png)

```Bash
notion2md -n post -p ~/MyBlog/content/posts -u https://notion.so/...
```

- This command will generate "**post.md**" in your '**~/MyBlog/content/posts**' directory

## To-do

- [x] Download file object(image and files)
- [x] Table blocks
- [ ] Page Exporter
- [ ] Database Exporter
- [ ] Child page
- [ ] Column List and Column Blocks 
- [ ] Synced Block
 
## Contribution

Please read [Contribution Guide](CONTRIBUTION.md)

## License
[MIT](https://choosealicense.com/licenses/mit/)
