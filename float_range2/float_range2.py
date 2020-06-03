import math
from itertools import islice


class float_range:
    def __init__(self, *args):
        num_args = len(args)
        if num_args == 1:
            start, stop, step = None, args[0], None
        elif num_args == 2:
            start, stop, step = args[0], args[1], None
        elif num_args == 3:
            start, stop, step = args
        else:
            raise TypeError

        self.start = start or 0
        self.step = step or 1
        self.stop = stop

        self._len = max([math.ceil((self.stop - self.start) / self.step), 0])
        self._last = self.start + (self.step * (self._len - 1))

    def __iter__(self):
        count = 0
        i = self.start
        while count < self._len:
            yield i
            i += self.step
            count += 1

    def __reversed__(self):
        count = 0
        i = self._last
        while count < self._len:
            yield i
            i -= self.step
            count += 1

    def __len__(self):
        return self._len

    def __eq__(self, other):
        if not isinstance(other, (float_range, range)):
            return other == self

        if self._len == 0 and len(other) == 0:
            return True
        elif self._len != len(other):
            return False

        if self.start != other.start:
            return False
        else:
            if self._len > 1:
                return self.step == other.step
            return True

    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = list(range(*key.indices(self._len)))
            return [k for index, k in enumerate(iter(self)) if index in indices]
        elif isinstance(key, int):
            if key < 0:
                key = self._len + key
            if key < 0 or key >= self._len:
                raise IndexError
            _iter = iter(self)
            for _ in range(key):
                next(_iter)
            return next(_iter)
        else:
            raise TypeError("Key should be int or slice")
