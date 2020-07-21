import sys
from contextlib import contextmanager

__all__ = ['suppress']


class SuppressContext:
    def __init__(self, exception=None, traceback=None):
        self.exception = exception
        self.traceback = traceback


@contextmanager
def suppress(*exc_clzz):
    if all({not issubclass(exc_clz, Exception) for exc_clz in exc_clzz}):
        raise TypeError("supress accept only an Exception class or subclass")
    context = SuppressContext()
    try:
        yield context
    except:
        _, ex, tb = sys.exc_info()
        if isinstance(ex, exc_clzz):
            context.exception = ex
            context.traceback = tb
        else:
            raise ex
