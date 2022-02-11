from cleo.config import ApplicationConfig as BaseApplicationConfig
from clikit.api.formatter import Style
from clikit.api.args.format.argument import Argument
from clikit.api.args.format.option import Option
from clikit.api.event import PRE_HANDLE
from clikit.api.event import PRE_RESOLVE
from clikit.config.default_application_config import DefaultApplicationConfig
from clikit.handler.help import HelpTextHandler
from clikit.resolver.help_resolver import HelpResolver

class ApplicationConfig(BaseApplicationConfig):
    def configure(self):
        self.set_io_factory(self.create_io)
        self.add_event_listener(PRE_RESOLVE, self.resolve_help_command)
        self.add_event_listener(PRE_HANDLE, self.print_version)

        self.add_option("help", "h", Option.NO_VALUE, "Display this help message")
        self.add_option("quiet", "q", Option.NO_VALUE, "Do not output any message")
        self.add_option(
            "verbose",
            "v",
            Option.OPTIONAL_VALUE,
            "Increase the verbosity of messages: "
            '"-v" for normal output, '
            '"-vv" for more verbose output '
            'and "-vvv" for debug',
        )
        self.add_option(
            "version", "V", Option.NO_VALUE, "Display this application version"
        )
        self.add_option("ansi", None, Option.NO_VALUE, "Force ANSI output")
        self.add_option("no-ansi", None, Option.NO_VALUE, "Disable ANSI output")
        self.add_option(
            "no-interaction",
            "n",
            Option.NO_VALUE,
            "Do not ask any interactive question",
        )

        with self.command("help") as c:
            c.set_description("Display the manual of a command")
            c.add_argument(
                "command", Argument.OPTIONAL | Argument.MULTI_VALUED, "The command name"
            )
            c.set_handler(HelpTextHandler(HelpResolver()))

        self.add_style(Style("status").fg("green").bold())
        self.add_style(Style("error").fg("red").bold())
        self.add_style(Style("code").fg("green"))
        self.add_style(Style("highlight").fg("blue").bold())

