from timeit import default_timer


class Timer:
    def __init__(self):
        self._start = 0
        self._end = 0

    @property
    def elapsed(self):
        return self._end - self._start

    def __enter__(self):
        self._start = default_timer()
        return self

    def __exit__(self, exc_type=None, exc_value=None, exc_traceback=None):
        self._end = default_timer()
