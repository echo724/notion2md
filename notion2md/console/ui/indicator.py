from cleo.ui.progress_indicator import ProgressIndicator

import time

class Indicator(ProgressIndicator):
    def _formatter_elapsed(self):
        elapsed = time.time() - self._start_time
        return f"{elapsed:0.1f}"