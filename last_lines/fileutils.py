import io
import os
from typing import Iterable, Tuple, Iterator


class LastLineIterator:
    def __init__(self, filename):
        self._filename = filename
        self._iterable = None
        self._items = None

    def _read_content(self, content: str, is_end: bool = False) -> Tuple[str, Iterable[str]]:
        remain = ''
        if not is_end:
            try:
                pos = content.index('\n')
                remain = content[:pos+1]
                content = content[pos+1:]
            except ValueError:
                pass
        items = []
        last_pos = 0
        try:
            while True:
                pos = content.index('\n', last_pos)
                items.append(content[last_pos:pos+1])
                last_pos = pos + 1
        except ValueError:
            if last_pos < len(content):
                items.append(content[last_pos:])
        items = reversed(items)
        return remain, items

    def __iter__(self):
        if self._items:
            return self._items
        self._items = []
        with open(self._filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            remaining_size = f.tell()
            remain = ''
            while remaining_size > 0:
                seek_pos = max(0, remaining_size - io.DEFAULT_BUFFER_SIZE)
                read_len = min(remaining_size, io.DEFAULT_BUFFER_SIZE)
                f.seek(seek_pos)
                chunk = f.read(read_len)
                content = chunk + remain
                remain, items = self._read_content(content, seek_pos == 0)
                yield from items
                self._items.append(items)
                remaining_size -= len(chunk)

    def __next__(self):
        self._iterable = self._iterable or iter(self)
        return next(self._iterable)


def last_lines(filename: str) -> Iterator[str]:
    return LastLineIterator(filename)
