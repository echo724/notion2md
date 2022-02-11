from notion2md import __version__

from cleo import Application as BaseApplication

from .commands.export_block import ExportBlockCommand

from .config import ApplicationConfig

class Application(BaseApplication):
    def __init__(self):
        super(Application,self).__init__(
            "notion2md",__version__,config=ApplicationConfig("notion2md",__version__)
        )

        block_command = ExportBlockCommand()

        self.add(block_command.default())
        

def main():
    Application().run()

if __name__ == "__main__":
    main()