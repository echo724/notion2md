# Changelog

All notable changes to this project will be documented in this file. See
[Conventional Commits](https://conventionalcommits.org) for commit guidelines.

### [2.8.3](https://github.com/echo724/notion2md/compare/v2.8.2...v2.8.3) (2023-06-29)


### Bug Fixes

* constructor in README.md ([03e42c4](https://github.com/echo724/notion2md/commit/03e42c4a8ba2b29a91df243b588a3cbcc6caffdf))

### [2.8.2](https://github.com/echo724/notion2md/compare/v2.8.1...v2.8.2) (2023-02-26)


### Bug Fixes

* fix retrieving over 100 blocks [#46](https://github.com/echo724/notion2md/issues/46) ([a89ce45](https://github.com/echo724/notion2md/commit/a89ce454d5ec53e7721ae326030c603016d7ab57))

### [2.8.1](https://github.com/echo724/notion2md/compare/v2.8.0...v2.8.1) (2022-11-07)


### Bug Fixes

* **pyproject:** fix dependencies' version requirement ([a7f2b04](https://github.com/echo724/notion2md/commit/a7f2b0432d0b2746c381c0c98c20116a727253fb)), closes [#44](https://github.com/echo724/notion2md/issues/44)

## [2.8.0](https://github.com/echo724/notion2md/compare/v2.7.6...v2.8.0) (2022-10-14)


### Features

* Make downloaded filenames consistent between runs ([#38](https://github.com/echo724/notion2md/issues/38)) ([30e8f0b](https://github.com/echo724/notion2md/commit/30e8f0b9ccc9c103cbb7b35746c8ec9bc27ad76b))


### Bug Fixes

* Fixed [#40](https://github.com/echo724/notion2md/issues/40) due to the update of Notion API ([#42](https://github.com/echo724/notion2md/issues/42)) ([1a63351](https://github.com/echo724/notion2md/commit/1a633515ed835e9cda26cd0b5951773f2076a069))

### [2.7.6](https://github.com/echo724/notion2md/compare/v2.7.5...v2.7.6) (2022-03-22)


### Features

* Replace methods to Exporter Classes ([2b35818](https://github.com/echo724/notion2md/commit/2b3581801dfb0e08c7db39053013a8e80a29efdf))


### Bug Fixes

* Change the way of calling get_children function ([4563790](https://github.com/echo724/notion2md/commit/4563790cff4f39e1625de2c748fe85bd9e0725c8))
* Implemented Singletone pattern in NotionClient class ([b8443ba](https://github.com/echo724/notion2md/commit/b8443ba963267a4ede3df9e782d07d3001b0b8d6))

### [2.7.5](https://github.com/echo724/notion2md/compare/v2.7.4...v2.7.5) (2022-03-01)


### Bug Fixes

* Remove Singleton pattern in Config class ([#31](https://github.com/echo724/notion2md/issues/31)) ([2de75e3](https://github.com/echo724/notion2md/commit/2de75e367e1a4cea0bf8c4c0bd31b05f805e8f8b))

<!--next-version-placeholder-->

## v2.7.4 (2022-02-21)
### Fix
* Remove exclamation mark in front of square brackets in bookmark convertor ([`4c37b0d`](https://github.com/echo724/notion2md/commit/4c37b0dc2564c0b55f57e65bb1b576f8e70e47bd))

## v2.7.3 (2022-02-20)
### Fix
* Fix exporter methods passing positional arguments to Config class to dict ([`3c66ca3`](https://github.com/echo724/notion2md/commit/3c66ca3b094f7511b0107c62cb5e80f9408a3a30))

## v2.7.2 (2022-02-20)
### Fix
* Change importing method names typo ([`f14ad98`](https://github.com/echo724/notion2md/commit/f14ad98d3f48ffeb874594fab77af2c47136e51c))

## v2.7.1 (2022-02-19)
### Fix
* Indicate parameters explicitly in Config Object ([`7ea65a4`](https://github.com/echo724/notion2md/commit/7ea65a432cc860bdc294984344bd5f43c7d6b885))

## v2.7.0 (2022-02-18)
### Feature
* Add a case if there is no extension, notion2md won't download the file ([`a8965a8`](https://github.com/echo724/notion2md/commit/a8965a833856fe713128dbedb5146b06c5ddc724))

## v2.6.3 (2022-02-17)
### Fix
* Fix block_string_exporter not downloading files ([`f46f31c`](https://github.com/echo724/notion2md/commit/f46f31cc4629b8e976028fb5fe25c9ef9d11e5d2))

## v2.6.2 (2022-02-14)
### Fix
* Add time indicator while retrieving blocks ([`48532fd`](https://github.com/echo724/notion2md/commit/48532fd8f9a25b1cd2b88f5e271d67b4e94ea8da))

## v2.6.1 (2022-02-13)
### Fix
* Fix methods' name in exporter __init__ ([`4cada7d`](https://github.com/echo724/notion2md/commit/4cada7da7f86a030284d70612fbfbfc04f13cd5e))
* Fix output for the case if io is not given ([`457a048`](https://github.com/echo724/notion2md/commit/457a0481fb019ca67447fbd987d321ec6e160796))

### Documentation
* Add unzipped option explanation ([`00df4d6`](https://github.com/echo724/notion2md/commit/00df4d64b08b2eca97ee331a9fe29f35b2c1543e))

## v2.6.0 (2022-02-11)
### Feature
* Exporting Notion block files to a single zip ([`d32afde`](https://github.com/echo724/notion2md/commit/d32afde66903c9c7191a2a87b1d2de4b19388909))

## v2.5.2 (2022-02-11)
### Fix
* Include config.py to the package ([`73078d7`](https://github.com/echo724/notion2md/commit/73078d7a9ff8dc420a4b2d1771325dc2c4275353))

## v2.5.1 (2022-02-11)
### Fix
* Fix notion2md.config module import error ([`baafa44`](https://github.com/echo724/notion2md/commit/baafa442f608c64dae800038a334bdfe45ee052a))
* Fix config module not found error ([`7a1f18c`](https://github.com/echo724/notion2md/commit/7a1f18c3234c5c6582737e013dc40683847fa963))

## v2.5.0 (2022-02-11)
### Feature
* Change block object convert methods to class ([`0f38d9a`](https://github.com/echo724/notion2md/commit/0f38d9adbc532e16cd04091d3cb8768f01432070))
* Implemented Cleo for managing cli application ([`305f533`](https://github.com/echo724/notion2md/commit/305f533e770d9d3bfd4104cc38df4a7096bd4f6f))

## v2.4.1 (2022-02-04)
### Fix
* Fix typo ([`31bda67`](https://github.com/echo724/notion2md/commit/31bda67e083c499dad3c42ed5f520eeeceff9670))

## v2.4.0 (2022-02-03)
### Feature
* Add block to string exporter ([`26981f5`](https://github.com/echo724/notion2md/commit/26981f5cf1cfdd7e263a64758ba09e8f83cffcad))
* Add "download" option so that user can choose whether to download files or not ([`bddcc40`](https://github.com/echo724/notion2md/commit/bddcc4071a7b2ef434b8782eff177c1a27757fb3))

### Documentation
* Add python usage description ([`e10687e`](https://github.com/echo724/notion2md/commit/e10687e2e9a986f9d261bd8007038222d2a8447b))
* Checked Synced Block ([`791f779`](https://github.com/echo724/notion2md/commit/791f779a728b0f6ac17d6c807f573cb500ca2a06))
* Update notion2md options image ([`7d1b263`](https://github.com/echo724/notion2md/commit/7d1b26322b9ec2c8c2ec1631cf84e6a601b57427))
* Add download option description ([`004202b`](https://github.com/echo724/notion2md/commit/004202bd69f304864a5e3c938f183ec116b11f18))

## v2.3.3 (2022-02-03)
### Fix
* Synced Block commented out #26 ([`c623a98`](https://github.com/echo724/notion2md/commit/c623a98f1da556c4acdfbef0b7688ea66351e6ef))
* Change the api of block_exporter without creating config file from user ([`2cd8bb8`](https://github.com/echo724/notion2md/commit/2cd8bb82d9c92823f568163c22f69ee1a3bcfed6))
* Change the way of saving a file name using uuid #27 ([`52dd12a`](https://github.com/echo724/notion2md/commit/52dd12af851fcb324507d45395e5d5b6d12356d6))
* Update os.getenv ([`29d5167`](https://github.com/echo724/notion2md/commit/29d5167da47b268bd8574ce129825fa6c9fcb8ed))
* Update ([`8a8193c`](https://github.com/echo724/notion2md/commit/8a8193c66ab441e104f790c0b0eb53fe1c6945dd))

### Documentation
* Add a donation button on README.md ([`51d84cc`](https://github.com/echo724/notion2md/commit/51d84cc275612c2e388d66257562890b6d8e612e))

## v2.3.2 (2022-01-22)
### Fix
* Merge error ([`a4244c0`](https://github.com/echo724/notion2md/commit/a4244c0064db5deb797ad64953f8ab07e5fb5d6b))
* Change directory of downloaded files ([`452cc69`](https://github.com/echo724/notion2md/commit/452cc69f56972ee15b721ffda19a3c39ac404bd8))

### Documentation
* Change Contribution guide in README.md ([`2c2c1da`](https://github.com/echo724/notion2md/commit/2c2c1daef50127995384dde4df57b21d789ca653))
* Add CONTRIBUTE.md ([`18be264`](https://github.com/echo724/notion2md/commit/18be264b4ed41eaee9c76f59f200714e47772bac))

## v2.3.1 (2022-01-17)
### Fix
* Key error ([`af224a6`](https://github.com/echo724/notion2md/commit/af224a62580551df3e2c49aa361c359175dd9eea))

## v2.3.0 (2022-01-17)
### Feature
* Add file(image) downloader #20 ([`d42a1a0`](https://github.com/echo724/notion2md/commit/d42a1a02975181b05d9290f12adc3f7bc2b87c51))

## v2.2.8 (2022-01-11)
### Fix
* Fix name of image in block converter ([`757e253`](https://github.com/echo724/notion2md/commit/757e2534a55eafa9041d0f24b340504f09f92892))

## v2.2.7 (2022-01-11)
### Fix
* Add handling 'mention' object to fix #18 ([`291b2c1`](https://github.com/echo724/notion2md/commit/291b2c1867d766e996168c6157dabf8ba25f9c03))
* Change ERROR color to RED ([`1ac9c80`](https://github.com/echo724/notion2md/commit/1ac9c8013c247b132743795ed1260027d4067c63))

## v2.2.6 (2022-01-11)
### Documentation
* Update README.md ([`ff115cb`](https://github.com/echo724/notion2md/commit/ff115cb091520843eaa18cf691e147db076e8fc0))

## v2.2.5 (2021-12-21)
### Fix
* Unpacking config dick error ([`6d0b105`](https://github.com/echo724/notion2md/commit/6d0b105c05ab12671d930dd61e72f7014985bb09))

## v2.2.4 (2021-12-21)
### Fix
* Format console output ([`bf27ced`](https://github.com/echo724/notion2md/commit/bf27ced9eed5dfa173331a53aa76c9dd52f05499))
* Refactorize exporter ([`661e3f8`](https://github.com/echo724/notion2md/commit/661e3f85e432674adbf2009fd0165af4e02cb543))
* Add checking version ([`2c9a6c1`](https://github.com/echo724/notion2md/commit/2c9a6c19ff96bfd8ba3073e49f87e5c04fa8edb6))
* Change file name as id because title can cause dir error ([`4db6e0f`](https://github.com/echo724/notion2md/commit/4db6e0f37421d092099929910d5bcbaa7831d332))
* Halt program after token error catched ([`0c356b4`](https://github.com/echo724/notion2md/commit/0c356b4c3e772cb059e3a9fb7321878a89ed0b60))

## v2.2.3 (2021-12-18)
### Fix
* Showing error message when client didn't get client ([`3e07428`](https://github.com/echo724/notion2md/commit/3e07428c96adc37a70c8fcd9cda70dae59873656))

## v2.2.2 (2021-12-16)
### Fix
* Fix script not working ([`e001e75`](https://github.com/echo724/notion2md/commit/e001e75eb8cd7c19f702510008e872cec9e7a331))

## v2.2.1 (2021-12-16)
### Fix
* Fix module names ([`e323911`](https://github.com/echo724/notion2md/commit/e3239110f8a72fd337b58ba2221b0df136f8c6a1))

# Update v2.2

- Stylized terminal output

# Update v2.1

- Improved exporting speed by using MultiThreading

# v2.0

- Notion Markdown Exporter(notion2md) now use **official notion api** by [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)

- Rewrite the structure of the program to use the api and improve the speed and usability of API

## v1.2.2.1

- Supports **Inline Math Code** in the `text block`, `bulleted list`, and `numbered list`. It will Be denoted as `$$<math code>$$`

- Supports Call `export_cli()` with `token_v2`, `url`, and `bmode`

# v1.2.0

- Now Supports Exporting the **inline table block**
    
    - Even the block that has its own page in the table will be exported as **subpage**

- You can choose wheather you will export notion page as `a blog post` or not

    - Blog post format includes frontmatter and Date in Post's name.

# v1.1.0

- Change the output folder name `Notion_Exporter_Output/` to `notion_output/`

- Save token_v2 in `notion_output/notion_token.json` and read it when you use the exporter again.

- Fix the error that `block.icon` is not defined if the block has no icon in the title.

# v1.0.0

- Changed the structure of the exporter to support exporting sub pages and sub files.

- Used Object named '`PageBlockExporter`' to connect supporting functions and attributes.

- Each Exporter has its client(`NotionClient`), page(`notion.Block`), and sub pages' exporter list (`[PageBlockExporter]`)
