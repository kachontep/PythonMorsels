import os
from os.path import abspath
from contextlib import contextmanager
from shutil import rmtree
from tempfile import mkdtemp

__all__ = ['cd']

SENTINEL = object()


class ContextDirectory:
    def __init__(self, previous, current):
        self.previous = previous
        self.current = current


class ContextDirectoryManager:

    def __init__(self, path):
        if path is SENTINEL:
            tempd = mkdtemp()
            path = tempd
            self._tempd = tempd
        else:
            self._tempd = None
        self._path = abspath(path)

    def __enter__(self):
        self._original = abspath(os.getcwd())
        os.chdir(self._path)
        return ContextDirectory(self._original, self._path)

    def __exit__(self, exc_type=None, exc_value=None, exc_traceback=None):
        os.chdir(self._original)
        if self._tempd:
            rmtree(self._tempd)

    def enter(self):
        return self.__enter__()

    def exit(self):
        return self.__exit__()


def cd(path=SENTINEL):
    return ContextDirectoryManager(path)
