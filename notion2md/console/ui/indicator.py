import time

from contextlib import contextmanager
from typing import Iterator

from cleo.ui.progress_indicator import ProgressIndicator

from notion2md.console.formatter import status


class Indicator(ProgressIndicator):
    def _formatter_elapsed(self):
        elapsed = time.time() - self._start_time
        return f"{elapsed:0.1f}s"


@contextmanager
def progress(io, stmsg, fnmsg) -> Iterator[None]:
    if io.is_debug():
        io.write_line(status("Retrieved", "Notion blocks..."))
        yield
    else:
        indicator = Indicator(io, fmt="{message} <dim>({elapsed:2s})</dim>")
        with indicator.auto(
            stmsg,
            fnmsg,
        ):
            yield
