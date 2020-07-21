import sys
from functools import update_wrapper

__all__ = ['suppress']


class SuppressContext:
    def __init__(self, exception=None, traceback=None):
        self.exception = exception
        self.traceback = traceback


class Suppress:
    def __init__(self, *exc_clzz):
        self._exc_clzz = exc_clzz

    def __enter__(self):
        self._context = SuppressContext()
        return self._context

    def __exit__(self, exc_cls, exc_val, exc_tb):
        if isinstance(exc_val, self._exc_clzz):
            self._context.exception = exc_val
            self._context.traceback = exc_tb
            return True

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            with self:
                return f(*args, **kwargs)
        update_wrapper(wrapped, f)
        return wrapped


suppress = Suppress
