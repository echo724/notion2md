from typing import List
from typing import Optional

from cleo.application import Application as BaseApplication
from cleo.commands.command import Command
from cleo.commands.completions_command import CompletionsCommand
from cleo.commands.help_command import HelpCommand
from cleo.formatters.style import Style
from cleo.io.inputs.argument import Argument
from cleo.io.inputs.definition import Definition
from cleo.io.inputs.input import Input
from cleo.io.inputs.option import Option
from cleo.io.io import IO
from cleo.io.outputs.output import Output

from notion2md import __version__

from .commands.export_block import ExportBlockCommand


class Application(BaseApplication):
    def __init__(self):
        super(Application, self).__init__("notion2md", __version__)
        self._default_command = "block"
        self._single_command = True

    @property
    def default_commands(self) -> List[Command]:
        return [HelpCommand(), ExportBlockCommand(), CompletionsCommand()]

    def create_io(
        self,
        input: Optional[Input] = None,
        output: Optional[Output] = None,
        error_output: Optional[Output] = None,
    ) -> IO:
        io = super().create_io(input, output, error_output)

        formatter = io.output.formatter
        formatter.set_style("status", Style("green", options=["bold", "dark"]))
        formatter.set_style("success", Style("green", options=["bold"]))
        formatter.set_style("error", Style("red", options=["bold"]))
        formatter.set_style("code", Style("green", options=["italic"]))
        formatter.set_style("highlight", Style("blue", options=["bold"]))
        formatter.set_style("dim", Style("default", options=["dark"]))

        io.output.set_formatter(formatter)
        io.error_output.set_formatter(formatter)

        return io

    @property
    def _default_definition(self) -> Definition:
        return Definition(
            [
                Argument(
                    "command",
                    required=True,
                    description="The command to execute.",
                ),
                Option(
                    "--help",
                    "-h",
                    flag=True,
                    description=(
                        "Display help for the given command. "
                        f"When no command is given display help for the <info>{self._default_command}</info> command."
                    ),
                ),
                Option(
                    "--version",
                    "-V",
                    flag=True,
                    description="Display this application version.",
                ),
            ]
        )


def main():
    Application().run()


if __name__ == "__main__":
    main()
