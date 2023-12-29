import sys
import time

from cleo.commands.command import Command
from cleo.helpers import option

from notion2md.console.formatter import error
from notion2md.console.formatter import status
from notion2md.console.formatter import success
from notion2md.console.ui.indicator import progress
from notion2md.exporter.block import CLIExporter

ARGS_NEW_KEY_MAP = {
    "id": "block_id",
    "url": "block_url",
    "name": "output_filename",
    "path": "output_path",
    "download": "download",
    "unzipped": "unzipped",
    "token": "token",
}


class ExportBlockCommand(Command):
    name = "block"
    description = "Export a Notion block object to markdown."

    options = [
        option("token", "t", "The token of your Notion account.", flag=False),
        option("url", "u", "The url of Notion block object.", flag=False),
        option("id", "i", "The id of Notion block object.", flag=False),
        option("name", "n", "The name of Notion block object", flag=False),
        option(
            "path", "p", "The path to save exported markdown file.", flag=False
        ),
        option(
            "download",
            None,
            "Download files/images inside of the block object",
            flag=True,
        ),
        option(
            "unzipped",
            None,
            "Download unzipped output files/images",
            flag=True,
        ),
    ]
    help = """The block command retrieves and exports Notion <highlight>block object</highlight> to markdownfile.

- By default, the <highlight>id</highlight> of the block will be the name of markdown file,

but if you path a value after <code>--name/-n</code>, the value will be the name of the markdown file.


- It will save the exported zip file in the path(<highlight>"notion-output/"</highlight> or <highlight>specific path you entered</highlight>)

- By default, it won't save files/images in the block object,

but if you pass <code>--download</code> option, it will download files/images in the path(<highlight>"notion-output/"</highlight>

or <highlight>specific path you entered</highlight>)


- By default, it will make a zip file in the output path, but if you want unzipped files, pass <code>--unzipped</code> option.
"""

    def status(self, st, msg):
        self.line(status(st, msg))

    def success(self, st, msg):
        self.line(success(st, msg))

    def error(self, msg):
        self.line_error(error(msg))
        sys.exit(1)

    def _parse_args(self):
        args = {}
        for k, v in self.io.input.options.items():
            if k in ARGS_NEW_KEY_MAP:
                args[ARGS_NEW_KEY_MAP[k]] = v
            else:
                pass
        return args

    def handle(self):
        try:
            args = self._parse_args()
            exporter = CLIExporter(**args)
            exporter.io = self.io
            exporter.create_directories()
            # Get actual blocks
            self.line("")
            with progress(
                self.io,
                status("Retrieving", "Notion blocks..."),
                success("Retrieved", "Notion blocks..."),
            ):
                blocks = exporter.get_blocks()
            # Write(Export) Markdown file
            start_time = time.time()
            self.success(
                "Converting", f"<info>{str(len(blocks))}</info> blocks..."
            )
            exporter.export(blocks)
            self.success(
                "Converted",
                f"<info>{str(len(blocks))}</info> blocks to Markdown{f' <dim>({time.time() - start_time:0.1f}s)</dim>' if not self.io.is_debug() else ''}",
            )

            # Compress Output files into a zip file
            if not exporter.config.unzipped:
                exporter.make_zip()
                extension = ".zip"
            else:
                extension = ".md"
            # Result and Time Check
            self.success(
                "Exported",
                f'"<info>{exporter.config.file_name}{extension}</info>" in "<info>./{exporter.config.path_name}/</info>"',
            )
            self.line("")

        except Exception as e:
            self.error(e)
