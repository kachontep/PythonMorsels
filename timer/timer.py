from timeit import default_timer


class Timer:
    def __init__(self, fn=None):
        self._start = 0
        self._end = 0
        self._runs = list()
        self._fn = fn

    @property
    def elapsed(self):
        return self._runs[-1] if self._runs else 0

    @property
    def runs(self):
        return self._runs.copy()

    def _record_run(self):
        self._runs.append(self._end - self._start)

    def __enter__(self):
        self._start = default_timer()
        return self

    def __exit__(self, exc_type=None, exc_value=None, exc_traceback=None):
        self._end = default_timer()
        self._record_run()

    def __call__(self, *args, **kwargs):
        with self:
            return self._fn(*args, **kwargs)

    @property
    def min(self):
        return min(self._runs)

    @property
    def max(self):
        return max(self._runs)

    @property
    def mean(self):
        return sum(self._runs) / len(self._runs)

    @property
    def median(self):
        pos, odd = divmod(len(self._runs), 2)
        if odd:
            return self._runs[pos]
        else:
            return (self._runs[pos-1] + self._runs[pos]) / 2
