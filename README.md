# Notion Markdown Exporter
This is Notion Markdown Exporter using [`notion-py`](https://github.com/jamalex/notion-py)
notion2md will export your [notion.so](http://notion.so) page to markdown formatted file.
## Installation
```Plain Text
pip install notion2md
```
## Usage from CLI
In your Bash/Zsh terminal,
```Bash
$python3 -m notion2md
#Markdown file name: <output file name(without .md)>
#Token_v2: <your token_v2 on notion.so>
#Notion Page Url: <your notion page to export>
```
This will make `.md` file in `your directory/ouput` folder.

## Todo
- make md to jekyll post format
- add other notion type
- add test
- sub page
- sub file
- export media

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
