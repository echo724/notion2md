# v1.1.0

- Change the output folder name Notion_Exporter_Output/ to `notion_output/'

- Save token_v2 in notion_output/notion_token.json and read it when you use the exporter again.

- Fix the error that block.icon is not defined if the block has no icon in the title.

# v1.0.0

- Changed the structure of the exporter to support exporting sub pages and sub files.

- Used Object named '`PageBlockExporter`' to connect supporting functions and attributes.

- Each Exporter has its client(`NotionClient`), page(`notion.Block`), and sub pages' exporter list (`[PageBlockExporter]`)
