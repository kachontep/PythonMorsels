from collections import UserString


class MutableString(UserString):
    def __init__(self, str):
        super().__init__(str)

    def _pos(self, pos):
        return len(self.data) + pos if pos < 0 else pos

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            start_pos = (
                0 if key.start is None else self._pos(key.start)
            )
            stop_pos = (
                len(self.data) if key.stop is None else self._pos(key.stop)
            )
        else:
            start_pos = self._pos(key)
            stop_pos = start_pos + 1
        self.data = (self.data[:start_pos] + value + self.data[stop_pos:])

    def __delitem__(self, key):
        self[key] = ''

    def append(self, s):
        self.data += s

    def insert(self, pos, s):
        self.data = self.data[:self._pos(pos)] + s + self.data[self._pos(pos):]

    def pop(self, pos=-1):
        val = self[pos]
        self[pos] = ''
        return val
