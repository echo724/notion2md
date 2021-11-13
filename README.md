# Notion Markdown Exporter 2.0 [Updated]

- Notion Markdown Exporter using **official notion api** by [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)

## API Key(Token)

- Before getting started, create [an integration and find the token](https://www.notion.so/my-integrations). → [Learn more about authorization](https://developers.notion.com/docs/authorization).

- Then save your api key(token) as your os environment variable

```{bash}
$ NOTION_TOKEN="{your integration token key}"
```

## Install

```{bash}
$ pip install notion2md
```

## Useage: Shell Command

![notion2md-options](notion2md-options.png)

```{bash}
notion2md
>>Enter Notion Url: URL
```

## Usage: Python
```{python}
from notion2md.exporter import block_exporter

#output_path is optional
block_exporter(target_id,output_path)
```

## To-do

- [ ] Page Exporter
- [ ] Database Exporter
- [ ] export file object(image and files)
- [ ] export child page
 
## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
