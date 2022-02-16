import unittest

from notion2md.console.application import Application

from cleo.testers.command_tester import CommandTester
from cleo.io.outputs.output import Verbosity

from .config import specific_block_id

class TestCommand(unittest.TestCase):
    def test_execute(self):

        expected = """
<status>  Retrieved Notion blocks...
<status> Converting 29 blocks...
<status>  Converted 29 blocks to Markdown
<status>   Exported "8e3bb46322d54fcf85155f747d205f8d.zip" in "./notion2md-output/"

"""

        app = Application()
        command = app.find('block')

        tester = CommandTester(command)
        tester.execute(f'--id {specific_block_id}',verbosity=Verbosity.DEBUG)
        assert expected == tester.io.fetch_output()
